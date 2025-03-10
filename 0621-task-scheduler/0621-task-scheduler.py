class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        UNICODE_A = ord('A')
        freq = [0] * 26

        for task in tasks:
            freq[ord(task) - UNICODE_A] += 1
        
        maxFreq = max(freq)
        maxFreqCnt = freq.count(maxFreq)
        
        partCount = maxFreq - 1
        partLength = n - maxFreqCnt + 1
        emptySlots = partCount * partLength

        availableTasks = len(tasks) - maxFreq * maxFreqCnt
        idle = max(0, emptySlots - availableTasks)

        return len(tasks) + idle
