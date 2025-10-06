//updateone
db.teachers.updateOne(
  {name:"Mr. SP Singh"},
  {$set :{city:"Jaipur"}}
);

//output
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
