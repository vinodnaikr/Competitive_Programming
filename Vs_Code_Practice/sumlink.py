class solution:
    def addTwoNumbers(self,L1,L2):
        return list(int(str(L1)[::-1]) + int(str(L2)[::-1]))[::-1]
L1 = [2,4,3]
L2 = [5,6,4]
s = solution()
print(s.addTwoNumbers(L1,L2))