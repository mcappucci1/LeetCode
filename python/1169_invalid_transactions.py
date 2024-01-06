class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        n = len(transactions)
        invalid = []
        splits = defaultdict(list)
        for i in range(len(transactions)):
            t = transactions[i].split(',') + [i]
            t[1], t[2] = int(t[1]), int(t[2])
            splits[t[0]].append(t)

        for lst in splits.values():
            for i in range(len(lst)):
                if lst[i][2] > 1000:
                    invalid.append(transactions[lst[i][4]])
                else:
                    for j in range(len(lst)):
                        bad = (i != j) and (0 <= abs(lst[i][1] - lst[j][1]) <= 60) and (lst[i][3] != lst[j][3])
                        if bad:
                            invalid.append(transactions[lst[i][4]])
                            break

        return invalid