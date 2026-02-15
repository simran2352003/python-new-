#args
def average_marks(*args):
    valid_marks = [mark for mark in args if mark >= 0]
    if len(valid_marks) == 0:
        avg = sum(valid_marks)/len(valid_marks)
        return avg
    
#kwargs
def filter_details(**kwargs): 
    for key, value in kwargs.items():
     if isinstance(value,str):
            print(f"{key} = {value}")
            filter_details(name="maria",age = 21,city ="shimla")


            
    