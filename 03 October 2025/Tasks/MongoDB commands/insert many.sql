//create a collection called teachers

db.teachers.insertMany([
  { id: 1, name: "Dr. P Mehta", subject: "Physics", experience: 12,city:"Delhi"},
  { id: 2, name: "Prof. K Iyer", subject: "Mathematics", experience: 8,city:"Chennai"},
  { id: 3, name: "Mrs. N Kapoor", subject: "Computer Science", experience: 10,city:"Hyderabad"},
  { id: 4, name: "Mr. SP Singh", subject: "Chemistry", experience: 6,city:"Bangalore"}
])

//output
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68e33dcc3a63827502152c57'),
    '1': ObjectId('68e33dcc3a63827502152c58'),
    '2': ObjectId('68e33dcc3a63827502152c59'),
    '3': ObjectId('68e33dcc3a63827502152c5a')
  }
}
