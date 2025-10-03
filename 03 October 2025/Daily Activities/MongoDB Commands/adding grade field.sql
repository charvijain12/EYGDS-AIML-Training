//update multiple students in AI course - adding grade field
db.students.updateMany(
  {course:"AI"},
  {$set: {grade:"A"}}
)

output
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 0,
  modifiedCount: 0,
  upsertedCount: 0
}
