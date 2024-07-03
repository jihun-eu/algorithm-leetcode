class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        history = []

        max_index = len(target)
        index = 0
        for num in range(1, n+1):
            if index == max_index:
                break
            if num == target[index]:
                history.append("Push")
                index += 1
            else:
                history += ["Push", "Pop"]

        return history
