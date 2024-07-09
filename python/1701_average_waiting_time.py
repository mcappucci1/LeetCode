class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        
        curr_time = 0
        total_wait_time = 0

        for arrive, time in customers:
            if arrive >= curr_time:
                curr_time = arrive + time
                total_wait_time += time
            else:
                curr_time += time
                total_wait_time += curr_time - arrive
        
        return total_wait_time / len(customers)