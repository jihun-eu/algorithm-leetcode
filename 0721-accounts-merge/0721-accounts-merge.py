class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountTable = {}
        for account in accounts:
            name, emails = account[0], set(account[1:])
            if name not in accountTable:
                accountTable[name] = deque([emails])
                continue

            for _ in range(len(accountTable[name])):
                userEmails = accountTable[name].popleft()
                if not userEmails & emails:
                    accountTable[name].append(userEmails)
                    continue
                emails = emails | userEmails
            accountTable[name].append(emails)

        mergedAccounts = []
        for name, usersEmails in accountTable.items():
            for userEmails in usersEmails:
                mergedAccounts.append([name] + sorted(userEmails))
        
        return mergedAccounts

