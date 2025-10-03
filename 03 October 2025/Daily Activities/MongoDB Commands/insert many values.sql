// insert values
db.students.insertMany([
  { student_id: 2, name: "Priya", age:22, city:"Delhi", course:"ML", marks:90},
  { student_id: 3, name: "Arjun", age:20, city:"Bengaluru", course:"Data Science", marks:78},
  { student_id: 4, name: "Neha", age:23, city:"Hyderabad", course:"AI", marks:88},
  { student_id: 5, name: "Vikram", age:21, city:"Chennai", course:"ML", marks:95}
])
  
//output 
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa867d820ec06268084b3'),
    '1': ObjectId('68dfa867d820ec06268084b4'),
    '2': ObjectId('68dfa867d820ec06268084b5'),
    '3': ObjectId('68dfa867d820ec06268084b6')
  }
}
