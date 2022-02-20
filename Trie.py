class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def create_trie(self, keys):
        for key in keys:
            self.insert(key)

    def insert(self, key):
        node = self.root

        for a in key:
            if not node.children.get(a):
                node.children[a] = TrieNode()

            node = node.children[a]

        node.last = True

    def suggestions_list_01(self, node, word):
        if node.last:
            print(word)

        for a, n in node.children.items():
            self.suggestionsRec(n, word + a)

    def suggestion_list_02(self, node, word):
        stack_node = [node]
        stack_word = [word]
        result = []
        while stack_node:
            _node = stack_node.pop()
            _word = stack_word.pop()
            if _node.last:
                print(_word)
                result.append(_word)
            for a, n in dict(reversed((_node.children.items()))).items():
                stack_node.append(n)
                stack_word.append(_word + a)
        return result

    def auto_suggestions(self, key):
        node = self.root

        for a in key:
            if not node.children.get(a):
                return []
            node = node.children[a]

        if not node.children:
            return []

        return self.suggestion_list_02(node, key)


