# Todo: Code is a bit unclear

def fahrenheit_to_celsius(fahr):

    """
    Given temp in fahrebheit, converts it to celsius

    :parm fahr: Temperature in Fahrenheit
    :return: The temperature in Celsius
    """
    
    celsius = (fahr - 32) * (5 / 9)
    return celsius



def fahrenheit_to_kelvin(fahr):
    """
    Given temp in fahrebheit, converts it to Kelvin

    :parm fahr: Temperature in Fahrenheit
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Kelvin
    """
    
    celsius = fahrenheit_to_celsius(fahr)
    if celsius < -273.15:
        # If temperature is les than absolute zero
        raise ValueError(
            f'Trying to convert impossible temperature: {fahr}F'
        )
    kelvin = celsius + 273.15
    return kelvin
