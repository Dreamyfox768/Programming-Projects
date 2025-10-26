'''
ResumeUI Application
This program creates a GUI for generating engineering resumes using AI.
It allows users to input personal info, skills, certifications, and job experiences,
then export them to a Word document or use AI to generate descriptions.
'''

import tkinter as tk
from tkinter import filedialog, messagebox
from Personal_Info import Personal
from Body_notAI import BodyPart2
from Body_withAI import body_part1
from Exporttodoc import Exporttodoc


class ResumeUI:
    """Main class that defines the Resume Generator UI"""

    def __init__(self, root):
        """Initialize the ResumeUI class and build the entire interface"""
        self.root = root
        self.root.title("Engineering Resume Generator with AI")
        self.root.geometry("1200x1200")
        self.root.config(bg="#FFCCCB")  # Set background color

        # Dictionaries to hold user-entered data
        self.personal_entries = {}
        self.skills_entries = {}
        self.cert_frames = []  # List of certification field blocks
        self.job_frames = []   # List of job experience field blocks

        # Build all UI sections
        self.create_nav_buttons()
        self.create_personal_section()
        self.create_skills_section()
        self.create_cert_section()
        self.create_job_section()
        self.create_result_section()

        # Start by showing the personal info section
        self.show_section("personal")

    # -------------------------- NAVIGATION --------------------------
    def create_nav_buttons(self):
        """Create navigation buttons for switching between form sections"""
        nav_frame = tk.Frame(self.root, bg="#D3D3D3")
        nav_frame.pack(fill="x")

        # Define consistent button styling
        button_style = {"width": 15, "fg": "black", "bg": "#C0C0C0", "font": ("Arial", 11, "bold")}

        # Navigation buttons
        self.btn_personal = tk.Button(nav_frame, text="Personal", command=lambda: self.show_section("personal"), **button_style)
        self.btn_personal.grid(row=0, column=0, padx=5, pady=5)

        self.btn_skills = tk.Button(nav_frame, text="Skills", command=lambda: self.show_section("skills"), **button_style)
        self.btn_skills.grid(row=0, column=1, padx=5, pady=5)

        self.btn_cert = tk.Button(nav_frame, text="Certification", command=lambda: self.show_section("cert"), **button_style)
        self.btn_cert.grid(row=0, column=2, padx=5, pady=5)

        self.btn_job = tk.Button(nav_frame, text="Job Experience", command=lambda: self.show_section("job"), **button_style)
        self.btn_job.grid(row=0, column=3, padx=5, pady=5)

    # -------------------------- PERSONAL INFO --------------------------
    def create_personal_section(self):
        """Create the section for personal information inputs"""
        self.personal_frame = tk.Frame(self.root, bg="#B3E5FC")
        tk.Label(self.personal_frame, text="Personal Information", font=('Arial', 14, 'bold'), fg="black", bg="#B3E5FC").pack(pady=10)

        form = tk.Frame(self.personal_frame, bg="#B3E5FC")
        form.pack()

        # Define labels for personal information fields
        labels = ["Full Name:", "Email:", "Phone Number:", "Education:", "Start Date:", "End Date:", "School:"]

        # Create entry widgets dynamically
        for i, lbl in enumerate(labels):
            tk.Label(form, text=lbl, bg="#B3E5FC", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(form, width=40, fg="black", bg="#E3F2FD", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.personal_entries[lbl] = entry  # Store entry widgets for later retrieval

    # -------------------------- SKILLS --------------------------
    def create_skills_section(self):
        """Create the section for entering user skills"""
        self.skills_frame = tk.Frame(self.root, bg="#F8BBD0")
        tk.Label(self.skills_frame, text="Skills", font=('Arial', 14, 'bold'), fg="black", bg="#F8BBD0").pack(pady=10)

        form = tk.Frame(self.skills_frame, bg="#F8BBD0")
        form.pack()

        # Define skill categories
        labels = ["Operating Systems:", "Programming Languages:", "Tools:", "Applications:", "Soft Skills:"]

        for i, lbl in enumerate(labels):
            tk.Label(form, text=lbl, bg="#F8BBD0", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(form, width=40, fg="black", bg="#FCE4EC", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.skills_entries[lbl] = entry

    # -------------------------- CERTIFICATIONS --------------------------
    def create_cert_section(self):
        """Create the section for entering certifications"""
        self.cert_frame = tk.Frame(self.root, bg="#FFF9C4")
        tk.Label(self.cert_frame, text="Certifications", font=('Arial', 14, 'bold'), fg="black", bg="#FFF9C4").pack(pady=10)

        self.cert_list_frame = tk.Frame(self.cert_frame, bg="#FFF9C4")
        self.cert_list_frame.pack()

        # Add the first certification block
        self.add_cert_fields()

        # Button to add more certifications
        tk.Button(self.cert_frame, text="➕ Add Another Certification", bg="#FFF176", fg="black",
                  command=self.add_cert_fields).pack(pady=10)

    def add_cert_fields(self):
        """Add a new set of certification entry fields"""
        cert_block = tk.LabelFrame(self.cert_list_frame, text=f"Certificate {len(self.cert_frames) + 1}", bg="#FFF9C4",
                                   fg="black", font=('Arial', 11, 'bold'))
        cert_block.pack(padx=10, pady=5, fill="x")

        fields = {}
        for lbl in ["Certificate Name:", "Certificate Code:", "Date:"]:
            tk.Label(cert_block, text=lbl, bg="#FFF9C4", fg="black").grid(row=len(fields), column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(cert_block, width=40, fg="black", bg="#FFFDE7", insertbackground="black")
            entry.grid(row=len(fields), column=1, padx=5, pady=5)
            fields[lbl] = entry

        self.cert_frames.append(fields)  # Store the certification entry set

    # -------------------------- JOBS (AI INTEGRATED) --------------------------
    def create_job_section(self):
        """Create the job experience section with AI integration"""
        self.job_frame = tk.Frame(self.root, bg="#E1BEE7")
        tk.Label(self.job_frame, text="Job Experience", font=('Arial', 14, 'bold'), fg="black", bg="#E1BEE7").pack(pady=10)

        self.job_list_frame = tk.Frame(self.job_frame, bg="#E1BEE7")
        self.job_list_frame.pack()

        # Add first job entry fields
        self.add_job_fields()

        # Button to add another job entry
        tk.Button(self.job_frame, text="➕ Add Another Job", bg="#CE93D8", fg="black",
                  command=self.add_job_fields).pack(pady=10)

        # Button to trigger AI description generation
        tk.Button(self.job_frame, text="✨ Generate AI Descriptions", width=25,
                  bg="#C5E1A5", fg="black", command=self.generate_ai_descriptions).pack(pady=10)

    def add_job_fields(self):
        """Add a new set of job experience entry fields"""
        job_block = tk.LabelFrame(self.job_list_frame, text=f"Job {len(self.job_frames) + 1}", bg="#E1BEE7",
                                  fg="black", font=('Arial', 11, 'bold'))
        job_block.pack(padx=10, pady=5, fill="x")

        fields = {}
        for lbl in ["Position:", "Company:", "Start Date:", "End Date:"]:
            tk.Label(job_block, text=lbl, bg="#E1BEE7", fg="black").grid(row=len(fields), column=0, sticky="e", padx=5, pady=5)
            entry = tk.Entry(job_block, width=40, fg="black", bg="#F3E5F5", insertbackground="black")
            entry.grid(row=len(fields), column=1, padx=5, pady=5)
            fields[lbl] = entry

        self.job_frames.append(fields)

    # -------------------------- RESULT / EXPORT --------------------------
    def create_result_section(self):
        """Create the section for previewing and exporting the resume"""
        self.result_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.result_frame.pack(fill="both", expand=True)

        # Text preview area
        box_frame = tk.LabelFrame(self.result_frame, text="Generated Resume Preview", bg="#F0F0F0", fg="black",
                                  font=('Arial', 12, 'bold'))
        box_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.result_text = tk.Text(box_frame, wrap="word", width=85, height=15, fg="black", bg="#FAFAFA",
                                   font=('Arial', 11), insertbackground="black")
        self.result_text.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # Scrollbar for preview text box
        scrollbar = tk.Scrollbar(box_frame, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)

        # Buttons for submit/reset/export actions
        btn_frame = tk.Frame(self.result_frame, bg="#F0F0F0")
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Submit", width=15, bg="#BDBDBD", fg="black", command=self.submit_info).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Reset", width=15, bg="#E0E0E0", fg="black", command=self.reset_fields).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Export (.docx)", width=15, bg="#D7CCC8", fg="black", command=self.export_to_word).grid(row=0, column=2, padx=10)

    # -------------------------- NAVIGATION LOGIC --------------------------
    def show_section(self, section):
        """Show the selected form section and hide others"""
        for frame in [self.personal_frame, self.skills_frame, self.cert_frame, self.job_frame]:
            frame.pack_forget()

        # Reset button background colors
        for btn in [self.btn_personal, self.btn_skills, self.btn_cert, self.btn_job]:
            btn.config(bg="#C0C0C0")

        # Display the selected section
        if section == "personal":
            self.personal_frame.pack(pady=20)
            self.btn_personal.config(bg="#9E9E9E")
        elif section == "skills":
            self.skills_frame.pack(pady=20)
            self.btn_skills.config(bg="#9E9E9E")
        elif section == "cert":
            self.cert_frame.pack(pady=20)
            self.btn_cert.config(bg="#9E9E9E")
        elif section == "job":
            self.job_frame.pack(pady=20)
            self.btn_job.config(bg="#9E9E9E")

    # -------------------------- BUTTON ACTIONS --------------------------
    def submit_info(self):
        """Combine all entered info into one formatted text block"""
        # Collect all entered data from sections
        personal_text = "\n".join([f"{k} {v.get().strip()}" for k, v in self.personal_entries.items() if v.get().strip()])
        skills_text = "\n".join([f"{k} {v.get().strip()}" for k, v in self.skills_entries.items() if v.get().strip()])

        # Certifications
        certs_list = []
        for cert in self.cert_frames:
            cert_text = ", ".join([f"{k} {v.get().strip()}" for k, v in cert.items() if v.get().strip()])
            if cert_text:
                certs_list.append(cert_text)
        certs_text = "\n".join(certs_list)

        # Job experiences
        jobs_list = []
        for job in self.job_frames:
            job_text = ", ".join([f"{k} {v.get().strip()}" for k, v in job.items() if v.get().strip()])
            if job_text:
                jobs_list.append(job_text)
        jobs_text = "\n".join(jobs_list)

        # Combine all parts into one preview
        full_resume = f"{personal_text}\n\n{skills_text}\n\n{certs_text}\n\n{jobs_text}"
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, full_resume)

    def reset_fields(self):
        """Clear all form entries and the result preview"""
        for entry_dict in [self.personal_entries, self.skills_entries]:
            for entry in entry_dict.values():
                entry.delete(0, tk.END)
        for frame_list in [self.cert_frames, self.job_frames]:
            for frame in frame_list:
                for entry in frame.values():
                    entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)

    # -------------------------- EXPORT --------------------------
    def export_to_word(self):
        """Export the generated resume to a .docx file"""
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Document", "*.docx")])
            if file_path:
                # Collect personal info
                personal = Personal()
                personal.full_name = self.personal_entries["Full Name:"].get().strip()
                personal.email = self.personal_entries["Email:"].get().strip()
                personal.phone = self.personal_entries["Phone Number:"].get().strip()
                personal.major = self.personal_entries["Education:"].get().strip()
                personal.start = self.personal_entries["Start Date:"].get().strip()
                personal.end = self.personal_entries["End Date:"].get().strip()
                personal.school = self.personal_entries["School:"].get().strip()

                # Collect skills
                skills = BodyPart2()
                skills.os = self.skills_entries["Operating Systems:"].get().strip()
                skills.language = self.skills_entries["Programming Languages:"].get().strip()
                skills.tool = self.skills_entries["Tools:"].get().strip()
                skills.application = self.skills_entries["Applications:"].get().strip()
                skills.soft_skills = self.skills_entries["Soft Skills:"].get().strip()

                # Collect job data
                jobs = body_part1()
                for job in self.job_frames:
                    position = job["Position:"].get().strip()
                    company = job["Company:"].get().strip()
                    start = job["Start Date:"].get().strip()
                    end = job["End Date:"].get().strip()
                    if position and company:
                        jobs.jobs.append(f"{position} | {company} ({start} - {end})")

                # Export using external class
                exporter = Exporttodoc(personal, skills, jobs, file_path)
                exporter.build_resume()
                exporter.export()
                messagebox.showinfo("Export", f"Resume exported successfully to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export resume: {str(e)}")

    def generate_ai_descriptions(self):
        """Generate AI job descriptions and display them in the preview area"""
        try:
            jobs = body_part1()
            for job in self.job_frames:
                position = job["Position:"].get().strip()
                company = job["Company:"].get().strip()
                start = job["Start Date:"].get().strip()
                end = job["End Date:"].get().strip()
                if position and company:
                    jobs.jobs.append(f"{position} | {company} ({start} - {end})")

            # Notify user while AI is processing
            self.result_text.insert(tk.END, "\n\n[Generating AI Descriptions... please wait]\n")
            self.result_text.update()

            ai_output = jobs.generate_job_descriptions()  # Call AI model method

            # Display generated text
            self.result_text.insert(tk.END, f"\n\n{ai_output}\n")
            self.result_text.see(tk.END)

        except Exception as e:
            messagebox.showerror("AI Error", f"Failed to generate AI descriptions: {e}")


# -------------------------- MAIN --------------------------
def main():
    """Main function to start the Tkinter application"""
    root = tk.Tk()
    app = ResumeUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
