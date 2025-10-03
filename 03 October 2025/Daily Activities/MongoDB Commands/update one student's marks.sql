//update one student's marks
db.students.updateOne(
  { name: "Neha"},
  {$set: {marks:92,course: "Advanced AI"}}
)

//output 
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
