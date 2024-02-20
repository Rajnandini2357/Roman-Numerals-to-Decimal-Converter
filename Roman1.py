def roman_to_decimal(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    roman_list = list(roman)  
    roman_list.reverse()      
    
    for char in roman_list:
        curr_value = roman_dict[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    
    return total

def main():
    roman_numeral = input("Enter a Roman numeral: ")
    decimal_equivalent = roman_to_decimal(roman_numeral)
    print("Decimal equivalent:", decimal_equivalent)

if __name__ == "__main__":
    main()

