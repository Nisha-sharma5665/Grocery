from .models import *

def GetOptionValueFromID(input_value):
    for choice in TYPE_CHOICES:
        if choice[0] == input_value:
            return choice[1]
    return None  # Return None if no match is found