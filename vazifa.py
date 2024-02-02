#1-mashq
def decorator(func):
    def wrapper(x, y):
        result = func(x, y)
        if isinstance(result, tuple) and len(result) == 2:
            return result
        else:
            print("Noto'g'ri javob :")
            return (None) 
    return wrapper

@decorator
def calculate(x, y):
    return (x * y,)

result = calculate(3, 4)
print("Natija:", result)
#2-mashq
def validate_answers(func):
    def wrapper(answer1, answer2):
        if isinstance(answer1, int) and isinstance(answer2, int):
            if answer1 * answer2 == 4:
                return func(answer1, answer2)
            else:
                raise ValueError("Noto'g'ri javob kiritdingiz")
        else:
            raise ValueError("Noto'g'ri javob, faqat butun sonlarni kiriting")
    return wrapper

@validate_answers
def perform_operation(answer1, answer2):
    return answer1 + answer2

try:
    result = perform_operation(2, 2)
    print("Natija:", result)
except ValueError as e:
    print(f"Hatolik: {e}")
#3-mashq
from datetime import datetime

def time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        print(f"Ish boshlangan vaqt: {start_time}")
        
        result = func(*args, **kwargs)
        
        end_time = datetime.now()
        print(f"Ish yakunlangan vaqt: {end_time}")
        
        return result
    return wrapper
@time
def function():
    total = 0
    for i in range(1000):
        total += i
    return total

result = function()
print("Natija:", result)
#4-mashq
from datetime import datetime

def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.now()
        
        print(f"Ish boshlangan vaqt: {start_time}")
        print(f"Ish yakunlangan vaqt: {end_time}")
        
        return result
    
    return wrapper

@log_execution_time
def example_function():
    total = 0
    for i in range(1000):
        total += i
    return total

result = example_function()
print("Natija:", result)
