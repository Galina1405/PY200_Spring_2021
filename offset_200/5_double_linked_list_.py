"""
Двусвязный список на основе односвязного списка.
    Самостоятельное задание. В двусвязном списке должны быть следующие методы:
    - **`__str__`**
    - **`__repr__`**
    - **`__getitem__`**
    - **`__setitem__`**
    - **`__len__`**
    - **`insert`**
    - **`index`**
    - **`remove`**
    - **`append`**
    - **`__iter__`**
    Необязательно все эти методы должны быть переопределены в явном виде. По максимуму используйте
    наследование, если поведение списков в контексте реализации указанных метод схоже.
    С точки зрения наследования по минимуму перегружайте методы. При необходимости рефакторите базовый класс,
    чтобы локализовать части кода во вспомогательные функции, которые имеют различное поведение
    в связном и двусвязном списках.
    Стремитесь к минимизации кода в дочернем классе.
    Есть какой-то метод класса DoubleLinkedList хотите отработать в явном виде ещё раз, не возбраняется.
"""

# ToDo импорт любой вашей реалиазации LinkedList
from typing import Any, Sequence, Optional


class LinkedList:
    class Node:
        """
        Внутренний класс, класса LinkedList.

        Пользователь напрямую не работает с узлами списка, узлами оперирует список.
        """
        def __init__(self, value: Any, next_: Optional['Node'] = None):
            """
            Создаем новый узел для односвязного списка

            :param value: Любое значение, которое помещено в узел
            :param next_: следующий узел, если он есть
            """
            self.value = value
            self.next = next_  # Вызывается сеттер

        @property
        def next(self):
            """Getter возвращает следующий узел связного списка"""
            return self.__next

        @next.setter
        def next(self, next_: Optional['Node']):
            """Setter проверяет и устанавливает следующий узел связного списка"""
            if not isinstance(next_, self.__class__) and next_ is not None:
                msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                      f"или None, не {next_.__class__.__name__}"
                raise TypeError(msg)
            self.__next = next_

        def __repr__(self):
            """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
            return f"Node({self.value}, {self.next})"

        def __str__(self):
            """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
            return f"{self.value}"

    def __init__(self, data: Sequence = None):
        """Конструктор связного списка"""
        self.__len = 0
        self.head = None
        self.tail = None

        if self.is_iterable(data):  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        return f"{[value for value in self]}"

    def __repr__(self):
        return f"{type(self).__name__}({[value for value in self]}"

    def __len__(self) -> int:
        return self.__len

    def __step_by_step_on_nodes(self, index) -> 'Node':
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.__len:
            raise IndexError()

        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

    def __getitem__(self, item: int) -> Any:
        print('Вызван getter')
        current_node = self.__step_by_step_on_nodes(item)
        return current_node.value

    def __setitem__(self, key: int, value: Any):

        current_node = self.__step_by_step_on_nodes(key)
        current_node.value = value

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            tail = self.head
            for _ in range(self.__len - 1):
                tail = tail.next
            print("before append: ")
            print("tail: ", tail)
            print("append node: ", append_node)
            self.__linked_nodes(tail, append_node)
            self.tail = tail.next

        self.__len += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        print('Вызван list')
        return [value for value in self]

    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()
        if index == 0:
            insert_node = self.Node(value)
            self.__linked_nodes(insert_node, self.head)
            self.head = insert_node
            self.__len += 1
        elif 1 <= index < self.__len:
            prev_node = self.__step_by_step_on_nodes(index - 1)
            next_node = prev_node.next
            current_node = self.Node(value)
            self.__linked_nodes(prev_node, current_node)
            self.__linked_nodes(current_node, next_node)
            self.__len += 1
        elif index >= self.__len:
            self.append(value)

    def clear(self) -> None:
        self.head = None
        self.__len = 0

    def index(self, value: Any) -> int:
        current_node = self.head
        for i in range(self.__len):
            if current_node.value == value:
                return i
            else:
                current_node = current_node.next


    def remove(self, value: Any) -> None:
        if self.index(value) == 0:
            self.head = self.head.next
            self.__len -= 1
        elif 1 <= self.index(value) < self.__len - 1:
            prev_node = self.__step_by_step_on_nodes(self.index(value) - 1)
            current_node = prev_node.next
            next_node = current_node.next
            self.__linked_nodes(prev_node, next_node)
            self.__len -= 1
        elif self.index(value) == self.__len - 1:
            prev_node = self.__step_by_step_on_nodes(self.index(value) - 1)
            prev_node.next = None
            self.__len -= 1

            
    def sort(self) -> None:
        current = self.head
        sorted_lst = []
        while (current != None):
            next = current.next
            sorted_lst = self.__insert_to_sorted(sorted_lst, current)
            current = next
        self.__init__(sorted_lst)


    def __insert_to_sorted(self, sorted_lst, current):
        current = current.value
        if len(sorted_lst) == 0:
            return [current]
        i = 0
        while sorted_lst[i] < current:
            i += 1
            if i == len(sorted_lst):
                sorted_lst.append(current)
                return sorted_lst

        return sorted_lst[:i] + [current] + sorted_lst[i:]


    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        if hasattr(data, "__iter__"):
            return True
        return False

class DoubleLinkedList(LinkedList):
     class DoubleLinkedNode(LinkedList.Node):
         def __init__(self, value: Any,
                      next_: Optional['Node'] = None,
                      prev: Optional['Node'] = None):
             super().__init__(value, next_)
             self._prev = prev

         @property
         def prev(self):
             """Getter возвращает предыдущий узел связного списка"""
             return self._prev

         @prev.setter
         def prev(self, prev: Optional['Node']):
             """Setter проверяет и устанавливает предыдущий узел связного списка"""
             if not isinstance(prev, self.__class__) and prev is not None:
                 msg = f"Устанавливаемое значение должно быть экземпляром класса {self.__class__.__name__} " \
                       f"или None, не {prev.__class__.__name__}"
                 raise TypeError(msg)
             self._prev = prev

         def __repr__(self):
             """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
             return f"Node({self.value}, {self.next}, {self.prev})"


     def __step_by_step_on_nodes(self, index) -> 'Node':
         return super().__step_by_step_on_nodes(index)


     @staticmethod
     def __linked_nodes(left: DoubleLinkedNode, right: Optional[DoubleLinkedNode ]) -> None:
         left.next = right
         if right is not None:
             right.prev = left


     def __init__(self, data: Sequence = None):
         super().__init__(data)
         self.__len = 4



if __name__ == '__main__':
    # ll = LinkedList([1, 2, 3, 4])
    # print(ll[1])

    # l1 = LinkedList('bdca')
    # print("before: \n", l1)
    # print(l1.index('c'))
    # l1.insert(2, 'r')
    # l1.remove('d')
    # l1.sort()
    #
    # print("after: \n", l1)
    # print("l1.head: ", l1.head)
    # print("l1.tail: ", l1.tail)


    l2 = DoubleLinkedList('bdca')
    print("before: \n", l2)
    # print(l2.index('c'))
    # l2.insert(2, 'r')
    # l2.remove('d')
    # l2.sort()

    print("after: \n", l2)
    # print("l2.head: ", l2.head)
    # print("l2.tail: ", l2.tail)

    # print(l1[0])
    # for val in l1:
    #     #     print(val)

    # print('a' in l1)
    # print(l1.to_list())
    # print(repr(l1))
    # l1.insert(2, '3')
    # print(l1)

