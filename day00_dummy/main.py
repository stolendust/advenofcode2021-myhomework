from pathlib import Path

###################
## part 1

with open(Path(__file__).parent/"input.txt", 'r') as file:
    lines = file.read().splitlines()
