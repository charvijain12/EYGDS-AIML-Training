//find one student 
db.students.findOne({name: "Vikram"})

//output
{
  _id: ObjectId('68dfa867d820ec06268084b6'),
  student_id: 5,
  name: 'Vikram',
  age: 21,
  city: 'Chennai',
  course: 'ML',
  marks: 95
}
