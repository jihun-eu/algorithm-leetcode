from collections import defaultdict
class DSU:
    def __init__(self, size: int) -> None:
        self.representatives = [i for i in range(size)]

    def union(self, a: int, b: int) -> None:
        representativeA = self.find(a)
        representativeB = self.find(b)
        if representativeA == representativeB: return
        self.representatives[max(representativeA, representativeB)] = min(representativeA, representativeB)
    
    def find(self, representative: int) -> int:
        if self.representatives[representative] == representative: return representative
        return self.find(self.representatives[representative])

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        disjointSetUnion = DSU(len(accounts))
        emailGroup = {}

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailGroup:
                    disjointSetUnion.union(i, emailGroup[email])

                else:
                    emailGroup[email] = i
        
        components = defaultdict(list)
        for email, representative in emailGroup.items():
            groupRepresentative = disjointSetUnion.find(representative)
            components[groupRepresentative].append(email)

        mergedAccounts = []
        for accountIndex, emails in components.items():
            name = accounts[accountIndex][0]
            mergedAccounts.append([name]+sorted(emails))

        return mergedAccounts     