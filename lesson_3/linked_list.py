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
        self.len_ = 0
        self.head = None  # Node

        if data:  # ToDo Проверить, что объект итерируемый. Метод self.is_iterable
            for value in data:
                self.append(value)

    def __str__(self):
        """Вызывается функциями str, print и format. Возвращает строковое представление объекта."""
        result = []
        current_node = self.head

        for _ in range(self.len_ - 1):
            result.append(current_node.value)
            current_node = current_node.next

        result.append(current_node.value)

        return f"{result}"

    def __repr__(self):
        """Метод должен возвращать строку, показывающую, как может быть создан экземпляр."""
        return ""

    def __len__(self):
        ...

    def __getitem__(self, item: int) -> Any:
        ...

    def __setitem__(self, key, value):
        ...

    def append(self, value: Any):
        """Добавление элемента в конец связного списка"""
        append_node = self.Node(value)
        if self.head is None:
            self.head = append_node
        else:
            tail = self.head  # ToDo Завести атрибут self.tail, который будет хранить последний узел
            for _ in range(self.len_ - 1):
                tail = tail.next
            self.__linked_nodes(tail, append_node)

        self.len_ += 1

    @staticmethod
    def __linked_nodes(left: Node, right: Optional[Node]) -> None:
        left.next = right

    def to_list(self) -> list:
        ...

    def insert(self, index: int, value: Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def index(self, value: Any) -> int:
        ...

    def remove(self, value: Any) -> None:
        ...

    def sort(self) -> None:
        ...

    def is_iterable(self, data) -> bool:
        """Метод для проверки является ли объект итерируемым"""
        ...


if __name__ == '__main__':
    ll = LinkedList([1, 2, 3, 4])
    print(ll)
