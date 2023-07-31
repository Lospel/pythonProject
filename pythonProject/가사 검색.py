class Node(object):
    def __init__(self, key):
        self.key = key
        self.count = 0
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(self)

    def insert(self, string):
        current = self.head

        for char in string:
            current.count += 1
            if char not in current.children:
                current.children[char] = Node(char)
            current = current.children[char]

    def starts_with(self, prefix):
        current = self.head

        for char in prefix:
            if char == '?' : break
            if char in current.children: current = current.children[char]
            else: return 0

        return current.count

def solution(words, queries):
    answer = []
    tries = {}
    reverse_tires = {}

    for word in words:
        size = len(word) # 0 1 2 3 ...
        if size not in tries:
            tries[size] = Trie()
            reverse_tires[size] = Trie()

        tries[size].insert(word)
        reverse_tires[size].insert(word[::-1])

    for query in queries:
        if len(query) in tries: # word 길이와 동일한 query 길이값
            if query[0] != '?': # 정방향
                trie = tries[len(query)]
                answer.append(trie.starts_with(query))
            else:
                trie = reverse_tires[len(query)]
                answer.append(trie.starts_with(query[::-1]))
        else: answer.append(0)

    return answer