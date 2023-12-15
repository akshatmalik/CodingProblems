from itertools import permutations

def print_balanced_braces(n):

    braces_store = []
    for _ in range(n):
        braces_store.append("(")
        braces_store.append(")")
    all_permutations = list(permutations(braces_store))

    valid_permutation_store = set()
    for perm in all_permutations:
        open_brace_count, close_brace_count = 0,0
        for val in perm:
            if val == "(":
                open_brace_count += 1
            if val == ")" and open_brace_count - 1 >= close_brace_count :
                close_brace_count += 1
        if open_brace_count == close_brace_count == 3:
            if perm not in valid_permutation_store:
                print(perm)
                valid_permutation_store.add(perm)

    # print(valid_permutation_store)

if __name__ == "__main__":

    print_balanced_braces(3)