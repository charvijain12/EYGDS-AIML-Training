select e.name, e.teacher_id, d.subject_name
from Teachers e
RIGHT JOIN Subjects d
ON e.subject_id = d.subject_id;