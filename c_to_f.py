# this program converts celsius to fahrenheit and vice versa

def convert_temp():
    c_or_f = input("Are you trying to convert to Celsius or Fahrenheit? ")
    temp = int(input("What is the temperature that you're trying to convert? "))

    if c_or_f == "Fahrenheit":
        temp_f = round((temp * 1.8 + 32),1)
        print(f"{temp}c = {temp_f}f")

    elif c_or_f == "Celsius":
        temp_c = round(((temp - 32) / 1.8),1)
        print(f"{temp}f = {temp_c}c")

convert_temp()
