import time
current_time = time.time()
print(current_time) #in seconds since 1/1/1970

#Write code here

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

#when the function runs the function decorator will be called and the inner function will run
fast_function()
slow_function()