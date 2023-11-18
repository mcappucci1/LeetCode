class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        access_times.sort(key=lambda entry: entry[1])
        stacks = defaultdict(list)
        high_access = set()
        for employee, time in access_times:
            if employee not in high_access:
                stack = stacks[employee]
                stack.append(int(time))
                if len(stack) >= 3 and (stack[-1] - stack[-3]) < 100:
                    high_access.add(employee)
        return list(high_access)