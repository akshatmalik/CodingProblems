import heapq

class FindKLargest:

    def __init__(self, arr, k):
        self.min_numbers = []
        self.arr = arr
        self.k = k

        for num in arr:
            self.add_num(num)

    def add_num(self, num):

        heapq.heappush(self.min_numbers, num)

        if len(self.min_numbers) > self.k:
            heapq.heappop(self.min_numbers)

        print(self.min_numbers)
        return self.min_numbers[0]

class MyImplementation:

    def __init_nums(self, arr, k):
        arr.sort()
        arr.reverse()
        self.min_numbers = arr[:k]
        self.min_numbers.reverse()

    def __init__(self, arr, k):
        self.min_numbers: list = []
        self.arr = arr
        self.k = k

        self.__init_nums(self.arr, k)

    def add_num(self, num: int):

        print(self.min_numbers)

        if num > self.min_numbers[0]:
            self.min_numbers.pop(0)
            # print(self.min_numbers)
            self.min_numbers.append(num)
            self.min_numbers.sort()

        return self.min_numbers[0]

from datetime import datetime

if __name__ == "__main__":

    time_1 = []
    for _ in range(100):
        start_time = datetime.now()
        largest_k_nums = FindKLargest([4, 1, 3, 12, 7, 14], 3)
        print(largest_k_nums.add_num(6))
        print(largest_k_nums.add_num(13))
        print(largest_k_nums.add_num(4))
        time_spent = datetime.now() - start_time
        time_1.append(time_spent)


    largest_k_nums = MyImplementation([4, 1, 3, 12, 7, 14], 3)
    print(largest_k_nums.add_num(6))
    print(largest_k_nums.add_num(13))
    print(largest_k_nums.add_num(4))

