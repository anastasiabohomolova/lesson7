def main_func(func):
    def wrapper(*args, **kwargs):
        my_dict = dict()
        
        for i in args:
            if isinstance(i, int):
                my_dict['int'] = i

            else:
                my_dict['str'] = i

            for el in my_dict:
                el = my_dict
                el = tuple([el])
            print(el)
            
        func(*args, **kwargs)   
        return my_dict 
      
    return wrapper

@main_func
def my_func(a, b, c, d, f):
    print('фукція працює!')


my_func('Nastia', 23, 30000, 'IT', 'Python')
