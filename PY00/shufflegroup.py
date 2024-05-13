import random

def create_random_groups(series, num_groups):
    # Shuffle the series to ensure randomness
    random.shuffle(series)
    
    group_size = len(series) // num_groups
    remainder = len(series) % num_groups

    groups = []
    start_index = 0

    for i in range(num_groups):
        size = group_size + (1 if i < remainder else 0)
        groups.append(series[start_index:start_index+size])
        start_index += size

    return groups

# Example usage
series = [0, 1, 2, 3]  # Example series of numbers
num_groups = 3  # Number of groups

groups = create_random_groups(series, num_groups)

for i, group in enumerate(groups, start=1):
    print(f"Group {i}:", group)

names = ["Chelito", "dani", "lolita"]
random.shuffle(names)
print(names)
