How i did :
# All the login in main.py

1. For loop over the dictionary
2. Check if the value is a dictionary
2.1 If I want to have the separated values in "list" I just had to apply the value method the the value and append the result to the new_list:
c = list(value.values())
            new_list.append(c)
outcome: [[42, 350], 3.14]
2.2 I do a second lopping in order to catch every value and put it inside a list. 
            for k, v in value.items():
                new_list.append(v)
outcome: [42, 350, 3.14]
3. Double condiction in order to create an elif to catch the list with dictionary inside
elif type(value) == list and type(value[0]) == dict:
3.1 Loop over de dictionary inside the list, the list is the value of the parent dictionary (book) and append the value to new_
list:
            for k, v in value[0].items():
                new_list.append(v)

4. The last "else" catch the values of the dictionary that are not list of dictionary, the simple values (not nested)