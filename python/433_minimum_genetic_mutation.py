class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if endGene not in bank:
            return -1

        queue = deque([(startGene, 0)])
        seen = set([startGene])

        while queue:
            (gene, moves) = queue.popleft()
            if gene == endGene:
                return moves
            for i in range(len(gene)):
                for c in 'ACGT':
                    next_gene = gene[:i] + c + gene[i+1:]
                    if (next_gene in bank) and (next_gene not in seen):
                        seen.add(next_gene)
                        queue.append((next_gene, moves+1))

        return -1