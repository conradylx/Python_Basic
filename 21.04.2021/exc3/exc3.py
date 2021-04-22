# Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów.
# Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki,
# sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).

class Queue:
    queue_list = []

    def __init__(self, item):
        self.queue_list.append(item)

    def put(self, item):
        return self.queue_list.append(item)

    def get(self):
        if len(self.queue_list) != 0:
            return self.queue_list.pop(0)
        else:
            return 'Queue is empty'

    def show_items(self):
        return self.queue_list

    def check_if_empty(self):
        return len(self.queue_list) == 0


if __name__ == '__main__':
    object1 = Queue("B")
    print(object1.show_items())
    print(f'Is empty: {object1.check_if_empty()}')
    object1.put('A')
    object1.put('E')
    print(object1.show_items())
    object1.get()
    print(object1.show_items())
    object1.get()
    object1.get()
    print(object1.show_items())
    print(f'Is empty: {object1.check_if_empty()}')
