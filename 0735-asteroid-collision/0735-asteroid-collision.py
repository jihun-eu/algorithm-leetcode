class Solution:

    @staticmethod
    def is_sign_equal(top: int, asteroid: int) -> bool:
        if top < 0:
            return True

        return top * asteroid > 0

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack = []
        top = None
        for asteroid in asteroids:
            if not stack or asteroid > 0:
                stack.append(asteroid)
            else:

                abs_asteroid = abs(asteroid)

                while True:
                    if not stack:
                        stack.append(asteroid)
                        break

                    top = stack[-1]
                    if Solution.is_sign_equal(top, asteroid):
                        stack.append(asteroid)
                        break

                    if abs_asteroid == top:
                        stack.pop()
                        break
                    if abs_asteroid > top:
                        stack.pop()
                        continue
                    else:
                        break

        return stack

            