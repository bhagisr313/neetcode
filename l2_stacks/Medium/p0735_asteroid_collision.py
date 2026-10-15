class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        output = []
        my_stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                my_stack.append(asteroid)
            else:
                #stack being empty
                if len(my_stack) == 0:
                    output.append(asteroid)
                #stack being non-empty
                else:
                    while my_stack and abs(asteroid) > my_stack[-1]:
                        my_stack.pop()
                    if my_stack and abs(asteroid) == my_stack[-1]:
                        my_stack.pop()
                    else:
                        if not my_stack:
                            output.append(asteroid)
        return output+my_stack