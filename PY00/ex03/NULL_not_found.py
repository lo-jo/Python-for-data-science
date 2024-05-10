# DESCRIPTION :
# NULL not found
# Write a function that prints the object type of all types of "Null".
# Return 0 if it goes well and 1 in case of error.
# Your function needs to print all types of NULL.

def NULL_not_found(object: any) -> int:

    # print("OBJECT TYPE", locals(), type(object))

    if locals()['object'] == None:
        print("Nothing :", locals()['object'], type(object))
    elif isinstance(object, float):
        convert = str(locals()['object'])
        if (convert == 'nan'):
            print("Cheese :", locals()['object'], type(object))
    elif (locals()['object']) == False and isinstance(object, bool):
        print("Fake :", locals()['object'], type(object))
    elif isinstance(object, str) and object == '':
        print("Empty :", type(object))
    elif (locals()['object']) == 0 and isinstance(object, int):
        print("Zero :", locals()['object'], type(object))
    else:
        print("Type not found")
        return 1
    return 0
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$