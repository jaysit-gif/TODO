import os
from todo import Todo,Do, DecodeTodo
import json

filename = 'storage.json'

def does_it_exist(file = filename)->bool: 
    if os.path.exists(file):
        return True
    else:
        return False
    

def readfromJSON():
    try:
        if does_it_exist(filename):
            with open(filename,'r') as file:
                L = json.load(file)
                DecodeTodo(L)
        else:
            with open(filename,'w') as file:
                Empty = []
                json.dump(Empty,file,indent=4)         
    except Exception as e:
        print(f'error in readfromJSON: {e}')



def writetoJSON():
    try:
        L = Todo.serialize()
        with open(filename,'w') as file:
            json.dump(L,file,indent=4)
    except Exception as e:
        print(f'error in writetoJSON {e}')
#json.dump(obj,file)
#json.load(file)

#def readfromJSON():
    #try:
 #       if does_it_exist():
 #           with open(filename,'r') as file:
 #               List = json.load(file)
 #               Todo.L = CustomEncoder.decode_list(List)
 #       else:
 #           with open(filename,'w') as file:
 #               Empty = []
  #              json.dump(Empty,file,indent=4)
 #   except Exception as e:
 #       print(f'ERROR in readfromJSON {e}')

#def writetoJSON():
   # try:
   #     List = CustomEncoder.serialize_list()
    #    with open(filename,'w') as file:
   #         json.dump(List,file,indent=4)
 #   except Exception as e:
 #       print(f'ERROR in Writetojson as {e}')"""        