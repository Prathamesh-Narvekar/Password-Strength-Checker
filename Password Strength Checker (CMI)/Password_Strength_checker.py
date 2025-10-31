import re

# Load the blacklist file

def load_blacklist(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print("⚠️ Blacklist file not found. Proceeding without it.")
        return []


def check_password_strength(password, Common_Passwords):
    strength = 0
    remarks = ""

    # Check blacklist
    if password.lower() in [p.lower() for p in Common_Passwords]:
        return "Very Weak", "This password is commonly used. Please choose a different one."

    # Check length
    if len(password) < 6:
        remarks = "Password too short! Must be at least 6 characters."
        return "Weak", remarks
    elif len(password) >= 8:
        strength += 1

    # Check for uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one uppercase letter."

    # Check for lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one lowercase letter."

    # Check for digits
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one number."

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one special character (!@#$ etc)."

    # Determine strength level
    if strength <= 2:
        return "Weak", remarks
    elif strength == 3 or strength == 4:
        return "Medium", remarks
    else:
        return "Strong", remarks


# --- Main Program ---
if __name__ == "__main__":
    blacklist = load_blacklist("Common_Passwords.txt")
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password, blacklist)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:", feedback)
