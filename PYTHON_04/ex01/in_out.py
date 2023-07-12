def square(x: int | float) -> int | float:
    """square function"""
    return x * x

def pow(x: int | float) -> int | float:
    """pow function"""
    return x ** x

# ! In Python, the nonlocal keyword is used to indicate
# ! that a variable is not local to the current function scope
# ! but is defined in an outer (enclosing) scope.
# ! It allows you to access and modify a variable
# ! in an outer scope from within an inner function.
# ! https://cutt.ly/awi2fNAG => nonlocal keyword ok for ex
def outer(x: int | float, function) -> object:
    """outer function"""
    count = 0
    def inner() -> float:
        """inner function"""
        nonlocal x
        x = function(x)
        return x
    return inner