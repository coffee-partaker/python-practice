def get_decimal_input():
    try:
        decimal_string = input("Type in a decimal: ")
        decimal_number = int(decimal_string.replace('-', ''))
        return decimal_number
    except ValueError:
        print("Error: invalid input. Please enter a valid decimal number.")
        return None

def decimal_to_binary(decimal_number):
    binary_list = []
    while decimal_number != 0:
        binary_list.append(decimal_number % 2)
        decimal_number //= 2
    binary_list.reverse()
    return binary_list

def main():
    decimal_number = get_decimal_input()
    if decimal_number is not None:
        sign_bit = 1 if decimal_number < 0 else 0
        binary_representation = decimal_to_binary(abs(decimal_number))
        print("The first bit represents the sign (0 for positive, 1 for negative):")
        print([sign_bit] + binary_representation)

if __name__ == "__main__":
    print("Welcome to Decimal-Binary Translator!")
    main()
