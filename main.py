import time

# --- Methods ---

# 1. Slow loop
def sum_of_squares(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

# 2. Generator expression
def sum_of_squares_fast(n):
    return sum(i * i for i in range(n))

# 3. Formula (fastest)
def sum_of_squares_formula(n):
    return (n-1) * n * (2*n - 1) // 6

# --- Timing helper ---
def time_function(func, n):
    start = time.time()
    result = func(n)
    elapsed = time.time() - start
    return elapsed, result

# --- Main test ---
n = 1_000_000

methods = [
    ("Slow loop", sum_of_squares),
    ("Generator", sum_of_squares_fast),
    ("Formula", sum_of_squares_formula)
]

print(f"{'Method':<15} {'Time (s)':<12} {'Result (first 10 digits)'}")
print("-" * 45)

for name, func in methods:
    elapsed, result = time_function(func, n)
    # Print result as first 10 digits to keep table readable
    print(f"{name:<15} {elapsed:<12.6f} {str(result)[:10]}...")
    
    
    
    # for this formulla methed this is fast enough this gives instant resuld even for million numbers calculations so this is insane
     