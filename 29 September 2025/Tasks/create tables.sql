USE schooldb;

CREATE TABLE Teachers(
	teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    subject_id INT
);

CREATE TABLE Subjects(
	subject_id INT auto_increment PRIMARY KEY,
    subject_name VARCHAR(50)
);