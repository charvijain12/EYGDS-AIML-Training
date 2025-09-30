select e.name, e.teacher_id, d.subject_name 
from Teachers e
INNER JOIN Subjects d 
ON e.subject_id = d.subject_id