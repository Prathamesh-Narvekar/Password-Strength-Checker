import re
import tkinter as tk
from tkinter import messagebox

# -------------------------
# Load the password blacklist
# -------------------------
def load_blacklist(file_path):
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        messagebox.showwarning("Warning", "⚠️ Blacklist file not found.")
        return []

# -------------------------
# Password strength function
# -------------------------
def check_password_strength(password, blacklist):
    strength = 0
    remarks = ""

    if password.lower() in [p.lower() for p in blacklist]:
        return "Very Weak", "This password is commonly used. Please choose a different one."

    if len(password) < 6:
        remarks = "Password too short! Must be at least 6 characters."
        return "Weak", remarks
    elif len(password) >= 8:
        strength += 1

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one uppercase letter."

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one lowercase letter."

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one number."

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        remarks += "\nAdd at least one special character (!@#$ etc)."

    if strength <= 2:
        return "Weak", remarks
    elif strength == 3 or strength == 4:
        return "Medium", remarks
    else:
        return "Strong", remarks

# -------------------------
# GUI Functionality
# -------------------------
def evaluate_password():
    password = entry.get()
    strength, feedback = check_password_strength(password, blacklist)

    # Update result labels
    strength_label.config(text=f"Password Strength: {strength}")

    # Color code for strength
    colors = {"Very Weak": "red", "Weak": "orange", "Medium": "blue", "Strong": "green"}
    strength_label.config(fg=colors.get(strength, "black"))

    feedback_text.delete("1.0", tk.END)
    feedback_text.insert(tk.END, feedback.strip())

# -------------------------
# GUI Layout
# -------------------------
root = tk.Tk()
root.title("🔐 Password Strength Checker")
root.geometry("450x320")
root.resizable(False, False)

blacklist = load_blacklist("blacklist.txt")

# Title
tk.Label(root, text="PASSWORD STRENGTH CHECKER", font=("Arial", 16, "bold")).pack(pady=10)

# Input box
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Enter Password:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
entry = tk.Entry(frame, show="*", width=30, font=("Arial", 12))
entry.grid(row=0, column=1)

# Check button
tk.Button(root, text="Check Strength", command=evaluate_password, font=("Arial", 12), bg="#0078D7", fg="white", width=18).pack(pady=10)

# Result label
strength_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
strength_label.pack(pady=5)

# Feedback box
tk.Label(root, text="Suggestions / Feedback:", font=("Arial", 12, "bold")).pack()
feedback_text = tk.Text(root, height=6, width=50, font=("Arial", 10))
feedback_text.pack(pady=5)

root.mainloop()
