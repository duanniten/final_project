from project import Todo, TodoList
import pytest
from datetime import date


def test_todo_change_term():
    test_todo = Todo(
        activity= 'test activity',
        term= '04/01/2025',
        complete= False
    )
    test_todo.change_term('04/02/2025')
    assert test_todo.term == date(
        year = 2025,
        month = 4,
        day = 2
    )

def test_todo_change_activty():
    test_todo = Todo(
        activity= 'test activity',
        term= '04/01/2025',
        complete= False
    )
    test_todo.change_activity('changed teste activity')
    assert test_todo.activity == 'changed teste activity'

def test_todo_change_complete():
    test_todo = Todo(
        activity= 'test activity',
        term= '04/01/2025',
        complete= False
    )
    test_todo.complete()
    assert test_todo.iscomplete == True
    test_todo.uncomplete()
    assert test_todo.iscomplete == False

def test_todo_wrong_term():
    with pytest.raises(ValueError):
        _ = Todo(
            activity= 'test activity',
            term= '04/012025',
            complete= False
        )

    test_todo = Todo(
        activity= 'test activity',
        term= '04/01/2025',
        complete= False
    )
    #monnth 13
    with pytest.raises(ValueError):
        test_todo.change_term('13/02/2025')
    # more days in a month
    with pytest.raises(ValueError):
        test_todo.change_term('02/30/2025')

def test_todo_list():
    todo_list = TodoList()
    todo_list.add_todo(
        Todo(
        activity= 'test activity',
        term= '04/01/2025',
        complete= False
            )
        )
    todo_list.add_todo(
        Todo(
        activity= 'test activity2',
        term= '04/01/2025',
        complete= False
            )
        )
    assert len(todo_list.todo_list) == 2
    assert isinstance(todo_list.todo_list[0], Todo)
    