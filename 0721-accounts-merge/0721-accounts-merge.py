class Solution:

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adjacents = {}
        visited = set()
        for account in accounts:
            firstAccount = account[1]
            if firstAccount not in adjacents:
                adjacents[firstAccount] = []
            
            if len(account) < 3: continue
            
            for otherAccount in account[2:]:
                adjacents[firstAccount].append(otherAccount)
                if otherAccount not in adjacents:
                    adjacents[otherAccount] = []
                adjacents[otherAccount].append(firstAccount)
        
        def mergeAccount(mergedAccounts: List[str], email: str) -> None:
            nonlocal adjacents, visited
            visited.add(email)
            mergedAccounts.append(email)       
            for adjacent in adjacents[email]:
                if adjacent in visited: continue
                mergeAccount(mergedAccounts, adjacent)

        mergedAccounts = []
        for account in accounts:
            name, firstEmail = account[0], account[1]
            if firstEmail not in visited:
                mergedAccount = []
                mergeAccount(mergedAccount, firstEmail)
                mergedAccounts.append([name]+sorted(mergedAccount))
        
        return mergedAccounts
        
        
