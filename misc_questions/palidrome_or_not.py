def is_palidrome(substring):
    i = 0
    j = len(substring) - 1

    while i <= j:
        if substring[i] == substring[j]:
            i += 1
            j -= 1
        else:
            return False
    return True

all_substrings = []

def recursive_solution(current_substring, index, string_for_palindrome):

    if index >= len(string_for_palindrome):
        return


    all_substrings.append(current_substring)

    new_word = current_substring
    new_word += string_for_palindrome[index]
    all_substrings.append(new_word)
    recursive_solution(new_word, index + 1, string_for_palindrome)


    recursive_solution(current_substring, index + 1, string_for_palindrome)



def find_longest_substring(string_for_palindrome):
    global all_substrings
    all_substrings = []
    recursive_solution("", 0, string_for_palindrome)

    palindrome_length = []
    for sub in all_substrings:
        if is_palidrome(sub):
            palindrome_length.append(len(sub))

    palindrome_length.sort(reverse=True)
    print(palindrome_length)
    return palindrome_length[0]


if __name__ == "__main__":
    assert find_longest_substring("abdbca") == 5
    assert find_longest_substring("cddpd") == 3
