class Array:
    def __init__(self):
        self.capacity = 2
        self.length = 0
        self.arr = [None] * self.capacity

    def __str__(self):
        return str(self.arr)

    def __len__(self):
        return self.length

    # 末尾への値の挿入
    def pushback(self, value):
        if self.length == self.capacity:
            self.resize()

        self.arr[self.length] = value
        self.length += 1

    def resize(self):
        # 新規配列を作成
        self.capacity *= 2
        newArr = [None] * self.capacity

        # 配列のコピー
        for i in range(self.length):
            newArr[i] = self.arr[i]
        self.arr = newArr

    # 末尾の値の削除
    def popback(self):
        if self.length > 0:
            self.length -= 1
