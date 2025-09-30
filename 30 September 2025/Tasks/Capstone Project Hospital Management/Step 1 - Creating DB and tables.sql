CREATE DATABASE HospitalMgmt;
USE HospitalMgmt;
--  Patients Table
CREATE TABLE Patients (
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),
city VARCHAR(50)
);
-- Doctors Table
CREATE TABLE Doctors (
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT
);
-- Appointments Table
CREATE TABLE Appointments (
appointment_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
status_s VARCHAR(20),
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
);
-- MedicalRecords Table
CREATE TABLE MedicalRecords (
record_id INT PRIMARY KEY,
patient_id INT,
doctor_id INT,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
diagnosis VARCHAR(100),
treatment VARCHAR(100),
date DATE
);
-- Billing Table
CREATE TABLE Billing (
bill_id INT PRIMARY KEY,
patient_id INT,
FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20)
);





-- Insert Students
INSERT INTO Students VALUES
(1, 'Rahul', 'Mumbai'),
(2, 'Priya', 'Delhi'),
(3, 'Arjun', 'Bengaluru'),
(4, 'Neha', 'Hyderabad'),
(5, 'Vikram', 'Chennai');
-- Insert Courses
INSERT INTO Courses VALUES
(101, 'Mathematics', 4),
(102, 'Computer Science', 3),
(103, 'Economics', 2),
(104, 'History', 3);
-- Insert Enrollments
INSERT INTO Enrollments VALUES
(1, 1, 101, 'A'),
(2, 1, 102, 'B'),
(3, 2, 103, 'A'),
(4, 3, 101, 'C'),
(5, 4, 102, 'B'),
(6, 5, 104, 'A');