# Student Record Management System
By Gitplayer100 / Kristoff Miguel A. Villena

---

## 1. Project Title and Purpose
The **Student Record Management System** is a modular, CLI Python application developed to manage student records using OOP principles and persistent storage. 

Its primary purpose of this project is to solve the limitation of in-memory applications where data is lost when the program terminates. By persisting records to **JSON** files and enabling data interchange through **CSV** files, the application ensures that student data survives program restarts, validates input data against domain constraints, and provides a clear user interface for managing student information.

---

## 2. Features
The application provides the following command-line menu operations:
1. **Add Student**: Prompts for student ID, full name, academic program, year level (1–4), and email. Validates each field, rejects empty inputs and duplicates, and saves the new record to storage.
2. **View All Students**: Displays all currently stored records in a structured, readable format including a record count summary. 
3. **Search Student**: Locates and displays an existing student record by unique student ID, or outputs an informative message if not found.
4. **Update Student**: Searches for a student by ID and allows the user to update their name, program, year level, and email address with complete data validation before saving.
5. **Delete Student**: Finds a student by ID, prompts the user for explicit confirmation (`y/n`), and removes the record from both memory and disk upon confirmation.
6. **Import Students from CSV**: Reads student records from `students_import.csv` using `csv.DictReader`. Validates required columns and row data, rejects duplicates and invalid year levels, skips faulty rows without crashing, and saves valid records to JSON.
7. **Export Students to CSV**: Exports all currently stored records to `students_export.csv` with standard header columns (`student_id,full_name,program,year_level,email`) using `csv.DictWriter`.
8. **Exit**: Cleanly terminates the program.

Bonus Feature for the challenge I added:
**Safer Persistence**: Uses temporary files to prevent database corruption during save operations.

---

## 3. File Structure
```
StudentRecordManager/
│
├── main.py                   # Entry point; manages the menu loop and user console interactions
├── student.py                # Contains the Student class (data model, validation, dictionary conversion)
├── student_repository.py     # Contains StudentRepository (JSON persistence, CRUD, CSV import/export)
├── students.json             # Primary persistent JSON database file
├── students_import.csv       # External CSV file used for importing sample student records
├── students_export.csv       # Generated CSV file containing exported student records
├── README.md                 # Project documentation, architecture explanation, and reflection questions
└── screenshots/              # Folder containing screenshot evidence of test executions
```

---

## 4. How to Run
### Prerequisites
- Python 3.10 (Latest).
- Uses only Python standard libraries (`json`, `csv`, `pathlib`, `shutil`, `os`). No third-party packages are needed.
- And all the important files needed (student.py, student_repository, main.py & additionally students_export/import.csv, without these, the program will definitely die out)

### Running the Application
Open a terminal (Command Prompt, PowerShell, or bash), navigate to the project directory, and run `main.py`:

```bash
cd YourFilePath\StudentRecordManager
python main.py
```
Or just run it in VSC/CODE
---

## 5. How Persistence Works
The application uses a hybrid persistence strategy combining JSON, CSV, and in-memory Python objects:

- **JSON (`students.json`) — Primary Persistence:**
  It preserves exact data types (integers, strings, lists) and structured key-value representations across sessions. Every time a student is added, updated, deleted, or imported, the repository immediately updates `students.json` using UTF-8 encoding.
- **CSV (`students_import.csv` & `students_export.csv`) — Data Interchange & Reporting:**
  Used to ingest external batch records (`import_csv`) and export repository snapshots (`export_csv`) for external reporting.
- **Python Objects — Runtime State:**
  While the program is running, student data is represented as instances of the `Student` class loaded into memory inside `StudentRepository`. This enables object-oriented manipulation, encapsulation, and validation during runtime.

---

## 6. OOP Design & Class Responsibilities
The project strictly adheres to the **Separation of Concerns** and **Single Responsibility Principle**:

1. **`Student` (`student.py`):**
   - **Responsibility:** Represents a single student entity.
   - **Key Behaviors:**
     - Encapsulates student attributes (`student_id`, `full_name`, `program`, `year_level`, `email`).
     - Validates fields (rejects empty/whitespace strings, verifies year level is an integer between 1 and 4, validates email syntax).
     - Provides a string representation via `__str__()`.
     - Serializes object state to a dictionary (`to_dict()`) and deserializes from dictionary data (`from_dict()`).

2. **`StudentRepository` (`student_repository.py`):**
   - **Responsibility:** Manages the collection of student objects and handles persistent file operations.
   - **Key Behaviors:**
     - Loads records from `students.json` on startup and handles missing, empty, or corrupt files.
     - Saves records to `students.json` with safer atomic writes.
     - Performs CRUD operations (`add_student`, `search_student`, `update_student`, `delete_student`).
     - Enforces business rules such as uniqueness of `student_id`.
     - Reads from and writes to CSV files (`import_csv`, `export_csv`).

