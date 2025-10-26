import tkinter as tk
from tkinter import filedialog, messagebox
from Personal_Info import Personal        # Custom module/class to store personal info
from Body_notAI import BodyPart2           # Custom module/class to store skills (non-AI related)
from Body_withAI import body_part1         # Custom module/class to store job experience / AI-related info
from Exporttodoc import Exporttodoc       # Custom module/class to export collected data to a Word document

class ResumeUI:
    def __init__(self, root):
        """
        Initialize the main UI class for the Resume Generator application.

        Parameters:
        root (tk.Tk): The root Tkinter window where the GUI will be displayed.
        """
        self.root = root
        self.root.title("Engineering Resume Generator")  # Set the window title
        self.root.geometry("1200x1200")                 # Set window size
        self.root.config(bg="#FFCCCB")                  # Set background color of the main window

        # Dictionaries to hold Entry widgets for different sections
        self.personal_entries = {}  # To store personal info input fields
        self.skills_entries = {}    # To store skills input fields
        self.ai_entries = {}        # To store AI-related input fields

        # Lists to hold dynamically created frames for certificates and jobs
        self.cert_frames = []       # Each item is a dict of Entry widgets for one certificate
        self.job_frames = []        # Each item is a dict of Entry widgets for one job

        # Initialize the GUI sections
        self.create_nav_buttons()      # Top navigation buttons to switch between sections
        self.create_personal_section() # Section for personal info input
        self.create_skills_section()   # Section for skills input
        self.create_ai_section()       # Section for AI-related input
        self.create_cert_section()     # Section for certifications
        self.create_job_section()      # Section for job experience input
        self.create_result_section()   # Section to display generated resume

        # Display the personal info section first by default
        self.show_section("personal")


    # ---------------- Navigation ---------------- #
    # ---------------- Navigation ---------------- #
    def create_nav_buttons(self):
        """
        Create the top navigation buttons for switching between different sections
        of the resume form. Sections include: Personal, Skills, AI, Certification, and Job Experience.
        """

        # Create a container frame for the navigation buttons
        # 'bg' sets the background color of the frame
        nav_frame = tk.Frame(self.root, bg="#D3D3D3")
        # Pack the frame to fill the horizontal space ('x') at the top of the window
        nav_frame.pack(fill="x")

        # Define a dictionary to hold common button styling properties
        # This avoids repeating styling code for each button
        button_style = {"width": 15,  # Button width in text units
                        "fg": "black",  # Text color
                        "bg": "#C0C0C0",  # Background color
                        "font": ("Arial", 11, "bold")}  # Font type, size, and weight

        # Create the "Personal" button
        # When clicked, it calls self.show_section("personal") to display the Personal section
        self.btn_personal = tk.Button(nav_frame,
                                      text="Personal",
                                      command=lambda: self.show_section("personal"),
                                      **button_style)
        # Place the button in the grid at row 0, column 0 with padding
        self.btn_personal.grid(row=0, column=0, padx=5, pady=5)

        # Create the "Skills" button
        # Clicking it switches to the Skills section
        self.btn_skills = tk.Button(nav_frame,
                                    text="Skills",
                                    command=lambda: self.show_section("skills"),
                                    **button_style)
        # Place it in the grid at row 0, column 1
        self.btn_skills.grid(row=0, column=1, padx=5, pady=5)

        # Create the "AI" button
        # Clicking it switches to the AI section
        self.btn_ai = tk.Button(nav_frame,
                                text="AI",
                                command=lambda: self.show_section("ai"),
                                **button_style)
        # Place it in the grid at row 0, column 2
        self.btn_ai.grid(row=0, column=2, padx=5, pady=5)

        # Create the "Certification" button
        # Clicking it switches to the Certification section
        self.btn_cert = tk.Button(nav_frame,
                                  text="Certification",
                                  command=lambda: self.show_section("cert"),
                                  **button_style)
        # Place it in the grid at row 0, column 3
        self.btn_cert.grid(row=0, column=3, padx=5, pady=5)

        # Create the "Job Experience" button
        # Clicking it switches to the Job Experience section
        self.btn_job = tk.Button(nav_frame,
                                 text="Job Experience",
                                 command=lambda: self.show_section("job"),
                                 **button_style)
        # Place it in the grid at row 0, column 4
        self.btn_job.grid(row=0, column=4, padx=5, pady=5)

        """
        Summary:
        - nav_frame is the container for all top navigation buttons.
        - Each button has a consistent style defined in button_style.
        - Clicking a button calls show_section() with the corresponding section name.
        - grid() arranges buttons in a horizontal row with padding for spacing.
        """

    # ---------------- Sections ---------------- #
    def create_personal_section(self):
        """
        Create the 'Personal Information' section of the form. This section includes
        input fields for Full Name, Email, Phone Number, Education, Start/End Dates, and School.
        """

        # Create a frame to hold all personal information widgets
        # 'bg' sets the background color for the entire frame
        self.personal_frame = tk.Frame(self.root, bg="#B3E5FC")

        # Create a label at the top of the personal section to indicate the section title
        # 'font' sets typeface, size, and style
        # 'fg' sets the text color, 'bg' sets the label background color
        tk.Label(self.personal_frame,
                 text="Personal Information",
                 font=('Arial', 14, 'bold'),
                 fg="black",
                 bg="#B3E5FC").pack(pady=10)  # 'pady' adds vertical padding around the label

        # Create a sub-frame to hold the form fields (labels + entry boxes)
        form = tk.Frame(self.personal_frame, bg="#B3E5FC")
        form.pack()  # Pack it into the personal_frame

        # List of field labels for the personal information form
        labels = ["Full Name:", "Email:", "Phone Number:", "Education:", "Start Date:", "End Date:", "School:"]

        # Loop through each label to create a label and entry field
        for i, lbl in enumerate(labels):
            # Create the label widget for the field
            # 'sticky="e"' aligns the label to the right (east)
            # 'padx' and 'pady' add spacing around the label
            tk.Label(form,
                     text=lbl,
                     bg="#B3E5FC",
                     fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)

            # Create an entry widget for user input
            # 'width=40' sets the text box width
            # 'fg' is text color, 'bg' is background color
            # 'insertbackground' sets the cursor color
            entry = tk.Entry(form, width=40, fg="black", bg="#E3F2FD", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)  # Place entry next to its label

            # Store the entry widget in a dictionary for later access
            # This allows retrieving user input from each field
            self.personal_entries[lbl] = entry

        """
        Summary:
        - personal_frame holds all personal info widgets.
        - A top label clearly indicates the section.
        - Each field has a label and an Entry widget aligned in a grid.
        - Entries are stored in self.personal_entries for easy access.
        """

    def create_skills_section(self):
        """
        Create the 'Skills' section of the form. This section includes input fields for
        Operating Systems, Programming Languages, Tools, Applications, and Soft Skills.
        """

        # Create a frame to hold all skills-related widgets
        # 'bg' sets the background color for the frame
        self.skills_frame = tk.Frame(self.root, bg="#F8BBD0")

        # Create a label at the top of the skills section to indicate the section title
        # 'font' sets the typeface, size, and style
        # 'fg' sets the text color, 'bg' sets the label background
        tk.Label(self.skills_frame,
                 text="Skills",
                 font=('Arial', 14, 'bold'),
                 fg="black",
                 bg="#F8BBD0").pack(pady=10)  # 'pady' adds vertical padding around the label

        # Create a sub-frame to hold the form fields (labels + entry boxes)
        form = tk.Frame(self.skills_frame, bg="#F8BBD0")
        form.pack()  # Pack the sub-frame into the skills_frame

        # List of field labels for the skills form
        labels = ["Operating Systems:", "Programming Languages:", "Tools:", "Applications:", "Soft Skills:"]

        # Loop through each label to create a label and corresponding entry widget
        for i, lbl in enumerate(labels):
            # Create the label for the field
            # 'sticky="e"' aligns the label to the right (east)
            # 'padx' and 'pady' add spacing around the label
            tk.Label(form, text=lbl, bg="#F8BBD0", fg="black").grid(row=i, column=0, sticky="e", padx=5, pady=5)

            # Create an entry widget for user input
            # 'width=40' sets the width of the text box
            # 'fg' is the text color, 'bg' is the background color
            # 'insertbackground' sets the cursor color
            entry = tk.Entry(form, width=40, fg="black", bg="#FCE4EC", insertbackground="black")
            entry.grid(row=i, column=1, padx=5, pady=5)  # Place entry next to its label

            # Store the entry widget in a dictionary for later access
            # Allows retrieving user input for each skill field
            self.skills_entries[lbl] = entry

        """
        Summary:
        - skills_frame contains all skill-related widgets.
        - A top label clearly indicates the section.
        - Each skill field has a label and an Entry widget aligned in a grid.
        - Entries are stored in self.skills_entries for easy access.
        """

    def create_ai_section(self):
        """
        Create the 'AI Section' of the form. This section currently has a single field for 'Position'.
        """

        # Create a frame to hold all AI-related widgets
        # 'bg' sets the background color for the frame
        self.ai_frame = tk.Frame(self.root, bg="#C8E6C9")

        # Create a label at the top of the AI section to indicate the section title
        # 'font' sets the typeface, size, and style
        # 'fg' sets the text color, 'bg' sets the label background
        tk.Label(self.ai_frame,
                 text="AI Section",
                 font=('Arial', 14, 'bold'),
                 fg="black",
                 bg="#C8E6C9").pack(pady=10)  # 'pady' adds vertical padding around the label

        # Create a sub-frame to hold the form fields (labels + entry boxes)
        form = tk.Frame(self.ai_frame, bg="#C8E6C9")
        form.pack()  # Pack the sub-frame into the ai_frame

        # Create the label for the 'Position' field
        # 'sticky="e"' aligns the label to the right (east)
        # 'padx' and 'pady' add spacing around the label
        tk.Label(form, text="Position:", bg="#C8E6C9", fg="black").grid(row=0, column=0, sticky="e", padx=5, pady=5)

        # Create an entry widget for the 'Position' field
        # 'width=40' sets the width of the text box
        # 'fg' is the text color, 'bg' is the background color
        # 'insertbackground' sets the cursor color
        entry = tk.Entry(form, width=40, fg="black", bg="#E8F5E9", insertbackground="black")
        entry.grid(row=0, column=1, padx=5, pady=5)  # Place entry next to its label

        # Store the entry widget in a dictionary for later access
        # Allows retrieving user input for the 'Position' field
        self.ai_entries["Position:"] = entry

        """
        Summary:
        - ai_frame contains all AI-related widgets.
        - A top label clearly indicates the section.
        - The section currently has a single field for 'Position'.
        - The entry widget is stored in self.ai_entries for easy access.
        """

    def create_cert_section(self):
        """
        Create the 'Certifications' section of the form.
        This section allows users to add multiple certifications dynamically.
        """

        # Create a frame to hold all certification-related widgets
        # 'bg' sets the background color for the frame
        self.cert_frame = tk.Frame(self.root, bg="#FFF9C4")

        # Create a label at the top of the Certifications section
        # 'font' sets the typeface, size, and style
        # 'fg' sets text color, 'bg' sets label background
        tk.Label(self.cert_frame,
                 text="Certifications",
                 font=('Arial', 14, 'bold'),
                 fg="black",
                 bg="#FFF9C4").pack(pady=10)  # 'pady' adds vertical spacing

        # Create a sub-frame to hold the list of certification entry fields
        self.cert_list_frame = tk.Frame(self.cert_frame, bg="#FFF9C4")
        self.cert_list_frame.pack()  # Pack it into the main cert_frame

        # Call a method to add the initial set of certification fields
        # This is useful for the first/default certification entry
        self.add_cert_fields()

        # Add a button to allow the user to add more certification fields dynamically
        # 'command' specifies the function to call when the button is clicked
        tk.Button(self.cert_frame,
                  text="➕ Add Another Certification",
                  bg="#FFF176",
                  fg="black",
                  command=self.add_cert_fields).pack(pady=10)

        """
        Summary:
        - cert_frame contains all widgets for certifications.
        - A top label clearly indicates the section.
        - cert_list_frame holds all dynamic certification fields.
        - add_cert_fields() initializes the first certification input.
        - A button allows the user to add more certification fields dynamically.
        """

    def add_cert_fields(self):
        """
        Dynamically add a new set of certification input fields.
        Each set includes Certificate Name, Certificate Code, and Date.
        """

        # Create a labeled frame (LabelFrame) for a single certificate block
        # The text of the frame shows which certificate number it is
        # 'bg' sets background color, 'fg' sets text color, 'font' sets font style
        cert_block = tk.LabelFrame(
            self.cert_list_frame,
            text=f"Certificate {len(self.cert_frames) + 1}",
            bg="#FFF9C4",
            fg="black",
            font=('Arial', 11, 'bold')
        )
        # Pack the labeled frame with padding and make it stretch horizontally
        cert_block.pack(padx=10, pady=5, fill="x")

        # Dictionary to hold entry widgets for this certificate
        fields = {}

        # List of labels for the input fields
        for lbl in ["Certificate Name:", "Certificate Code:", "Date:"]:
            # Create a label for each field in the cert_block
            # 'sticky="e"' aligns label to the east/right
            tk.Label(cert_block, text=lbl, bg="#FFF9C4", fg="black").grid(
                row=len(fields), column=0, sticky="e", padx=5, pady=5
            )

            # Create an entry widget for the user to input data
            # 'insertbackground' sets the color of the cursor inside the entry
            entry = tk.Entry(cert_block, width=40, fg="black", bg="#FFFDE7", insertbackground="black")
            entry.grid(row=len(fields), column=1, padx=5, pady=5)

            # Save this entry widget in the fields dictionary
            fields[lbl] = entry

        # Append this dictionary of entry widgets to the main cert_frames list
        # This allows tracking all certificates added dynamically
        self.cert_frames.append(fields)

        """
        Summary:
        - Each call creates a new labeled frame for a certificate.
        - Each certificate block has three input fields: Name, Code, Date.
        - All entries are stored in a dictionary for easy access later.
        - The dictionary is appended to self.cert_frames for tracking multiple certificates.
        """

    def create_job_section(self):
        """
        Create the Job Experience section of the form.
        This section allows dynamic addition of multiple job entries.
        """

        # Create a frame for the entire job section
        # 'bg' sets background color
        self.job_frame = tk.Frame(self.root, bg="#E1BEE7")

        # Create a label for the section title
        # 'font' specifies font style, 'fg' is text color, 'bg' is background color
        tk.Label(
            self.job_frame,
            text="Job Experience",
            font=('Arial', 14, 'bold'),
            fg="black",
            bg="#E1BEE7"
        ).pack(pady=10)  # Add vertical padding

        # Create a frame that will hold all individual job entries dynamically
        self.job_list_frame = tk.Frame(self.job_frame, bg="#E1BEE7")
        self.job_list_frame.pack()  # Pack it into the job section frame

        # Add the first set of job fields by default
        self.add_job_fields()

        # Create a button to add more job fields dynamically
        # Clicking this button calls the add_job_fields method
        tk.Button(
            self.job_frame,
            text="➕ Add Another Job",
            bg="#CE93D8",
            fg="black",
            command=self.add_job_fields
        ).pack(pady=10)  # Add vertical padding

    def add_job_fields(self):
        """
        Add a new set of job fields to the Job Experience section.
        Each job entry includes Position, Company, Start Date, and End Date.
        """

        # Create a labeled frame for a single job entry
        # The title shows the job number dynamically based on how many job frames exist
        # 'bg' sets background color, 'fg' sets text color, 'font' sets title style
        job_block = tk.LabelFrame(
            self.job_list_frame,
            text=f"Job {len(self.job_frames) + 1}",
            bg="#E1BEE7",
            fg="black",
            font=('Arial', 11, 'bold')
        )
        job_block.pack(padx=10, pady=5, fill="x")  # Pack with padding and full width

        # Dictionary to store the entry widgets for this job
        fields = {}

        # Loop over each label to create corresponding Label and Entry widgets
        for lbl in ["Position:", "Company:", "Start Date:", "End Date:"]:
            # Create the label for the field
            tk.Label(
                job_block,
                text=lbl,
                bg="#E1BEE7",
                fg="black"
            ).grid(
                row=len(fields),  # Row number based on how many fields added so far
                column=0,
                sticky="e",  # Align text to the right
                padx=5,
                pady=5
            )

            # Create the entry widget where user can input data
            entry = tk.Entry(
                job_block,
                width=40,
                fg="black",
                bg="#F3E5F5",
                insertbackground="black"  # Cursor color
            )
            entry.grid(
                row=len(fields),  # Align with label
                column=1,
                padx=5,
                pady=5
            )

            # Store the entry widget in the dictionary using the label as key
            fields[lbl] = entry

        # Add this job's fields dictionary to the main job_frames list
        self.job_frames.append(fields)

    # ---------------- Result Section ---------------- #
    def create_result_section(self):
        """
        Create the Result section where the generated resume preview is displayed.
        Includes a scrollable text box and action buttons: Submit, Reset, Export, AI Descriptions.
        """

        # Main frame for the result section
        self.result_frame = tk.Frame(self.root, bg="#F0F0F0")
        self.result_frame.pack(fill="both", expand=True)  # Fill available space

        # Labeled frame for the resume preview
        box_frame = tk.LabelFrame(
            self.result_frame,
            text="Generated Resume Preview",
            bg="#F0F0F0",
            fg="black",
            font=('Arial', 12, 'bold')
        )
        box_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Text widget to display the generated resume
        self.result_text = tk.Text(
            box_frame,
            wrap="word",  # Wrap text at word boundaries
            width=85,
            height=15,
            fg="black",
            bg="#FAFAFA",
            font=('Arial', 11),
            insertbackground="black"  # Cursor color
        )
        self.result_text.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

        # Vertical scrollbar for the text widget
        scrollbar = tk.Scrollbar(box_frame, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")  # Place on the right side
        self.result_text.config(yscrollcommand=scrollbar.set)  # Link scrollbar to text

        # Frame for action buttons below the text box
        btn_frame = tk.Frame(self.result_frame, bg="#F0F0F0")
        btn_frame.pack(pady=10)

        # Submit button to generate resume preview
        tk.Button(
            btn_frame,
            text="Submit",
            width=15,
            bg="#BDBDBD",
            fg="black",
            command=self.submit_info
        ).grid(row=0, column=0, padx=10)

        # Reset button to clear all input fields
        tk.Button(
            btn_frame,
            text="Reset",
            width=15,
            bg="#E0E0E0",
            fg="black",
            command=self.reset_fields
        ).grid(row=0, column=1, padx=10)

        # Export button to save resume as a Word document (.docx)
        tk.Button(
            btn_frame,
            text="Export (.docx)",
            width=15,
            bg="#D7CCC8",
            fg="black",
            command=self.export_to_word
        ).grid(row=0, column=2, padx=10)

        # AI Descriptions button to generate AI-assisted resume descriptions
        tk.Button(
            btn_frame,
            text="AI Descriptions",
            width=15,
            bg="#C5E1A5",
            fg="black",
            command=self.generate_ai_descriptions
        ).grid(row=0, column=3, padx=10)

    # ---------------- Section Navigation ---------------- #
    def show_section(self, section):
        """
        Show the selected section frame and hide all others.
        Also updates the navigation button colors to indicate the active section.
        """

        # Hide all section frames
        for frame in [self.personal_frame, self.skills_frame, self.ai_frame, self.cert_frame, self.job_frame]:
            frame.pack_forget()  # Remove from view without destroying

        # Reset all navigation buttons to default background
        for btn in [self.btn_personal, self.btn_skills, self.btn_ai, self.btn_cert, self.btn_job]:
            btn.config(bg="#C0C0C0")  # Default gray color for inactive buttons

        # Show the selected section and highlight its button
        if section == "personal":
            self.personal_frame.pack(pady=20)  # Add padding for spacing
            self.btn_personal.config(bg="#9E9E9E")  # Darker gray to indicate active
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

    # ---------------- Submit & Reset ---------------- #
    def submit_info(self):
        """
        Gather all user input from the different sections and display
        the full resume in the result text box.
        """

        # Personal Information
        personal_text = "\n".join(
            [f"{k} {v.get().strip()}" for k, v in self.personal_entries.items() if v.get().strip()]
        )

        # Skills
        skills_text = "\n".join(
            [f"{k} {v.get().strip()}" for k, v in self.skills_entries.items() if v.get().strip()]
        )

        # AI Section
        ai_text = "\n".join(
            [f"{k} {v.get().strip()}" for k, v in self.ai_entries.items() if v.get().strip()]
        )

        # Certifications
        certs_list = []
        for cert in self.cert_frames:
            cert_text = ", ".join(
                [f"{k} {v.get().strip()}" for k, v in cert.items() if v.get().strip()]
            )
            if cert_text:
                certs_list.append(cert_text)
        certs_text = "\n".join(certs_list)

        # Job Experience
        jobs_list = []
        for job in self.job_frames:
            job_text = ", ".join(
                [f"{k} {v.get().strip()}" for k, v in job.items() if v.get().strip()]
            )
            if job_text:
                jobs_list.append(job_text)
        jobs_text = "\n".join(jobs_list)

        # Combine all sections
        full_resume = f"{personal_text}\n\n{skills_text}\n\n{ai_text}\n\n{certs_text}\n\n{jobs_text}"

        # Display in the result text box
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, full_resume)

    def reset_fields(self):
        """
        Clear all input fields and the result text box.
        """
        # Clear Personal, Skills, and AI entries
        for entry_dict in [self.personal_entries, self.skills_entries, self.ai_entries]:
            for entry in entry_dict.values():
                entry.delete(0, tk.END)

        # Clear Certifications and Jobs
        for frame_list in [self.cert_frames, self.job_frames]:
            for frame in frame_list:
                for entry in frame.values():
                    entry.delete(0, tk.END)

        # Clear the result preview
        self.result_text.delete(1.0, tk.END)

    # ---------------- Export to Word ---------------- #
    def export_to_word(self):
        """
        Export the filled resume to a .docx file using custom classes
        Personal, BodyPart2, body_part1, and Exporttodoc.
        """
        try:
            file_path = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Word Document", "*.docx")]
            )
            if file_path:
                # Collect Personal info
                personal = Personal()
                personal.full_name = self.personal_entries["Full Name:"].get().strip()
                personal.email = self.personal_entries["Email:"].get().strip()
                personal.phone = self.personal_entries["Phone Number:"].get().strip()
                personal.major = self.personal_entries["Education:"].get().strip()
                personal.start = self.personal_entries["Start Date:"].get().strip()
                personal.end = self.personal_entries["End Date:"].get().strip()
                personal.school = self.personal_entries["School:"].get().strip()

                # Collect Skills info
                skills = BodyPart2()
                skills.os = self.skills_entries["Operating Systems:"].get().strip()
                skills.language = self.skills_entries["Programming Languages:"].get().strip()
                skills.tool = self.skills_entries["Tools:"].get().strip()
                skills.application = self.skills_entries["Applications:"].get().strip()
                skills.soft_skills = self.skills_entries["Soft Skills:"].get().strip()

                # Collect Job Experience
                jobs = body_part1()
                jobs_list = []
                for job in self.job_frames:
                    position = job["Position:"].get().strip()
                    company = job["Company:"].get().strip()
                    start = job["Start Date:"].get().strip()
                    end = job["End Date:"].get().strip()
                    if position and company:
                        jobs_list.append(f"{position} at {company} ({start} - {end})")
                jobs.jobs = jobs_list

                # Export the resume using Exporttodoc
                exporter = Exporttodoc(personal, skills, jobs, file_path)
                exporter.build_resume()
                exporter.export()
                messagebox.showinfo("Export", f"Resume exported successfully to {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export resume: {str(e)}")

    # ---------------- AI Descriptions ---------------- #
    def generate_ai_descriptions(self):
        """
        Placeholder function to integrate AI-generated descriptions.
        Currently inserts a placeholder text into the result box.
        """
        self.result_text.insert(tk.END, "\n\n[AI-generated descriptions would appear here]")

# ---------------- Main ---------------- #
def main():
    """Main function."""
    root = tk.Tk()
    app = ResumeUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
