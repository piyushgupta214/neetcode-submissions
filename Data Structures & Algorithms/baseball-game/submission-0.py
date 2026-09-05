class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        record:List[int] = []

        for operation in operations: 
            if operation == '+':
                record.append(record[-1] + record[-2])
            elif operation == 'D':
                a = record[-1]
                record.append(2*a)
            elif operation == 'C':   
                record.pop()
            else:
                record.append(int(operation))   

        sum = 0 
        for r in record:
            sum = sum +r

        return sum    
        