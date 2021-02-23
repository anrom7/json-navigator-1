"""
This module helps to navigate throught the
json file.
"""

import json

def object_warning():
    """
    Informates user, that the key of needed
    piece of information is an object.
    >>> object_warning()
    The needed key is an object
    There are list of possible keys:
    """
    print('The needed key is an object')
    print('There are list of possible keys:')

def list_warning(length: int):
    """
    Informates user, that the key of needed
    piece of information is a list.
    >>> list_warning(2)
    The needed key is a list
    The length of the list is 2
    Please, choose the needed index.
    """
    print('The needed key is a list')
    print('The length of the list is', str(length))
    print('Please, choose the needed index.')

def json_into_dictionary(path: str) -> dict:
    """
    Gets the path to the json file, turns it
    into python dictionary and returns it.
    """
    json_dict = json.load(open(path, 'r', encoding='utf-8'))
    return json_dict

def json_navigator(data):
    """
    Gets the key and returns, what it is contains.
    If key is a dictionary or a list function recursively
    works again with different arguments. Returns
    key if it doesn`t contain any other objects.
    """
    if type(data) == dict:
        object_warning()
        print(list(data.keys()))
        new_key = str(input())
        json_navigator(data[new_key])
    elif type(data) == list:
        list_warning(len(data))
        new_index = int(input())
        try:
            new_key = data[new_index]
            json_navigator(new_key)
        except IndexError:
            print('Index is out of range! Try again')
            json_navigator(data)
    else:
        print(data)

def main():
    """
    Main function of the module. Gets the name
    of needed file and navigates user throught it.
    """
    print('Please, enter the file`s name')
    path = str(input())
    main_dict = json_into_dictionary(path)
    json_navigator(main_dict)
    
if __name__=="__main__":
    main()
