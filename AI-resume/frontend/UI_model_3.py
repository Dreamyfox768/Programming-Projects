import tkinter as tk
from tkinter import filedialog

class ResumeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Resume Generator")
        self.root.geometry("750x900")
        self.root.config(bg="#F0F0F0")  # Light neutral background

        # Store entries
        self.personal_entries = {}
        self.skills_entries = {}
        self.ai_entries = {}
        self.cert_frames = []
        self.job_frames = []

        # Create interface
        self.create_nav_buttons()
        self.create_personal_section()
        self.create_skills_section()
        self.create_ai_section()
        self.create_cert_section()
        self.create_job_section()
        self.create_result_section()

        self.show_section("personal")

    # ===== Navigation Buttons =====
    def create_nav_buttons(self):
        nav_frame = tk.Frame(self.root, bg="#D3D3D3")
        nav_frame.pack(fill="x")

        button_style = {"width": 15, "fg": "black", "bg": "#C0C0C0", "font": ("Arial", 11, "bold")}

        self.btn_personal = tk.Button(nav_frame, text="Personal", command=lambda: self.show_section("personal"), **button_style)
        self.btn_personal.grid(row=0, column=0, padx=5, pady=5)

        self.btn_skills = tk.Button(nav_frame, text="Skills", command=lambda: self.show_section("skills"), **button_style)
        self.btn_skills.grid(row=0, column=1, padx=5, pady=5)

        self.btn_ai = tk.Button(nav_frame, text="AI", command=lambda: self.show_section("ai"), **button_style)
        self.btn_ai.grid(row=0, column=2, padx=5, pady=5)

        self.btn_cert = tk.Button(nav_frame, text="Certification", command=lambda: self.show_section("cert"), **button_style)
        self.btn_cert.grid(row=0, column=3, padx=5, pady=5)

        self.btn_job = tk.Button(nav_frame, text="Job Experience", command=lambda: self.show_section("job"), **button_style)
        self.btn_job.grid(row=0, column=4, padx=5, pady=5)

    # ===== Personal Section =====
    def create_personal_section(self):
        self.personal_frame = tk.Frame(self.root, bg="#B3E5FC")  # Baby Blue
        tk.Label(self.personal_frame, text="Personal Information", font=('Arial', 14, 'bold'),
                 fg="black", bg="#B3E5FC").pack(pady=10)

        form = tk.Frame(self.personal_frame, bg="#B3E5FC")
        form.pack()

        labels = ["Full Name:", "Email:", "Phone Number:", "Education:", "Start Date:", "End Date:", "School:"]
        for i, lbl in enumerate(labels):
            tk.Label(form, text=lbl, bg="#B3E5FC", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(form, width=40, fg="black", bg="#E3F2FD", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.personal_entries[lbl] = entry

    # ===== Skills Section =====
    def create_skills_section(self):
        self.skills_frame = tk.Frame(self.root, bg="#F8BBD0")  # Pastel Pink
        tk.Label(self.skills_frame, text="Skills", font=('Arial', 14, 'bold'),
                 fg="black", bg="#F8BBD0").pack(pady=10)

        form = tk.Frame(self.skills_frame, bg="#F8BBD0")
        form.pack()

        labels = ["Operating Systems:", "Programming Languages:", "Tools:", "Applications:", "Soft Skills:"]
        for i, lbl in enumerate(labels):
            tk.Label(form, text=lbl, bg="#F8BBD0", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(form, width=40, fg="black", bg="#FCE4EC", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.skills_entries[lbl] = entry

    # ===== AI Section =====
    def create_ai_section(self):
        self.ai_frame = tk.Frame(self.root, bg="#C8E6C9")  # Pastel Green
        tk.Label(self.ai_frame, text="AI Section", font=('Arial', 14, 'bold'),
                 fg="black", bg="#C8E6C9").pack(pady=10)

        form = tk.Frame(self.ai_frame, bg="#C8E6C9")
        form.pack()

        tk.Label(form, text="Position:", bg="#C8E6C9", fg="black").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(form, width=40, fg="black", bg="#E8F5E9", insertbackground="black")
        entry.grid(row=0, column=1, padx=5, pady=5)
        self.ai_entries["Position:"] = entry

    # ===== Certification Section =====
    def create_cert_section(self):
        self.cert_frame = tk.Frame(self.root, bg="#FFF9C4")  # Pastel Yellow
        tk.Label(self.cert_frame, text="Certifications", font=('Arial', 14, 'bold'),
                 fg="black", bg="#FFF9C4").pack(pady=10)

        self.cert_list_frame = tk.Frame(self.cert_frame, bg="#FFF9C4")
        self.cert_list_frame.pack()

        self.add_cert_fields()

        tk.Button(self.cert_frame, text="➕ Add Another Certification",
                  bg="#FFF176", fg="black", command=self.add_cert_fields).pack(pady=10)

    def add_cert_fields(self):
        cert_block = tk.LabelFrame(self.cert_list_frame, text=f"Certificate {len(self.cert_frames)+1}",
                                   bg="#FFF9C4", fg="black", font=('Arial', 11, 'bold'))
        cert_block.pack(padx=10, pady=5, fill="x")

        fields = {}
        labels = ["Certificate Name:", "Certificate Code:", "Date:"]
        for i, lbl in enumerate(labels):
            tk.Label(cert_block, text=lbl, bg="#FFF9C4", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(cert_block, width=40, fg="black", bg="#FFFDE7", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            fields[lbl] = entry

        self.cert_frames.append(fields)

    # ===== Job Experience Section =====
    def create_job_section(self):
        self.job_frame = tk.Frame(self.root, bg="#E1BEE7")  # Pastel Purple
        tk.Label(self.job_frame, text="Job Experience", font=('Arial', 14, 'bold'),
                 fg="black", bg="#E1BEE7").pack(pady=10)

        self.job_list_frame = tk.Frame(self.job_frame, bg="#E1BEE7")
        self.job_list_frame.pack()

        self.add_job_fields()

        tk.Button(self.job_frame, text="➕ Add Another Job",
                  bg="#CE93D8", fg="black", command=self.add_job_fields).pack(pady=10)

    def add_job_fields(self):
        job_block = tk.LabelFrame(self.job_list_frame, text=f"Job {len(self.job_frames)+1}",
                                  bg="#E1BEE7", fg="black", font=('Arial', 11, 'bold'))
        job_block.pack(padx=10, pady=5, fill="x")

        fields = {}
        labels = ["Position:", "Company:", "Start Date:", "End Date:"]
        for i, lbl in enumerate(labels):
            tk.Label(job_block, text=lbl, bg="#E1BEE7", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(job_block, width=40, fg="black", bg="#F3E5F5", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            fields[lbl] = entry

        self.job_frames.append(fields)

    # ===== Resume Preview Section =====
    def create_result_section(self):
        self.result_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.result_frame.pack(fill="both", expand=True)

        box_frame = tk.LabelFrame(self.result_frame, text="Generated Resume Preview",
                                  bg="#F0F0F0", fg="black", font=('Arial', 12, 'bold'))
        box_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.result_text = tk.Text(box_frame, wrap="word", width=85, height=15,
                                   fg="black", bg="#FAFAFA", font=('Arial', 11), insertbackground="black")
        self.result_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(box_frame, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)

        btn_frame = tk.Frame(self.result_frame, bg="#F0F0F0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Submit", width=15, bg="#BDBDBD", fg="black", command=self.submit_info).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Reset", width=15, bg="#E0E0E0", fg="black", command=self.reset_fields).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Export", width=15, bg="#F5F5F5", fg="black", command=self.export_to_file).grid(row=0, column=2, padx=10)

    # ===== Show Section =====
    def show_section(self, section):
        for frame in [self.personal_frame, self.skills_frame, self.ai_frame, self.cert_frame, self.job_frame]:
            frame.pack_forget()

        for btn in [self.btn_personal, self.btn_skills, self.btn_ai, self.btn_cert, self.btn_job]:
            btn.config(bg="#C0C0C0")

        if section == "personal":
            self.personal_frame.pack(pady=20)
            self.btn_personal.config(bg="#9E9E9E")
        elif section == "skills":
            self.skills_frame.pack(pady=20)
            self.btn_skills.config(bg="#9E9E9E")
        elif section == "ai":
            self.ai_frame.pack(pady=20)
            self.btn_ai.config(bg="#9E9E9E")
        elif section == "cert":
            self.cert_frame.pack(pady=20)
            self.btn_cert.config(bg="#9E9E9E")
        elif section == "job":
            self.job_frame.pack(pady=20)
            self.btn_job.config(bg="#9E9E9E")

    # ===== Submit =====
    def submit_info(self):
        personal = "\n".join([f"{k} {v.get().strip()}" for k, v in self.personal_entries.items() if v.get().strip()])
        skills = "\n".join([f"{k} {v.get().strip()}" for k, v in self.skills_entries.items() if v.get().strip()])
        ai = "\n".join([f"{k} {v.get().strip()}" for k, v in self.ai_entries.items() if v.get().strip()])

        certs = []
        for cert in self.cert_frames:
            certs.append(", ".join([f"{k} {v.get().strip()}" for k, v in cert.items() if v.get().strip()]))
        certs_text = "\n".join(certs) if certs else "N/A"

        jobs = []
        for job in self.job_frames:
            jobs.append(", ".join([f"{k} {v.get().strip()}" for k, v in job.items() if v.get().strip()]))
        jobs_text = "\n".join(jobs) if jobs else "N/A"

        result = f"=== PERSONAL INFORMATION ===\n{personal or 'N/A'}\n\n"
        result += f"=== SKILLS ===\n{skills or 'N/A'}\n\n"
        result += f"=== AI SECTION ===\n{ai or 'N/A'}\n\n"
        result += f"=== CERTIFICATIONS ===\n{certs_text}\n\n"
        result += f"=== JOB EXPERIENCE ===\n{jobs_text}"

        self.result_text.delete("1.0", tk.END)
        self.result_text.insert(tk.END, result)

    # ===== Reset =====
    def reset_fields(self):
        for section in [self.personal_entries, self.skills_entries, self.ai_entries]:
            for e in section.values():
                e.delete(0, tk.END)

        for cert in self.cert_frames:
            for e in cert.values():
                e.delete(0, tk.END)

        for job in self.job_frames:
            for e in job.values():
                e.delete(0, tk.END)

        self.result_text.delete("1.0", tk.END)

    # ===== Export =====
    def export_to_file(self):
        text = self.result_text.get("1.0", tk.END).strip()
        if not text:
            self.result_text.insert(tk.END, "\n⚠️ Please generate a resume first.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files", "*.txt")],
                                            title="Save Resume As")
        if path:
            with open(path, "w") as f:
                f.write(text)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.END, f"✅ Resume exported successfully to:\n{path}")

# ===== Run App =====
def main():
    root = tk.Tk()
    app = ResumeUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
