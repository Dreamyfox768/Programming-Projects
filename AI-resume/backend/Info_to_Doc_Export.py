# resume_builder.py

from docx import Document
from AI_Implementation import body_part1 
from class_for_body import BodyPart2 #not ai
from resumebackend import Personal #personal info
'''
install package 
import and create 
'''

class exporttodoc:
    def __init__(self, data = None):

        self.document = Document()
        self.data = data
        self.personal_info = Personal()  # Instantiate your all import class
        self.vol_job = body_part1
        self.skill_cets = BodyPart2
    def heading(self):
        self.document.add_heading("Resume", level=1)
    def name_personal(self):
        self.personal_info.collect_info()
    def education(self):
        self.personal_info.education()
    def Technical_skills_certs(self):
        self.skill_cets.skill()
        self.skill_cets.certs()
    def exprience_volunteerign(self):
        self.vol_job.job_experience()
        self.vol_job.job_experience()
    def export(self):
        self.document.save("my_exported_document.docx")

def main():
    builder = exporttodoc()
    builder.heading()
    builder.name_personal()
    builder.education()
    builder.Technical_skills_certs()
    builder.exprience_volunteerign()
    builder.export()


if __name__ == "__main__":
    main()




