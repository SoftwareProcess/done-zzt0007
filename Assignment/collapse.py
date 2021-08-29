def collapse(value):
    digits = len(value)
    if value.isnumeric() and digits < 51:
        while digits == 1:
            return value
        while digits > 1:
            number = 0
            for values in value:
                number += int(values)
            value = str(number)
            digits = len(str(number))
        return value
    else: 
        return None 
