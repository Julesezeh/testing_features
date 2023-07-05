import unittest

# hinting type variable type
var1: int = 344


# hinting return value type
def rsvp(a: int, b: str) -> str:
    invite = f"Please send an invite to 0{a}"
    return invite + " " + b


IV1 = rsvp(a=9038631650, b="Hench Mafia")
print(IV1)
