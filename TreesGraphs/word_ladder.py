from collections import defaultdict, deque


def minMutation(start, end, bank):
    def build_wildcard_lookup(bank):
        table = defaultdict(list)
        for gene in bank:
            for i in range(len(gene)):
                wildcard_gene = gene[:i] + '_' + gene[i+1:]
                table[wildcard_gene].append(gene)
        return table

    gene_lookup = build_wildcard_lookup(bank)
    queue = deque()
    queue.append([start, 0])
    visited = set()
    visited.add(start)
    while queue:
        gene, count = queue.popleft()
        for i in range(len(gene)):
            wildcard_gene = gene[:i] + '_' + gene[i+1:]
            if wildcard_gene in gene_lookup:
                for next_gene in gene_lookup[wildcard_gene]:
                    if next_gene not in visited:
                        if next_gene == end:
                            return count + 1
                        queue.append([next_gene, count + 1])
                        visited.add(next_gene)
    return -1
