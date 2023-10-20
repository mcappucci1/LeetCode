# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = []
        self.i = 0
        self.prepNums(nestedList)

    def prepNums(self, nestedList):
        stack = [[nestedList, 0]]
        while stack:
            [lst, i] = stack[-1]
            while i < len(lst) and lst[i].isInteger():
                self.nums.append(lst[i])
                i += 1
            if i == len(lst):
                stack.pop()
            else:
                stack.append([lst[i].getList(), 0])
                stack[-2][1] = i+1
    
    def next(self) -> int:
        val = self.nums[self.i]
        self.i += 1
        return val
    
    def hasNext(self) -> bool:
         return self.i < len(self.nums)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())