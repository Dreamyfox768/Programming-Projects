import tkinter as tk
from tkinter import ttk

def submit_info():
    full_name = name_entry.get().strip()
    email_user = email_entry.get().strip()
    platform = email_platform_var.get()
    phone = phone_entry.get().strip()

    if not full_name or not email_user or not platform or not phone:
        result_var.set("Please fill in all fields.")
        return

    email_full = f"{email_user}@{platform.lower()}.com"
    result = f"Name: {full_name}\nEmail: {email_full}\nPhone: {phone}"
    result_var.set(result)

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_platform_var.set("Gmail")
    result_var.set("")

# Main window
root = tk.Tk()
root.title("Resume Generator")
root.geometry("500x400")
root.config(bg="#89CFF0")

# Heading label
label = tk.Label(root, text="Best Resume Generator", font=('Purisa', 16, 'bold'),
                 fg='purple', bg='pink', relief='raised', bd=10, padx=10, pady=10)
label.pack(pady=10)

# Form frame
form_frame = tk.Frame(root, bg="#89CFF0")
form_frame.pack(pady=10)

# Full Name
tk.Label(form_frame, text="Full Name:", bg="#89CFF0").grid(row=0, column=0, sticky="e", padx=5, pady=5)
name_entry = tk.Entry(form_frame, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Email Username
tk.Label(form_frame, text="Email Username:", bg="#89CFF0").grid(row=1, column=0, sticky="e", padx=5, pady=5)
email_entry = tk.Entry(form_frame, width=30)
email_entry.grid(row=1, column=1, padx=5, pady=5)

# Email Platform Dropdown
tk.Label(form_frame, text="Email Platform:", bg="#89CFF0").grid(row=2, column=0, sticky="e", padx=5, pady=5)
email_platform_var = tk.StringVar()
email_platform_var.set("Gmail")  # default
platform_options = ["Gmail", "Yahoo", "Outlook", "iCloud", "Other"]
platform_menu = ttk.Combobox(form_frame, textvariable=email_platform_var, values=platform_options, state="readonly", width=27)
platform_menu.grid(row=2, column=1, padx=5, pady=5)

# Phone Number
tk.Label(form_frame, text="Phone Number:", bg="#89CFF0").grid(row=3, column=0, sticky="e", padx=5, pady=5)
phone_entry = tk.Entry(form_frame, width=30)
phone_entry.grid(row=3, column=1, padx=5, pady=5)

# Result Display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, bg="#89CFF0", justify="left", font=('Arial', 12))
result_label.pack(pady=10)

# Buttons
btn_frame = tk.Frame(root, bg="#89CFF0")
btn_frame.pack()

submit_btn = tk.Button(btn_frame, text="Submit", width=12, command=submit_info)
submit_btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(btn_frame, text="Clear", width=12, command=clear_fields)
clear_btn.grid(row=0, column=1, padx=10)
clear_btn = tk.Button(btn_frame, text="export", width=12, command=clear_fields)
clear_btn.grid(row=0, column=2, padx=10)

root.mainloop()
