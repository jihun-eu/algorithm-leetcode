class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
                continue
            
            while stack and -asteroid > stack[-1] and asteroid * stack[-1] < 0:
                stack.pop()
            
            if not stack or stack[-1] < 0:
                stack.append(asteroid)

            elif -asteroid == stack[-1]:
                stack.pop()

        return stack

            