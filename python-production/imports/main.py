# An import lets one file use code written in another

# from the file helpers, bring in the function clean_username

from helpers import clean_username
from data import load_numbers
from stats import average

numbers = load_numbers()
print(average(numbers))  # 25.0

print(clean_username("  Alice  "))  # alice



