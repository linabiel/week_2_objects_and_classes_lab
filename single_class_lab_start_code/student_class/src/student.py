class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort

    def talk(self):
        return "I can talk!"

    def say_favourite_language(self, favourite_language):
        return f"I love {favourite_language}"
        # "I love " + favourite_language
