# Contains the repository and persistence operations, stores collection of students, loads from and saves records to json
# adds, searches, updates and deletes records, imports from and exports to CSV

#JSON PART
#ME
import json
import csv
from pathlib import Path
from student import Student

class StudentRepository:
    def __init__(self, path="students.json"):
        self.path = Path(path)
        self.students = self.load_all()

    def load_all(self):
        if not self.path.exists():
            return []
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("Expected a list of student records.")
            return [Student.from_dict(item) for item in data]
        except FileNotFoundError:
            print("The student file does not exist.")
            return []
        except json.JSONDecodeError:
            print("The student file contains invalid JSON.")
            return []
        
    def save_all(self, students):
        data = [student.to_dict() for student in students]
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def add_student(self, student: Student):
        if any(s.student_id == student.student_id for s in self.students):
            raise ValueError(f"Student ID '{student.student_id}' already exists.")
        self.students.append(student)
        self.save_all()

    def search_student(self, student_id: str):
        return next((s for s in self.students if s.student_id == student_id), None)

    def delete_student(self, student_id: str):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            self.save_all()
            return True
        return False

#CSV PART
    #ME
    def export_csv(self, filepath="students_export.csv"):
        path = Path(filepath)
        fieldnames = ["student_id", "full_name", "program", "year_level", "email"]
        
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(s.to_dict() for s in self.students)

    def import_csv(self, filepath="students_import.csv"):
        path = Path(filepath)
        if not path.exists():
            return False
            
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            #AI, i couldn't save nor prevent crashes.
            for row in reader:
                row["year_level"] = int(row["year_level"])
                student = Student.from_dict(row)
                
                if not any(s.student_id == student.student_id for s in self.students):
                    self.students.append(student)
                    
        self.save_all(self.students)
        return True