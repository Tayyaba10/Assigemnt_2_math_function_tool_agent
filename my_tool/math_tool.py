from agents import function_tool


@function_tool
def add(a:int, b:int):
    """
    simple add function that return the sum of two number
    
    Args:
    a:int
    b:int
    
    """
    print("add tool")
    return f"Your answer is {a + b}"
