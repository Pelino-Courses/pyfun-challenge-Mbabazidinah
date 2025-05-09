class Person:
    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string")
        self.name = name

    def get_role(self):
        return "Person"
