def main():
    print(" Temperature in Fahrenheit!")
    fahrenheit =float(input("Input the Temperature in Fahrenheit: "))
    celsius =(fahrenheit -32) * 5.0 / 9.0 
    print(f"Temperature: {fahrenheit}f = {celsius}C")
if __name__ == '__main__':
    main()