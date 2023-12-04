# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

# Greet function


def greet(name):
    return (f'Hello {name}')


print(greet('Bob'))


# Add function
def add(x, y, z):
    outcome = x + y + z
    return outcome


print(add(5, 2, 3))

# Positive Function. Return a boolean


def positive(nr):
    if nr > 0:
        return True
    else:
        return False


print(positive(50), positive(-50), positive(0))


# Negative Function. Return a boolean

def negative(nr):
    if nr < 0:
        return True
    else:
        return False


print(negative(50), negative(-50), negative(0))
