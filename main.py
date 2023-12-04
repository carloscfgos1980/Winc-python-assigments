# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

'''
I had to creat a if else coz if I parameter just like:
"what'z up"
it it wont replace the name. To be fair. In the exercise the parameter is just like that:
greet('Bob', "What's up, <name>!")
But this way is event cooler..hahaha
'''


def greet(name='Doc', greeting="Hello, <name>!"):
    message = ''
    if greeting == "Hello, <name>!":
        message = greeting.replace("<name>", name)
        return message
    else:
        message = f'{greeting}, {name}!'
        return message


print(greet('Bob', "what'z up"))


def force(mass=1, body='earth'):
    gravity = {
        'earth': 9.8,
        'sun': 274.1,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturne': 10.4,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    force = gravity[body] * mass
    return f'The force of {body} is {force}'


print(force())


def pull(m1, m2, d):
    G = (6.674) * (10 ** -10)
    pull = G * (((m1) * m2)/d**2)

    return pull


print(pull(800, 1500, 3))
