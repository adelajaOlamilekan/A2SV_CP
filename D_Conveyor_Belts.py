import math

def min_energy(n, x1, y1, x2, y2):
    # Calculate distance between starting and ending points
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    # Calculate steps to outermost layer
    outer_steps = min(x1, y1, n - x1 + 1, n - y1 + 1)
    
    # Calculate steps from outermost layer to ending point
    inner_steps = max(dx - outer_steps, dy - outer_steps)
    
    # Calculate total energy
    energy = outer_steps * 2 + inner_steps
    
    return energy

# Read input
t = int(input())
for _ in range(t):
    n, x1, y1, x2, y2 = map(int, input().split())
    result = min_energy(n, x1, y1, x2, y2)
    print(result)
