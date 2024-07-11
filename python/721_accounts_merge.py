class UnionFind:
    def __init__(self, num_groups):
        self.groups = [[i, 1] for i in range(num_groups)]
        self.emails = dict()
    
    def add(self, email, group):
        if email in self.emails:
            group = self.union(group, self.emails[email])
        self.emails[email] = group
        
    def union(self, a, b):
        a_rep = self.find(a)
        b_rep = self.find(b)
        if self.groups[a_rep][1] > self.groups[b_rep][1]:
            self.groups[a_rep][1] += self.groups[b_rep][1]
            self.groups[b_rep][0] = a_rep
            return a_rep
        else:
            self.groups[b_rep][1] += self.groups[a_rep][1]
            self.groups[a_rep][0] = b_rep
            return b_rep

    def find(self, i):
        if self.groups[i][0] == i:
            return i
        self.groups[i][0] = self.find(self.groups[i][0])
        return self.groups[i][0]

    def get_groups(self):
        groups = defaultdict(list)
        for email in self.emails:
            i = self.find(self.emails[email])
            groups[i].append(email)
        return groups


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:  

        n = len(accounts)      
        union = UnionFind(n)

        for acc_num in range(n):
            for email_num in range(1, len(accounts[acc_num])):
                email = accounts[acc_num][email_num]
                union.add(email, acc_num)
        
        groups = union.get_groups()
        result = []
        for group in groups.keys():
            arr = [accounts[group][0]]
            arr.extend(sorted(groups[group]))
            result.append(arr)

        return result