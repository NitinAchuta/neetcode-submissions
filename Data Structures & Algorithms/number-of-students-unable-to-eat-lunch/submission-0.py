class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = 0

        while students and sandwiches:
            currStudent = students.pop(0)
            currSandwich = sandwiches[0]

            if currStudent==currSandwich:
                count = 0
                sandwiches.pop(0)
            else:
                students.append(currStudent)
                sandwiches.append(currSandwich)
                count += 1
            
            if count == len(students):
                return count
        
        return 0 
                
        