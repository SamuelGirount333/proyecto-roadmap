### lambdas ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(6,12))
print(type(sum_two_values))

multiply_value = lambda first_value, second_value: first_value * second_value
print(multiply_value(100,3))
print(type(multiply_value))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))