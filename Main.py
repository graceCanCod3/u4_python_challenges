import math

# Python Challenges


#  1) The Time Stone: Lets get cosmic here and begin working with Time.

# - First, lets create a function that converts Minutes to Seconds (1 ->60, 5 -> 300)
# -  Then take it up a step further, converting Hours into seconds (1 -> 3600)
# -  We're on the right track here, how many seconds are in a day
# - How many Hours are in the month of June? 
# - How many Minutes are in the month of August?
 
 
 # Bonus -> Without singing the old showtune in your head, how many Minutes are there in a year? 
 # In days, in weeks, in cups of coffee?


# ---------------------------------
#      Solution Goes Here ->

def min_to_sec(m):
    return m * 60

def hr_to_sec(h):
    return h * 3600

def sec_in_a_day():
    return hr_to_sec(1) * 24

def hrs_in_june():
    return 24 * 30

def mins_in_august():
    return 60 * 24 * 31

def mins_in_a_year():
    return 365 * 24 * 60


print(min_to_sec(1))  
print(min_to_sec(5))  
print(hr_to_sec(1)) 
print(sec_in_a_day())  
print(hrs_in_june())  
print(mins_in_august())  
print(mins_in_a_year())

# ---------------------------------



#  2) Middle letter

# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
# For example, mid("abc") should return "b" and mid("aaaa") should return "".


# ---------------------------------
#      Solution Goes Here ->

def mid(s):
    length = len(s)
    if length % 2 == 0:
        return ""
    else:
        return s[length // 2]
    
print(mid("grace")) 
print(mid("aaaa"))
# ---------------------------------


# ### 3) Hide the credit card number
# Write a function in Python that accepts a credit card number. It should return a string where all the characters are hidden with an asterisk except the last four. For example, if the function gets sent "1234567894444", then it should return "*********4444".


# ---------------------------------
#      Solution Goes Here ->

def hide(card_number):
    return '*' (len(card_number) - 4) + card_number[-4:]

print(hide("1213242536374897")) 
# ---------------------------------



# ### 4) Online status
# The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

# For example, consider the following dictionary:

# ```
statuses = {
    "John": "online",
    "Paul": "offline",
    "George": "online",
    "Ringo": "offline"
}

# ```

# In this case, the number of people online is 2.
# Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
# Your function should return the number of people who are online.


# ---------------------------------
#      Solution Goes Here ->

def online_count(statuses):
    return sum(1 for status in statuses.values() if status == "online")

print(online_count(statuses)) 
# ---------------------------------



#  5) Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. The second should be the discount percentage as an integer.
# The function should return the price of the item after the discount has been applied. For example, if the price is 100 and the discount is 20, the function should return 80.

# ---------------------------------
#      Solution Goes Here ->

def discounted_price(price, discount):
    return price - (price * discount / 100)

print(discounted_price(50, 10))
# ---------------------------------


#  6) Pythagorean Theorum

# As any High School sophomore will tell you, the sum of the squares of two legs of a right trangle will equal the square of the hypotenouse.
# Create a function that takes two integers as the Adjacent and Opposite legs of a triangle, and returns an integer of the Hypotenouse


# ---------------------------------
#      Solution Goes Here ->

def hypotenuse(a, b):
    return int(math.sqrt(a ** 2 + b ** 2))

print(hypotenuse(3, 4))
# ---------------------------------


#  7) Fibonacci Sequence 
# Everyone's favorite Math Problem!

# The Fibonacci numbers are the numbers in the following integer sequence.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
# In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation between two adjacent steps in a list
# Create a python function that takes two numbers and finds the next Nine intervals using the Fibonacci Sequence

# ---------------------------------
#      Solution Goes Here ->

def fibonacci_sequence(n1, n2):
    sequence = [n1, n2]
    for _ in range(7):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci_sequence(0, 1)) 
print(fibonacci_sequence(2, 3))
# ---------------------------------
