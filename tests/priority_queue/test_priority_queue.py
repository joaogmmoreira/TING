from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    mock = [
        {"qtd_linhas": 7},
        {"qtd_linhas": 3},
    ]

    priority_queue = PriorityQueue()

    assert len(priority_queue) == 0

    priority_queue.enqueue(mock[0])

    assert len(priority_queue) == 1

    priority_queue.enqueue(mock[1])

    assert len(priority_queue) == 2

    assert priority_queue.search(1) == mock[0]

    assert priority_queue.dequeue() == mock[1]

    assert len(priority_queue) == 1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(90)

    assert priority_queue.dequeue() == mock[0]

    assert len(priority_queue) == 0
