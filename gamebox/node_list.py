#順位を格納する線形リスト

class Node:#ノードクラス
    def __init__(self, score, name):
        self.score = score
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):#初期化
        self.head = Node(None,None)

    def insert(self, score, name):
        front = self.head
        rear = front.next
        while rear and score > rear.score:
            front = rear
            rear =rear.next

        new_node = Node(score,name)
        new_node.next = rear
        front.next = new_node
        self.delete()
    
    def show(self):#順位を表示
        tmp = self.head.next
        while tmp:
            print(f"{tmp.name} : {tmp.score}")
            tmp = tmp.next
    
    def delete(self):
        front = self.head
        rear = front.next
        count = 0
        while rear:
            count += 1
            if count > 10:
                front.next = None  # 3つ目のノードの次をNoneに設定
                break
            front = rear
            rear = rear.next
