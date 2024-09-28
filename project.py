'''To-Do List Application'''
from datetime import date
from emoji import emojize 
import re
import sys
import csv


def main():
    todo_list= TodoList()
    todo_list.load()
    #todo_list.menu()


class Todo:
    def __init__(self, activity = None, term = None, complete = False) -> None:
        if activity:
            self.activity = activity
            self.term = term
            self.iscomplete = complete
        else:
            while True:
                try:
                    self.activity = input('Activity: ').strip()
                    self.term = input('Term: ').strip()
                except ValueError as e:
                    print(e)
                else:
                    break
            self.uncomplete()
    def __str__(self) -> str:
        # se estiver completo, cor em verde
        if self.iscomplete:
            inicial = f"{emojize(':heavy_check_mark:', language='alias')} \033[92m"
        # se tiver vencido, cor em vermelho
        elif (date.today() - self.term).days > 0: 
            inicial = f"{emojize(':heavy_multiplication_x:', language='alias')} \033[91m"
        # se não tiver vencido, cor em amarelo
        else:
            inicial = f"  \033[93m"
        return f"{inicial} {self.term.month}/{self.term.day}/{self.term.year} - {self.activity} \033[0m"

    def change_term(self, new_term = None):
        if new_term:
            self.term = new_term
        else:
            while True:
                try:
                    self.term = input(
                        f'Change {self.term.month}/{self.term.day}/{self.term.year} to (mm/dd/yy): '
                        ).strip()
                except ValueError:
                    pass
                else:
                    return
    def change_activity(self, new_activity = None):
        if new_activity:
            self.activity = new_activity
        else:
            try:
                self.activity = input(
                    f'Change {self.activity} to: '
                    ).strip()
            except ValueError:
                pass
            else:
                return
    def complete(self):
        self.iscomplete = True
    def uncomplete(self):
        self.iscomplete = False 

    @property
    def iscomplete(self) -> bool:
        return self._iscomplete
    @iscomplete.setter
    def iscomplete(self, c = False):
        if c:
            self._iscomplete = True
        else:
            self._iscomplete = False

    @property
    def activity(self):
        return self._activity
    @activity.setter
    def activity(self,activity):
        self._activity = activity

    @property
    def term(self):
        return self._term
    @term.setter
    def term(self, term):
        pattern = r"\b(\d{1,2})/(\d{1,2})/(\d{2,4})\b"
        if matches := re.search(pattern, term):
            m, d, y = matches.groups()
            if len(y) == 2:
                y = f'20{y}'
            
            self._term = date(year=int(y), month=int(m), day=int(d))
        else:
            raise ValueError('Wrong data set')

class TodoList:
    def __init__(self) -> None:
        self.todo_list = ''

    def add_todo(self, todo: Todo = None):
        if not todo:
            todo = Todo()
        if isinstance(todo, Todo):
            self._todo_list.append(todo)
        else:
            raise TypeError('only accept Todo types')
    
    def remove_todo(self, index):
        del self.todo_list[index]
    
    def mark_complete(self, index):
        self.todo_list[index].complete()
    
    def mark_uncomplete(self, index):
        self.todo_list[index].uncomplete()
    
    def change_term(self, index): 
        self.todo_list[index].change_term()
    def change_activity(self, index): 
        self.todo_list[index].change_activity()

    def show_list(self):
        self.todo_list.sort(key = lambda todo: todo.term)
        for i, l in enumerate(self.todo_list):
            print(f'{i}: {l}')

    def get_index(self):
        index = input('What index: ').strip()
        try: 
            index = int(index)
            if 0 <= index < len(self.todo_list):
                return index + 1
            else:
                raise ValueError
        except ValueError:
            print('\033[91m Out of range\033[0m')

    def save(self):
        with open('save.csv', 'w', newline='') as file:
            fields = ["complete", "activity", "term"]
            escritor_csv = csv.DictWriter(file, fieldnames= fields)

            escritor_csv.writeheader()

            for todo in self.todo_list:
                escritor_csv.writerow({
                    'complete' : todo.iscomplete,
                    'activity' : todo.activity,
                    'term' : todo.term
                })

    
    def load(self):
        try:
            with open('save.csv', 'r', newline='') as file:
                leitor_csv = csv.DictReader(file)
                for row in leitor_csv:
                    complete = True if row["complete"] == "True" else False
                    activity = row['activity']
                    year, month, day = row['term'].split(sep='-')
                    term = f'{month}/{day}/{year}'
                                            
                    self.todo_list.append(
                        Todo(
                            activity = activity,
                            complete = complete,
                            term = term
                            )
                    )
        except:
            pass
    def menu(self):
        if len(self.todo_list) > 0:
            self.show_list()
        while True:
            
            comandos = {
                'a': 'add todo',
                'r': 'remove todo',
                'ct': 'change todo term',
                'ca' : 'change todo activity',
                'mc' : 'mark todo complete',
                'mu' : 'mark todo uncomplete',
                'e' : 'to quit without saving',
                'es' : 'to quit saving',
                's': 'to save'
            }
            s = '||'
            for key, value in comandos.items():
                s += f' {key} - {value} ||'
            comand = input(f'{s}\n Command: ').strip()
            match comand:
                case 'a':
                    self.add_todo()
                    self.show_list()
                case 'r':
                    index = self.get_index()
                    if index:
                        self.remove_todo(index-1)
                        self.show_list()
                case 'ct':
                    index = self.get_index()
                    if index: 
                        self.change_term(index-1)
                        self.show_list()
                case 'ca':
                    index = self.get_index()
                    if index:
                        self.change_activity(index-1)
                        self.show_list()
                case 'mc': 
                    index = self.get_index()
                    if index:
                        self.mark_complete(index-1)
                        self.show_list()
                case 'mu': 
                    index = self.get_index() 
                    if index:
                        self.mark_uncomplete(index-1)
                        self.show_list()
                case 'e':
                    sys.exit()
                case 'es':
                    self.save()
                    sys.exit()
                case 's':
                    self.save()
                case _:
                    print("\033[91m Wrong command\033[0m")
                
                
    @property
    def todo_list(self):
        return self._todo_list
    @todo_list.setter
    def todo_list(self,_):
        self._todo_list = []

if __name__ == '__main__':
    main()