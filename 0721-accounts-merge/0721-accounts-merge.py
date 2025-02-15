class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjacents = {}
        for account in accounts:
            firstEmail = account[1]
            if firstEmail not in adjacents: adjacents[firstEmail] = []
            for email in account[2:]:
                adjacents[firstEmail].append(email)
                if email not in adjacents: adjacents[email] = []
                adjacents[email].append(firstEmail)
        
        visited = set()
        def mergeAccounts(mergedAccount: List[str], email: str) -> None:
            nonlocal adjacents, visited
            visited.add(email)
            mergedAccount.append(email)
            for adjacent in adjacents[email]:
                if adjacent in visited: continue
                mergeAccounts(mergedAccount, adjacent)
        
        mergedAccounts = []
        for account in accounts:
            name, firstEmail = account[0], account[1]
            if firstEmail in visited: continue
            mergedAccount = []
            mergeAccounts(mergedAccount, firstEmail)
            mergedAccounts.append([name] + sorted(mergedAccount))
        
        return mergedAccounts