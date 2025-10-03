//delete all students with marks <80
db.students.deleteMany({marks:{$lt: 80 }})

output
{
  acknowledged: true,
  deletedCount: 0
}
