from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"

# First Part


def unique_koala_facts(nr):
    my_list = []
    i = len(list)
    while i > 0:
        if (i == nr):
            break
        i -= 1
        my_list.append(list[i])
    return my_list

# Second Part


def num_joey_facts():
    count = ''
    if 'joey' in list:
        i = len(list)
        while i > 0:
            i -= 1
            count += i
            print(count)


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    list = [random_koala_fact()]
    print('lets see:', random_koala_fact())

print('Funny characteristics:', list)

print('unique koala facts\n', unique_koala_facts(2))

print('count:\n', num_joey_facts())
