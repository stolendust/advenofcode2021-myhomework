# To shift elements easily
from collections import deque

def efficient_solution(input_text, t):
    # Create a 9-element array
    effishent_fishnet = deque([0]*9)

    # Optimize input
    for val in input_text:
        effishent_fishnet[val] += 1

    for _ in range(t):
        # Get the number of reproducing fish
        temp = effishent_fishnet[0]
        # Spin that array right round right round
        effishent_fishnet.rotate(-1)
        # Reset the reproducing fish
        effishent_fishnet[6] += temp
        
    return sum(effishent_fishnet)

days = 256
school = [3,4,3,1,2]
result = efficient_solution(school, days)
print("school after %d days is: %d" %(days, result))