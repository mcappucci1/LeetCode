class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recSolve(nums, score1, score2, turn1):
            if len(nums) == 0:
                return score1 >= score2
            if turn1:
                return (
                    recSolve(nums[1:], score1 + nums[0], score2, False) or
                    recSolve(nums[:-1], score1 + nums[-1], score2, False)
                )
            else:
                return (
                    recSolve(nums[1:], score1, score2 + nums[0], True) and
                    recSolve(nums[:-1], score1, score2 + nums[-1], True)
                )

        

        return recSolve(nums, 0, 0, True)