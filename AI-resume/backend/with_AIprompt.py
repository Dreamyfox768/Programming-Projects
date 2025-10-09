'''
AI implemented oes
job description
volunteer
skills?

non AI
skills?
certs
'''


class body_part2:
    def __init__(self):
        self.num = ''
        self.date = ''
        self.os = ''
        self.langua = ''
        self.tool = ''
        self.application = ''
        self.soft = ''
        self.name = ''
        self.code = ''
        self.store = []
        self.fix = ''

    def skill(self):
        self.os = input("OS:").strip()
        self.langua = input("Language(Software): ").strip()
        self.tool= input("tool: ").strip()
        self.application = input("application: ").strip()
        self.soft= input("softskills: ").strip()

    def certs(self):
        self.num = int(input("enter how many job certs you have, enter zero to move on  "))
        while self.num > 0:
            self.date = input("Enter start date for certs received:").strip()
            self.name = input("Enter name of certification").strip()
            self.code = input(" certification code").strip()
            self.num -= 1
            final = f'{self.name}{self.code}{self.date}'
            self.store.append(final)
    def __str__(self):
        formatted_certs = "\n".join(self.store)
        return (f"Skills|Certifications "
                f"Operating System:{self.os}  \nLanguage: {self.langua}  \n"
                f"Tool: {self.tool} \nApplication: {self.application}  \nsoftskills:{self.soft}  \n"
                f"Certifications|"
                f"{formatted_certs}")

def main():
    print("\n=== information in the body no AI  ===")
    user = body_part2()
    user.skill()
    user.certs()
    print(user)

if __name__ == "__main__":
    main()
