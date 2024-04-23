from utils.logger import logger
from utils.llm_requests import (
    generate_table_descriptions,
    llm_generate_json,
)
from utils.embeddings_manager import EmbeddingsManager

db_context = """
-- Departments Table
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Budget DECIMAL(12, 2) NOT NULL,
    StartDate DATE NOT NULL
);

-- Instructors Table
CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Courses Table
CREATE TABLE Courses (
    CourseID INT AUTO_INCREMENT PRIMARY KEY,
    Title VARCHAR(100),
    Credits INT,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- Students Table
CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    EnrollmentDate DATE
);

-- Enrollments Table
CREATE TABLE Enrollments (
    EnrollmentID INT AUTO_INCREMENT PRIMARY KEY,
    CourseID INT,
    StudentID INT,
    Grade CHAR(1),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

-- CourseOfferings Table
CREATE TABLE CourseOfferings (
    OfferingID INT AUTO_INCREMENT PRIMARY KEY,
    CourseID INT,
    InstructorID INT,
    Semester VARCHAR(10),
    Year INT,
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID)
);
"""
user_input = "Get all course offerings with unique semester and output course id"


embeddings_manager = EmbeddingsManager()
if embeddings_manager.contain_embeddings():
    logger.info("Embeddings was loaded from persistant memory")
else:
    table_descriptions = generate_table_descriptions(db_context)
    embeddings_manager.add_documents(table_descriptions)


associated_table_descriptions = embeddings_manager.vector_search(user_input)

prompt = f"""
Using these table descriptions: {associated_table_descriptions}.
Generate SQL query that will do the following: "{user_input}".
Output JSON with generated SQL query.
JSON structure: {{"sql": "<generated_sql_query>"}}
"""
logger.info(f"Final prompt:\n{prompt}")
sql = llm_generate_json(prompt)["sql"]

logger.info(f"Result SQL: {sql}")
