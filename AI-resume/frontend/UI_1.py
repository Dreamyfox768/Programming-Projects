import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class UI:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Resume Generator")
        self.root.geometry("700x700")
        self.root.config(bg="#F4F4F4")

        self.result_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        # Heading
        label = tk.Label(self.root, text="Professional Resume Generator", font=('Helvetica', 16, 'bold'),
                         fg='#2C3E50', bg='#D5DBDB', relief='groove', bd=5, padx=10, pady=10)
        label.pack(pady=10)

        # Form Frame
        form_frame = tk.Frame(self.root, bg="#F4F4F4")
        form_frame.pack(pady=10)

        # Name Fields
        tk.Label(form_frame, text="First Name:",fg="black", bg="#F4F4F4").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.first_name_entry = tk.Entry(form_frame, width=20)
        self.first_name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Last Name:",fg="black", bg="#F4F4F4").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.last_name_entry = tk.Entry(form_frame, width=20)
        self.last_name_entry.grid(row=0, column=3, padx=5, pady=5)

        # Email Fields
        tk.Label(form_frame, text="Email Username:", fg="black",bg="#F4F4F4").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame, width=40)
        self.email_entry.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

        tk.Label(form_frame, text="Email Platform:", fg="black",bg="#F4F4F4").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.email_platform_var = tk.StringVar(value="Gmail")
        platform_options = ["Gmail", "Yahoo", "Outlook", "iCloud", "Other"]
        platform_menu = ttk.Combobox(form_frame, textvariable=self.email_platform_var,
                                     values=platform_options, state="readonly", width=37)
        platform_menu.grid(row=2, column=1, columnspan=3, padx=5, pady=5)

        # Phone Number
        tk.Label(form_frame, text="Phone Number:",fg="black", bg="#F4F4F4").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        self.phone_entry = tk.Entry(form_frame, width=40)
        self.phone_entry.grid(row=3, column=1, columnspan=3, padx=5, pady=5)

        # Skills and Certifications (Separate)
        tk.Label(form_frame, text="Skills:",fg="black", bg="#F4F4F4").grid(row=4, column=0, sticky="ne", padx=5, pady=5)
        self.skills_entry = tk.Text(form_frame, width=28, height=5)
        self.skills_entry.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Certifications:", fg="black",bg="#F4F4F4").grid(row=4, column=2, sticky="ne", padx=5, pady=5)
        self.certifications_entry = tk.Text(form_frame, width=28, height=5)
        self.certifications_entry.grid(row=4, column=3, padx=5, pady=5)

        # Job and Volunteer Experience (Separate)
        tk.Label(form_frame, text="Job Experience:",fg="black", bg="#F4F4F4").grid(row=5, column=0, sticky="ne", padx=5, pady=5)
        self.job_entry = tk.Text(form_frame, width=28, height=5)
        self.job_entry.grid(row=5, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Volunteer Experience:", fg="black",bg="#F4F4F4").grid(row=5, column=2, sticky="ne", padx=5, pady=5)
        self.volunteer_entry = tk.Text(form_frame, width=28, height=5)
        self.volunteer_entry.grid(row=5, column=3, padx=5, pady=5)

        # Result Display
        result_label = tk.Label(self.root, textvariable=self.result_var, bg="#F4F4F4",
                                fg="black", justify="left", font=('Arial', 12), wraplength=650)
        result_label.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.root, bg="#F4F4F4")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Submit", width=15, command=self.submit_info, bg="#2C3E50", fg="black").grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Clear", width=15, command=self.clear_fields, bg="#7F8C8D", fg="black").grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Try Again", width=15, command=self.try_again, bg="#D68910", fg="black").grid(row=0, column=2, padx=10)
        tk.Button(btn_frame, text="Export", width=15, command=self.export_to_file, bg="#27AE60", fg="black").grid(row=0, column=3, padx=10)

    def submit_info(self):
        first_name = self.first_name_entry.get().strip()
        last_name = self.last_name_entry.get().strip()
        email_user = self.email_entry.get().strip()
        platform = self.email_platform_var.get()
        phone = self.phone_entry.get().strip()
        skills = self.skills_entry.get("1.0", tk.END).strip()
        certifications = self.certifications_entry.get("1.0", tk.END).strip()
        job_exp = self.job_entry.get("1.0", tk.END).strip()
        volunteer_exp = self.volunteer_entry.get("1.0", tk.END).strip()

        if not first_name or not last_name or not email_user or not platform or not phone:
            self.result_var.set("Please fill in all required fields.")
            return

        full_name = f"{first_name} {last_name}"
        email_full = f"{email_user}@{platform.lower()}.com"

        result = (
            f"Name: {full_name}\n"
            f"Email: {email_full}\n"
            f"Phone: {phone}\n\n"
            f"Skills:\n{skills}\n\n"
            f"Certifications:\n{certifications}\n\n"
            f"Job Experience:\n{job_exp}\n\n"
            f"Volunteer Experience:\n{volunteer_exp}"
        )
        self.result_var.set(result)

    def clear_fields(self):
        """Clear all fields including name, email, etc."""
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.email_platform_var.set("Gmail")
        self.phone_entry.delete(0, tk.END)
        self.skills_entry.delete("1.0", tk.END)
        self.certifications_entry.delete("1.0", tk.END)
        self.job_entry.delete("1.0", tk.END)
        self.volunteer_entry.delete("1.0", tk.END)
        self.result_var.set("")

    def try_again(self):
        """Clear only content-specific fields, keep name/email/phone."""
        self.skills_entry.delete("1.0", tk.END)
        self.certifications_entry.delete("1.0", tk.END)
        self.job_entry.delete("1.0", tk.END)
        self.volunteer_entry.delete("1.0", tk.END)
        self.result_var.set("")

    def export_to_file(self):
        resume_text = self.result_var.get()
        if not resume_text:
            self.result_var.set("Please generate resume first using Submit.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt")],
                                                 title="Save Resume As")
        if file_path:
            with open(file_path, "w") as file:
                file.write(resume_text)
            self.result_var.set(f"Resume exported to:\n{file_path}")

def main():
    root = tk.Tk()
    app = UI(root)
    root.mainloop()
if __name__ == "__main__":
    main()
