'''https://www.hackerrank.com/challenges/qheap1/problem -Hackerrank Question link '''




import heapq


class MinHeap:
    def __init__(self):
        self.heap = []
        self.deleted = set()

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def delete(self, value):
        self.deleted.add(value)

    def get_min(self):
        while self.heap[0] in self.deleted:
            heapq.heappop(self.heap)
        return self.heap[0]


def heap_operations(queries):
    min_heap = MinHeap()
    result = []

    for query in queries:
        query_type = query[0]

        if query_type == 1:
            element = query[1]
            min_heap.insert(element)
        elif query_type == 2:
            element = query[1]
            min_heap.delete(element)
        elif query_type == 3:
            result.append(min_heap.get_min())

    return result


if __name__ == "__main__":
    Q = int(input())
    queries = []

    for _ in range(Q):
        query = list(map(int, input().split()))
        queries.append(query)

    results = heap_operations(queries)

    for res in results:
        print(res)
