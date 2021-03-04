class Course:
    def __init__(self, department: str = "csse", number: str = "120",
                 term: int = 202130):
        self.department = department
        self.number = number
        self.term = term
        session_names = []  # TODO: Get from file
        self.sessions = [Session(name) for name in session_names]


class Session:
    def __init__(self, name: str = None):
        self.name = name
        self.id, self.topic = self.parse_name()
        module_names = []  # TODO: Get from file
        self.modules = [Module(name) for name in module_names]

    def parse_name(self):
        return self.name.split("-")


class Module:
    def __init__(self, number: int = None):
        self.number = number
