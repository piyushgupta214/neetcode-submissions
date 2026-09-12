class Solution:
    def countBits(self, n: int) -> List[int]:
        
        countPut = []
        output = []
        i = 0 
        while i <= n:
            output.append(i)
            i += 1
        print(output)
        for o in output:
            count = 0 
            while o > 0:
                if o & 1 == 1:
                    count += 1
                o = o >> 1
            countPut.append(count)

        return countPut
