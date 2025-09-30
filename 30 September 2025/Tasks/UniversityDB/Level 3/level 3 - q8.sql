DELIMITER $$
CREATE PROCEDURE CoursesByStudents(IN student INT)
BEGIN
	SELECT c.course_name, e.grade
    FROM courses c
    JOIN enrollments e ON c.course_id=e.course_id
    WHERE e.student_id = student;
    
END$$
DELIMITER ;
CALL CoursesByStudents(3);