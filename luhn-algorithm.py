def luhn_algorithm(card_number):
    digits = [int(d) for d in card_number]
    check_digit = digits.pop()
    
    # Double every second digit from right to left
    for i in range(len(digits) - 1, -1, -2):
        digits[i] *= 2
        if digits[i] > 9:
            digits[i] -= 9
    
    # Calculate the sum of all digits
    total = sum(digits) + check_digit
    
    # The number is valid if the sum is divisible by 10
    return total % 10 == 0

def test_luhn_algorithm():
    # Valid numbers
    assert luhn_algorithm("79927398713") == True
    assert luhn_algorithm("4532015112830366") == True
    assert luhn_algorithm("6011514433546201") == True
    
    # Invalid numbers
    assert luhn_algorithm("79927398714") == False
    assert luhn_algorithm("4532015112830367") == False
    assert luhn_algorithm("6011514433546202") == False
    
    # Edge cases
    assert luhn_algorithm("0") == True  # Single digit, always valid
    assert luhn_algorithm("00") == True  # Two zeros, always valid
    
    print("All tests pass")

test_luhn_algorithm()