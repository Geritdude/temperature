def area(base, height): #header
    '''(number, number) -> number #Type Contract

    Return the area of a triangle with dimensions base and height. #Description

    >>> area (10, 5)  #Examples
    25.0
    >>> area(2.5, 3)
    3.75
    '''

    return base * height / 2  #Body

#Recipes for Designing functions:
# 1. Examples: What should your function do?
#Type a couple of example calls
#Pick a name (often a verb or verb phrase)
#What is a short answer to "What does your function do?"

#2. Type Contract: What are the parameter types?
#What type of value is returned?

#3. Header: Pick meaningful parameter names

#4. Description:
#Mention every parameter in your description.
#Describe the return value.

#5. Body

#6. Test
#Run the Examples

def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees

    >>> convert_to_celsius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) * 5 / 9


