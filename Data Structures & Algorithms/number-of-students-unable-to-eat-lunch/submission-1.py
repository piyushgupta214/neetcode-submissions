class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        counters = {0: 0, 1: 0}

        for student in students:
            counters[student] = counters.get(student,0)+1

        for sandwich in sandwiches:

            if counters[sandwich] == 0:
                break
            counters[sandwich] -= 1
        
        return counters[0] + counters[1]


        