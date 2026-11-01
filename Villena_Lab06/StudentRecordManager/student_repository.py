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
        self.path = Path(__file__).parent / path
        self.students = self.load_all()

    def load_all(self):
        if not self.path.exists() or self.path.stat().st_size == 0:
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
            print("The student file contains invalid JSON. A backup has been saved.")
            import shutil
            shutil.copy2(self.path, self.path.with_suffix(".corrupt.bak"))
            return []

    # BONUS CHALLENGE OPTION D - SAFER PERSISTENCE (for save_all)
    def save_all(self, students):
        data = [student.to_dict() for student in students]
        temp_path = self.path.with_suffix(".tmp")
        # 1. Write to temporary file first
        with temp_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        # 2. Safely replace original file only after write succeeds
        temp_path.replace(self.path)

    def add_student(self, student: Student):
        if any(s.student_id == student.student_id for s in self.students):
            raise ValueError(f"Student ID '{student.student_id}' already exists.")
        self.students.append(student)
        self.save_all(self.students)

    def update_student(self, student_id: str, full_name: str, program: str, year_level: int, email: str):
        student = self.search_student(student_id)
        if not student:
            return False
        temp = Student(student_id, full_name, program, year_level, email)
        student.full_name = temp.full_name
        student.program = temp.program
        student.year_level = temp.year_level
        student.email = temp.email
        self.save_all(self.students)
        return True

    def search_student(self, student_id: str):
        return next((s for s in self.students if s.student_id == student_id), None)

    def delete_student(self, student_id: str):
        student = self.search_student(student_id)
        if student:
            self.students.remove(student)
            self.save_all(self.students)
            return True
        return False

#CSV PART
    #ME
    def export_csv(self, filepath="students_export.csv"):
        if not self.students:
            return 0

        path = Path(__file__).parent / filepath #AI (pathfile issue)
        fieldnames = ["student_id", "full_name", "program", "year_level", "email"]
        
        with path.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(s.to_dict() for s in self.students)

        return len(self.students)

    def import_csv(self, filepath="students_import.csv"):
        path = Path(__file__).parent / filepath #AI (pathfile issue)
        if not path.exists():
            return None

        imported_count = 0
        rejected_count = 0
            
        with path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            #AI
            for row in reader:
                try:
                    if not all(row.get(field) for field in ["student_id", "full_name", "program", "year_level", "email"]):
                        rejected_count += 1
                        continue
                        
                    year_level = int(row["year_level"])
                    if not (1 <= year_level <= 4):
                        rejected_count += 1
                        continue

                    row["year_level"] = int(row["year_level"])
                    student = Student.from_dict(row)
                
                    if any(s.student_id == student.student_id for s in self.students):
                        rejected_count += 1
                        continue

                    self.students.append(student)
                    imported_count += 1

                except (ValueError, TypeError):
                    rejected_count += 1
                    continue

        if imported_count > 0:
            self.save_all(self.students)

        return imported_count, rejected_count