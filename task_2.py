import random

def get_numbers_ticket(min, max, quantity):
    if (min < 1) or (max > 1000) or (quantity < 1) or (max - min + 1 < quantity):
        return []
    
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))
    
    return sorted(numbers)

lottery_numbers = get_numbers_ticket(1,49,6)
print("Ваші лотерейні числа:",lottery_numbers)

lottery_numbers = get_numbers_ticket(1,49,60)
print("Ваші лотерейні числа:",lottery_numbers)