import inspect

class Data():
    def __init__(self,name,**kwargs):
        self.name = name
   
    def get_name(self):
        return self.name





# def repeat(num):
#     def my_decorator(func):
#         def wrapper(*args, **kwargs):
#             for i in range(num):
#                 print('wrapper of decorator')
#                 func(*args, **kwargs)
#         return wrapper
#     return my_decorator


def repeat(status):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            if status==True:
                func(*args, **kwargs)
            else:
                print("xxxxxxx")
        return wrapper
    return my_decorator


@repeat(True)
def greet(message,name=None):
    print(message,name)

greet('hello world',name="Terry")







if __name__ == "__main__":
    
    data = Data("Terry")
    print(data.get_name())
    name = getattr(data,"name","")
    print(name)
    print(id(name))
    setattr(data,"name","Marry")
    name = getattr(data,"name","")
    print(name)
    print(id(name))
    # boolName = hasattr(data,"get_name")
    # print(boolName)
    name = getattr(data,"get_name")()
    print(name)
    print(data.get_name())
    print(inspect.getfullargspec(Data.__init__))