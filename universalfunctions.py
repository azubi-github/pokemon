'''Universal Help functions'''


def tryVar(var):
    try:
        val = var
    except NameError:
        return None
    return val
