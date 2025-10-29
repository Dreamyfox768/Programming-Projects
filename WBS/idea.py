class WBS:
    def __init__(self, name, description="", level=1):
        self.name = name
        self.description = description
        self.level = level
        self.subtasks = []

    def add_subtask(self, subtask):
        if isinstance(subtask, WBS):
            self.subtasks.append(subtask)
        else:
            raise TypeError("Subtask must be an instance of the WBS class")

    def display(self, indent=0):
        print(" " * indent + f"{self.name} (Level {self.level})")
        if self.description:
            print(" " * (indent + 2) + f"Description: {self.description}")
        for subtask in self.subtasks:
            subtask.display(indent + 4)


def main():
    ...



if __name__ == "__main__":
    main()
