
class Do :
    def __init__(self,task:str = 'NO TASK',status = False):
        try:
            self.task = task
            self.status:bool = status
        except Exception as e:
            print(f'ERROR in constructor {e}')          

    def __str__(self):
        return self.task 
    
    def __repr__(self):
        return self.task
    
    def encode(self)->dict:
        Dictionary:dict = {'task':self.task,'status':self.status}
        return Dictionary
    
    def task_done(self):
        self.status = True
    
def DecodeDO(Dictionary:dict) -> Do:
    try:
        Do(task = Dictionary['task'],status=Dictionary['status'])
    except KeyError:
        print("KEY ERROR IN THE \'DecodeDo\' function")

class Todo:
    List:list[Do] = []
    @classmethod
    def add(cls):
      try:  
        while True:
            s = input('ADD TASK(input \'exit\' to exit): ')
            if s == 'exit':
                break
            d = Do(task = s)
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
                print(f'\033[95m{i}. {obj} \033[0m')
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

def DecodeTodo(List:list[dict]):
    try:
        for objs in List:
            Todo.List.append(Do(task=objs['task'],status=objs['status']))
        return Todo.List
    except KeyError as e:
        print(f'\033[91m \033[1m \033[4m{e}\033[0m')
    except Exception as e:
        print(f'\033[91m \033[1m \033[4m{e}\033[0m') 

