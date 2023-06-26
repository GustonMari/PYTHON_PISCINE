def all_thing_is_obj(arg):
    if type(arg) == int:
        print("Type not found")
        return 42
    elif type(arg) == list:
        print("List : ", type(arg))
    elif type(arg) == tuple:
        print("Tuple : ", type(arg))
    elif type(arg) == set:
        print("Set : ", type(arg))
    elif type(arg) == dict:
        print("Dict : ", type(arg))
    elif type(arg) == str:
        print(arg, " is in the kitchen!", type(arg))
    