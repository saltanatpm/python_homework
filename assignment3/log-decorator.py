import logging

# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if args:
            pos_params = list(args)
        else:
            pos_params = "none"

        if kwargs:
            kw_params = kwargs
        else:
            kw_params = "none"

        result = func(*args, **kwargs)

        logger.info("function: " + func_name)
        logger.info("positional parameters: " + str(pos_params))
        logger.info("keyword parameters: " + str(kw_params))
        logger.info("return: " + str(result))
        logger.info("-----------------------------")
        return result

    return wrapper

# 1. function with no parameters
@logger_decorator
def hello():
    print("Hello, World!")

# 2. function with variable positional arguments
@logger_decorator
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return True

# 3. function with keyword arguments only
@logger_decorator
def get_decorator(**kwargs):
    return logger_decorator

if __name__ == "__main__": 
    hello()
    add_all(1, 2, 3, 4)
    get_decorator(a=10, b=20)