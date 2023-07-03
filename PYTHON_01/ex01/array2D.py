import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list and return it"""
    np_family = np.array(family)
    print("My shape is :", np_family.shape)
    
    np_new_family = np_family[start:end]
    print("My new shape is :", np_new_family.shape)
    return np_new_family.tolist()