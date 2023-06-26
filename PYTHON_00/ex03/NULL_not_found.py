def NULL_not_found(value):
    if value is None:
        print(f"Nothing: {value} {type(value)}")
    elif isinstance(value, float) and value != value:
        print(f"Cheese: {value} {type(value)}")
    elif value == 0:
        print(f"Zero: {value} {type(value)}")
    elif isinstance(value, str) and value == '':
        print(f"Empty: {type(value)}")
    elif isinstance(value, bool):
        print(f"Fake: {value} {type(value)}")
    else:
        print("Type not Found")
        return 1