def calculate_discounted_price(price, is_member):
    if is_member:
        discount = 0.10 * price  # 10% discount
        discounted_price = price - discount
        return discounted_price
    else:
        return 0  # No discount for non-members

# Example usage
price = 100
is_member = True
discounted_amount = calculate_discounted_price(price, is_member)
print("Discounted Amount:", discounted_amount)


def calculate_difference(numbers):
    if len(numbers) == 0:
        return None  # Return None for an empty list

    max_num = float('-inf')  # Initialize max_num with negative infinity
    min_num = float('inf')  # Initialize min_num with positive infinity

    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num

    difference = max_num - min_num
    return difference


# Example usage
numbers_list = [5, 12, 8, 3, 20, 7]
result = calculate_difference(numbers_list)
print("Difference between max and min:", result)