3. **User Interface (`main.py`):**
   - **Responsibility:** Manages user interaction and menu presentation.
   - **Key Behaviors:**
     - Displays the main menu and handles user selection.
     - Collects terminal inputs and displays formatted outputs and error messages.
     - Delegates data processing to `StudentRepository` without directly manipulating files.

---

## 7. Testing Results
https://docs.google.com/document/d/11j3iLVB9Ft9EPTy2cGyR-_GuvBBxd3QvhJNffNmLdXI/edit?usp=sharing - Test Cases (All Success)

---

## 8. Limitations / Unfinished Features
- Data is locally stored (but shouldn't be too much of an issue)
- Search is a bit limited (it requires you to input the ID only which could be tedious and hard to remember by)
- I did not get to add any role based access (therefore whoeveer owns the terminal has full privelege which is a big issue)

---

## 9. AI Assistance Disclosure
(Every AI was used to compress, fix missing data in python commands. Individually they all had their use for one specific thing which i may get to mention)
At first, I used Brave Search + AI to compress my code. learn from it and check the modules for the lessons (you may notice repetitions for student.py but thats because i
didn't want to add an additional dictionary that would essenstially bring down my whole file structure in which i have to change or review every single thing), it properly
worked well at first when I pushed my 2nd commit to my private github repo (so i can transfer between laptops if ever i lose the main) but then as things were starting to
delve deep in main.py + the additional requirements / checklist needed in the assignment, I needed more help so I switched to Gemini to help me in the idea of what i wanted
for the main menu.

The Main Menu i wanted was just a cleaner version because everytime I enter an option, the previous log/text are still in the terminal so i wanted to get rid of that eyesore
(Hence it gave me the idea to import OS and had to redo every single print into a message so that was the newmain.py) and then a filepath issue started to happen so i had to
rely on AI that was locally in my device to try and fix the filepath issue so that it can properly update the students.json file

I used Antigravity CLI (Gemini Model) to fix this filepath issue and I was done with the project. I also used Claude to organize the Test Cases that I have done for this
project (but it was not used in any of the code)

In short:
Every AI - used for compression and fix missing data
Brave AI + Search - to search commands in python that can be shortened 
Gemini - to improve the main menu interface of the old student record 
AntiGravity - to fix filepath
Claude - to organize the test case document/screenshots i made in another document

All generated suggestions were reviewed, modified, and tested by me to ensure full understanding and ownership of the implementation.

---

## 10. Reflection Questions

### 1. What is the difference between an object stored in memory and a record stored in a JSON file?
An object stored in memory only exists when the program is running but once it terminates, so does the object stored in that memory. A record in a JSON file is a static, serialized text string stored that is stored persistently when a program relaunches itself (it is basically the kept save data that is stored in a file inside your storage drive locally)

### 2. Why can you not directly save an ordinary custom Python object using `json.dump()` without converting it into a serializable representation?
json.dump() only understands basic JSON-serializable types like `dict`, `str`, `int`, etc. This is because it cannot automatically translate without a converter.

### 3. What is the difference between JSON serialization and deserialization?
- **Serialization:** The process of converting an in-memory Python object into a serializable format and writing it as a text string
- **Deserialization:** The reverse process of reading a JSON text string from disk, parsing it into Python data types, and reconstructing a full `Student` object 

### 4. Why is JSON suitable for the application's primary storage, while CSV is useful for exchanging tabular data?
JSON is built for programs to keep data types intact (Python can read the JSON file and recreate objects without any delays). 
While CSV is built for spreadsheets, It doesn't have data types but has plain data that is useful for spreadsheet applications (like google sheets or excel)

### 5. What could happen if your application writes directly to the JSON file and the write operation fails midway?
It will just wipe the file but in this case since I used option D, it wipes a temporary file while the real file is untouched

### 6. Why should a CSV import process validate records before adding them to the repository?
External files of CSV cannot be trusted by someone who might've made mistakes inside the file which is why it validates during the import process before dumping all of it
to the student.json (if it never had that process, all that garbage data would saved in the json file with issues.)

### 7. How does separating the `Student`, `StudentRepository`, and menu responsibilities improve maintainability?
Each of these files have their own responsibility, student.py having validate data, student_respository.py being able to edit these records (especially save these records) and main.py to changes to the user interface. This improves maintainbility because you know what file should be change if your are going to make modifications (changing from json to SQLITE by changing the studentrepository, leaving Student and Main.py untouched unless there is something that has to be done in order to adapt to this change)

### 8. If you were to expand this application into a system used by an entire university, what additional features or safeguards would you introduce?
I would recommend a database engine like PostgreSQL to audit logs and record who made changes and when.

---

## 11. Final Challenge Enhancement (Option D: Safer Persistence)
- I chose Option D — Safer persistence and I implemented that in my student_respository.py (lines 34-42)
- What it does is that it writes to temporary file first (with the use of a temp_path) and replaces original file only after write succeeds
- This can prevent database truncation and data loss if a crash occurs during writing.
