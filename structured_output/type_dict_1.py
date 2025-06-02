from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int

new_person : Person = {'name':'kashish', "age":33}

print (new_person)

