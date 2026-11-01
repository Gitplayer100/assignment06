from student import Student
from student_repository import StudentRepository
import os #clears the terminal per choice, just makes it cleaner

def main():
    repo = StudentRepository()
    message = f"Loaded {len(repo.students)} student record(s) from storage."

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #for the display thing, which can be both compatible for windows and mac, this just clears the thing for clean display
        print("=" * 45)
        print("STUDENT RECORD MANAGER")
        print("=" * 45)

        if message:
            print(">>> RESULT:")
            print(message)
            print("-" * 45)
        message = ""

        print("[1] Add Student")
        print("[2] View All Students")
        print("[3] Search Student")
        print("[4] Update Student")
        print("[5] Delete Student")
        print("[6] Import CSV")
        print("[7] Export CSV")
        print("[8] Exit")
        
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            try:
                student_id = input("Student ID: ").strip()
                full_name = input("Full Name: ").strip()
                program = input("Program: ").strip()
                year_level = int(input("Year Level: ").strip())
                email = input("Email: ").strip()
                
                new_student = Student(student_id, full_name, program, year_level, email)
                repo.add_student(new_student)
                message = "Student added and saved!"
            except (ValueError, TypeError) as e:
                message = f"Error: {e}"
            print(f"\n>>> RESULT: {message}")
            input("\nPress Enter to continue.")

        elif choice == "2":
            if not repo.students:
                message = "No student records found."
            else:
                lines = [f"{'ID':<12} | {'Full Name':<20} | {'Program':<10} | {'Yr':<3} | {'Email'}"]
                lines.append("-" * 70)
                for s in repo.students:
                    lines.append(f"{s.student_id:<12} | {s.full_name:<20} | {s.program:<10} | {s.year_level:<3} | {s.email}")
                lines.append(f"Total: {len(repo.students)} record(s).")
                message = "\n".join(lines)

        elif choice == "3":
            student_id = input("Enter Student ID to search: ").strip()
            student = repo.search_student(student_id)
            if student:
                print(f"\nFound: {student}")
            else:
                print("Student not found.")
            input("\nPress Enter to return to menu.")

        elif choice == "4":
            student_id = input("Enter Student ID to update: ").strip()
            student = repo.search_student(student_id)
            if not student:
                message = "Student not found."
            else:
                try:
                    print(f"Current details: {student}")
                    full_name = input("New Full Name: ").strip()
                    program = input("New Program: ").strip()
                    year_level = int(input("New Year Level: ").strip())
                    email = input("New Email: ").strip()
                    
                    repo.update_student(student_id, full_name, program, year_level, email)
                    message = "Student updated!"
                except (ValueError, TypeError) as e:
                    message = f"Error: {e}"
            print(f"\n>>> RESULT: {message}")
            input("\nPress Enter to continue.")

        elif choice == "5":
            student_id = input("Enter Student ID to delete: ").strip()
            student = repo.search_student(student_id)
            if not student:
                message = "Student not found."
            else:
                confirm = input(f"Are you sure you want to delete {student.full_name}? (y/n): ").strip().lower()
                if confirm == 'y':
                    repo.delete_student(student_id)
                    message = "Student deleted."
                else:
                    message = "Deletion cancelled."
            print(f"\n>>> RESULT: {message}")
            input("\nPress Enter to continue.")

        elif choice == "6":
            result = repo.import_csv()
            if result is None:
                message = "Import file not found."
            else:
                imported, rejected = result
                message = f"Successfully imported!. Imported: {imported} record(s). Rejected: {rejected} record(s)."
            print(f"\n>>> RESULT: {message}")
            input("\nPress Enter to continue.")

        elif choice == "7":
            count = repo.export_csv()
            if count == 0:
                message = "No student record to export."
            else:
                message = f"Succesfully exported! Exported {count} record(s) to 'students_export.csv'."
            print(f"\n>>> RESULT: {message}")
            input("\nPress Enter to continue.")

        elif choice == "8":
            print("Exiting program.")
            break
        else:
            message = "Please enter a number between 1 and 8."
            input("\nPress Enter to continue.")

if __name__ == "__main__":
    main()