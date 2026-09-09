from capitalize.capitalize import capitalize
import random


the_number = random.randint(1, 10)

assert capitalize(the_number) == 'it is a number!'
assert capitalize('') == ''
assert capitalize('hello') == 'Hello'

print('All tests passed.')