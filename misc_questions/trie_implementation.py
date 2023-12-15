class TrieNode:

    def __init__(self, char):
        self.char = char
        self.children = {}
        self.end_word = False


class TrieTraversal:

    def __init__(self):
        self.root = TrieNode("")

    def insert_word(self, word):

        tree_pointer = self.root

        for char in word:
            node = TrieNode(char)
            tree_pointer.children[char] = node
            tree_pointer = node

        tree_pointer.end_word = True

    def __find_words_from_node(self, node_start, prefix):

        word_prefix = prefix
        for children in node_start.children.values():
            word_prefix += children.char
            if children.end_word == True:
                self.output.append(word_prefix)
            self.__find_words_from_node(children, word_prefix)

    def search(self, word_root):

        self.output = []

        prefix_word_root = self.root

        word_store_prefix = ""
        for char in word_root:
            word_store_prefix += char
            prefix_word_root = prefix_word_root.children[char]

            self.__find_words_from_node(prefix_word_root, word_store_prefix)

        return self.output


if __name__ == "__main__":
    tt = TrieTraversal()
    tt.insert_word("what")
    tt.insert_word("where")
    print(tt.search("wh"))
