from queue import Queue


def hot_potato(names, num):
    q = Queue()
    for name in names:
        q.enqueue(name)
    print(q.items)
    while q.size() > 1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print(q.items)
        q.dequeue()
    return q.dequeue()


if __name__ == "__main__":
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7))
