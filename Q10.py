celsius = input("Enter temperature in Celsius: ")
celsius = float(celsius)

fahrenheit = (celsius * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")

if celsius < 0:
    print("Very cold! Wear thick jacket")
elif 0 <= celsius <= 15:
    print("Cold. Wear jacket")
elif 16 <= celsius <= 25:
    print("Nice weather")
else:
    print("Hot! Stay hydrated")
