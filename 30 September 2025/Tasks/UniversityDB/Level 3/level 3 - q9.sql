DELIMITER $$
CREATE PROCEDURE AvgGradePerCourse()
BEGIN
	SELECT c.course_name
		AVG( 
			CASE 
				when e.grade = 'A' then 4
                when e.grade ='B' then 3
                when e.grade ='C' then 2
                when e.grade ='D' then 1
                else 0
			END) as avggrade
    FROM courses c
    JOIN enrollments e ON c.course_id=e.course_id
    GROUP BY c.course_name;
END$$
DELIMITER ;
CALL AvgGradePerCourse();