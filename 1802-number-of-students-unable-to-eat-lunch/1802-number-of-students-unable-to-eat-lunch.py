class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        student_count = len(students)

        student_table = {}
        student_table[0] = students.count(0)
        student_table[1] = student_count - student_table[0]

        

        for sandwich in sandwiches:
            if student_table[sandwich] > 0:
                student_table[sandwich] -= 1
                student_count -= 1
            else:
                break
        return student_count
