# Contains the Student class, Validates Student Data, Converts objects and dictionaries
#ME
class Student:  
    def __init__(self, student_id: str, full_name: str, program: str, year_level: int, email: str):
        if not isinstance(student_id, str):
            raise TypeError(f"student_id must be str like 2026-001. Error: {type(student_id).__name__}")
        if not isinstance(full_name, str):
            raise TypeError(f"full_name must be str like Kristoff Miguel A. Villena. Error: {type(full_name).__name__}")
        if not isinstance(program, str):
            raise TypeError(f"program must be str like BSIT or BSAI. Error: {type(program).__name__}")
        if not isinstance(year_level, int) or isinstance(year_level, bool):
            raise TypeError(f"year_level must be int only from 1 to 4. Error: {type(year_level).__name__}")
        if not (1 <= year_level <= 4):
            raise ValueError(f"year_level must be between 1 and 4. Error: {year_level}")
        if not isinstance(email, str):
            raise TypeError(f"email must be str like kristoffmiguel.villena@uap.asia. Error: {type(email).__name__}")
        self.student_id = student_id
        self.full_name = full_name
        self.program = program
        self.year_level = year_level
        self.email = email
#AI
    def __str__(self):
        return f"{self.student_id} | {self.full_name} | {self.program} | Year {self.year_level} | {self.email}"      
#ME
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "full_name": self.full_name,
            "program": self.program,
            "year_level": self.year_level,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            student_id=str(data["student_id"]),
            full_name=str(data["full_name"]),
            program=str(data["program"]),
            year_level=int(data["year_level"]),
            email=str(data["email"])
        )
