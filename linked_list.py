class LinkedList:
    
    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head:Item = None
    
    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return
        
        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item
    
    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        a = self.current.value
        self.current = self.current.next
        return a
    
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head is None:
            raise ValueError("Невозможно удалить из пустого списка")
        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Невозможно удалить из пустого списка")
        if self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def remove_at(self, index):
        if index < 0 or index >= len(self):
            raise ValueError("Индекс вне диапазона")
        if index == 0:
            self.remove_first()
            return
        current = self.head
        for i in range(index - 1):
            current = current.next
        current.next = current.next.next

    def remove_first_value(self, value):
        current = self.head
        b = None
        while current:
            if current.value == value:
                if b:
                    b.next = current.next
                else:
                    self.head = current.next
                return
            b = current
            current = current.next
        raise ValueError("Значение не найдено в списке")

    def remove_last_value(self, value):
        current = self.head
        t = None
        if self.head is None:
            raise ValueError('Список пуст')
        elif self.head is not None and self.head.next is None:
            if self.head.value == value:
                self.head = None
                return
            else:
                raise ValueError('')
        
        while current:
            if current.next and current.next.value == value:
                t = current
            current = current.next
        
        if t != None:
            t.next = t.next.next
        else:
            raise ValueError("Значение не найдено в списке")


    