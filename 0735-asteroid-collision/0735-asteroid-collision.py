import math
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0 or asteroid > 0:
                stack.append(asteroid)
            else:
                while True:
                    if len(stack) == 0:
                        stack.append(asteroid)
                        break
                    peek = stack[-1]
                    if peek < 0 or peek * asteroid > 0:
                        stack.append(asteroid)
                        break
                    
                    abs_asteroid = abs(asteroid)
                    if peek == abs_asteroid:
                        stack.pop()
                        break
                    elif peek > abs_asteroid:
                        break
                    else:
                        stack.pop()

        return stack

                        

                        

                    