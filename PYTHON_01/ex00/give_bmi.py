import numpy as np

# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# This behavior is called locality of reference in computer science.
# This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
#? numpy is mainly coded in C and C++ which are faster than python


#The BMI calculation divides an adult's weight in kilograms (kg) by their height in metres (m) squared. 
def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """Return the BMI of each person in the list."""
    result: list[int | float] = []
    
    assert len(height) == len(weight),"The two lists doesnt have the same size"
    try:
        for i in range(len(height)):
            result.append(weight[i] / (height[i] ** 2))
    except AssertionError as msg:
        print(msg)
    return result

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Return True if the BMI is above the limit, False otherwise."""
    result: list[int | float] = []
    
    assert limit >= 0,"Impossible to have a negative BMI"
    try:
        for i in range(len(bmi)):
            if bmi[i] > limit:
                result.append(True)
            else:
                result.append(False)
    except AssertionError as msg:
        print(msg)
    return result
    
