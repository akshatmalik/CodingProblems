

def word_contains_all_dict(test_word, dict_words):

    for word in dict_words:

        if word in test_word:
            test_word = test_word.replace(word, "")

    if test_word == "":
        return True
    else:
        return False


if __name__ == "__main__":
    assert word_contains_all_dict("applepenapple", ["apple", "pen"]) == True
    assert word_contains_all_dict("applepenapple1", ["apple", "pen"]) == False