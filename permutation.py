import itertools
my_list = [1, 2, 3]
permutations = itertools.permutations(my_list)

# Convert to a list of tuples
permuted_list = list(permutations)

print("All permutations of [1, 2, 3]:", permuted_list)
