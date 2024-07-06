class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        index = 0
        student_size = len(students)
        tmp = 0

        while True:
            if tmp == student_size:
                break
            if sandwiches and students[index] == sandwiches[0]:
                sandwiches.pop(0)
                students[index] = -1
                tmp = 0
            index = (index + 1) % student_size
            tmp += 1

        not_eaten_students = student_size - students.count(-1)

        return not_eaten_students
                