def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(object, "is in the kitchen : <class 'str'>")
    elif isinstance(object, list):
        print("List : <class 'list'>")
    elif isinstance(object, tuple):
        print("Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print("That is a set")
    elif isinstance(object, dict):
        print("That is a dict")
    else:
        print("Type not found")
    return 42
#your code here