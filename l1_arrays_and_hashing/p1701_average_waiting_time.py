class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        cumulative_wait_time, wait_time = 0, 0
        prev_arrival, prev_time = 0,0
        for arrival, time in customers:
            wait_time += max((prev_arrival + prev_time) - arrival, 0)
            cumulative_wait_time += wait_time + time
            prev_arrival, prev_time = arrival, time
        return cumulative_wait_time/len(customers)