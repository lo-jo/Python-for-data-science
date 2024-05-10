# DESCRIPTION :
# First function python
# Write a function that prints the object types and returns 42.

def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(object, "is in the kitchen :", type(object))
    elif isinstance(object, list):
        print("List :", type(object))
    elif isinstance(object, tuple):
        print("Tuple :", type(object))
    elif isinstance(object, set):
        print("Set :", type(object))
    elif isinstance(object, dict):
        print("Dict :", type(object))
    else:
        print("Type not found")
    return 42
#your code here