class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x_overlap = (rec1[0] < rec2[2] and rec1[2] > rec2[0]) or (rec2[0] < rec1[2] and rec2[2] > rec1[0])
        y_overlap = (rec1[1] < rec2[3] and rec1[3] > rec2[1]) or (rec2[1] < rec1[3] and rec2[3] > rec1[1])
        
        return x_overlap and y_overlap