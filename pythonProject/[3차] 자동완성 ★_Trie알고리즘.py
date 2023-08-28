# class Trie() 알고리즘
class Trie():
    def __init__(self):
        self.child = dict()
        self.count = 0

    def insert(self, string):
        curr = self
        for str in string:
            if str not in curr.child:
                # 처음 등록된 char 문자라면 child 딕셔너리에 0값으로 등록
                curr.child[str] = Trie()
            # curr 루트 노드부터 이어지는 문자를 간선과 노드로 연결하여 그래프를 만듬
            curr = curr.child[str]
            curr.count += 1

    def search(self, string):
        curr = self

        for index, str in enumerate(string):
            # curr 노드에서 간선이 나누어지는 부분이라면, 거기까지의 count 값을 리턴함
            if curr.child[str].count == 1:
                return index + 1
            curr = curr.child[str]

        return index + 1


def solution(words):
    answer = 0
    word_dict = Trie()

    for word in words:
        word_dict.insert(word)
    for word in words:
        answer += word_dict.search(word)

    return answer