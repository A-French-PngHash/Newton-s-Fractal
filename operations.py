import cmath

"""
I just wasn't feeling like implementing divisions manually xD
Maybe later :p
"""

def divide(complex_1 : tuple, complex_2 : tuple) -> tuple:
    output = (complex(complex_1[0], complex_1[1]) / complex(complex_2[0], complex_2[1]))
    return (output.real, output.imag)

print(divide((3, 2), (1, -5)))