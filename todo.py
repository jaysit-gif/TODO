class Priority:
    dictionary = {'no':'\033[97m','high':'\033[94m','medium':'\033[93m','low':'\033[92m'}

class Do :
    
    def __init__(self,task:str = 'NO TASK',status = False,priority:str = 'no'):
        try:
            self.task = task
            self.status:bool = status
            self.priority = priority
        except Exception as e:
            print(f'ERROR in constructor {e}')          

    def __str__(self):
        try:
            return f'{Priority.dictionary[self.priority]}{self.task}\033[0m'
        except KeyError as e:
            print(e)
    
    def __repr__(self):
        return self.task
    
    def encode(self)->dict:
        Dictionary:dict = {'task':self.task,'status':self.status,'priority':self.priority}
        return Dictionary
    
    def task_done(self):
        self.status = True
    

class Todo:
    List:list[Do] = []
    @classmethod
    def add(cls):
      try:  
        while True:
            s = input('ADD TASK(input \'exit\' to exit): ')           
            if s == 'exit':
                break
            p = input('Priority Order(no/low/medium/high): ').lower()
            d = Do(task = s,priority=p)
            Todo.List.append(d)
        return Todo.List
      except (TypeError, AttributeError, KeyError) as e:
          print(f'processing failed: {e}')
          return "ERROR OCCURED\n"
      except Exception as e:
          print(f'unexcepted error: {e}')    
          return "UNKNOWN ERROR\n"
            

    @classmethod
    def show(cls):
        if len(Todo.List) == 0:
            print("EMPTY\nPLEASE FILL IN SOME TASKS :)!")
        i = 1
        for obj in Todo.List:
            if obj.status:
                print(f'\033[41m{i}. {obj} \033[0m')
            else:    
                print(f'{i}. {obj}')
            i+=1    
        return 'DONE PRINTING\n'        

    @classmethod
    def delete_task(cls):
        try:
            Todo.show()
            k = int(input('index of task you want to delete: '))
            Todo.List.pop(k-1)
            return Todo.List
        except IndexError as e:
            print(f'\033[91m \033[1m \033[4m{e}\033[0m') 


    @classmethod
    def insert_task(cls):
        try:
            Todo.show()
            indice = int(input('index: '))
            s = input('Task: ')
            p = input('priority(no/low/high/medium): ').lower()
            d = Do(task=s)
            Todo.List.insert(indice,d)
            return Todo.List
        except IndexError as e:
            print(f'\033[91m \033[1m \033[4m{e}\033[0m')

    @classmethod
    def mark_done(cls):
        try:
            Todo.show()
            i = int(input('index of task you want to mark done: '))
            Todo.List[i-1].task_done()
            return Todo.List
        except  IndexError as e:
            print(f'\033[91m \033[1m \033[4m{e}\033[0m') 

    @classmethod
    def serialize(cls):
        L:list[dict] = []
        for obj in Todo.List:
            L.append(obj.encode())
        return L  

    @classmethod
    def kill_all(cls):
        while len(Todo.List) != 0:
            Todo.List.pop()
        return Todo.List
    
    @classmethod
    def edit(cls):
        try:
            Todo.show()
            index = int(input('Index: '))
            task_name = input('Task:  ')
            prior = input('Priority: ')
            prev = Todo.List[index-1]
            Todo.List[index-1] = Do(task=task_name,priority=prior)
            print(f'Changed {prev} to {Todo.List[index-1]}')
            return Todo.List
        except IndexError as e:
            print(f'\033[91m \033[1m \033[4m{e}\033[0m')

def DecodeTodo(List:list[dict]):
    try:
        for objs in List:
            Todo.List.append(Do(task=objs['task'],status=objs['status'],priority=objs['priority']))
        return Todo.List
    except KeyError as e:
        print(f'\033[91m \033[1m \033[4m{e}\033[0m')
    except Exception as e:
        print(f'\033[91m \033[1m \033[4m{e}\033[0m') 

