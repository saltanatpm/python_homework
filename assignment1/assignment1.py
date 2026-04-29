# Write your code here.
# 1
def hello():
    return "Hello!"

# 2
def greet(name):
    return f"Hello, {name}!"

# 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "multiply":
            return a * b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b
        else:
            raise TypeError("Unsupported operation")
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

#  4
def data_type_conversion(value, data_type):
    try:
        if data_type == "float":
            return float(value)
        elif data_type == "int":
            return int(value)
        elif data_type == "str":
            return str(value)
    except:
        return f"You can't convert {value} into a {data_type}."

# 5
def grade(*args):
    try:
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except:
        return "Invalid data was provided."

# 6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

# 7
def student_scores(option, **kwargs):
    if option == "best":
        return max(kwargs, key=kwargs.get)
    elif option == "mean":
        return sum(kwargs.values()) / len(kwargs)

# 8
def titleize(text):
    small_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word in small_words:
            result.append(word)
        else:
            result.append(word.capitalize())
    return " ".join(result)

# 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# 10
def pig_latin(text):
    vowels = "aeiou"
    words = text.split()
    result = []
    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word):
                # if we hit "qu", skip both letters together
                if word[i:i+2] == "qu":
                    i += 2
                    continue
                if word[i] in vowels:
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)