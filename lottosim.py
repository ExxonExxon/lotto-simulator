import random

"---------------------------------------------VAR----------------------------------------------"

lotto_numbers = [] # Lotto Numbers (KEEP THIS VARIABLE BLANK)
trys = 0 # Trys done (KEEP THIS VARIABLE BLANK)

user_money = 100 # The amount of money for the user


"----------------------------------------------------------------------------------------------"


"-------------------------------------------SETTINGS-------------------------------------------"

number_of_tickets_a_day = 5 # Number of tickets to buy a day
number_of_days = 100 # How long to run the test for in days (NOT REAL LIFE DAYS DONT WORRY)

ticket_price = 10 # Ticket price 

number_of_lotto_numbers = 7 # The number of lotto numbers (the lower the faster)
range_lotto_numbers = 69 # The range of the lotto numbers 

"----------------------------------------------------------------------------------------------"



def create_lotto_numbers():
    global range_lotto_numbers, number_of_lotto_numbers

    """
    Generates lotto numbers depending on the settings above
    
    """
    
    lotto_numbers = []
    
    for i in range(number_of_lotto_numbers):
        lotto_numbers.append(random.randint(0, range_lotto_numbers)) 

    return lotto_numbers


def guess_lotto_numbers():
    global range_lotto_numbers, lotto_numbers, user_money

    """

    Guesses Lotto Numbers from the settings above using 2 for loops
    
    """

    for day in range(number_of_days):

        for ticket in range(number_of_tickets_a_day):

            lotto_numbers = create_lotto_numbers()
            guessed_numbers = [] 
            guessed_number_try = 0

            for i in range(7):
                guessed_number = random.randint(0, range_lotto_numbers)
                guessed_numbers.append(guessed_number)
                if guessed_number in lotto_numbers:
                    guessed_number_try += 1

            # Prize calculation
            if guessed_number_try >= 3:
                if guessed_number_try == 3:
                    user_money += 100
                elif guessed_number_try == 4:
                    user_money += 1000
                elif guessed_number_try == 5:
                    user_money += 50000
                elif guessed_number_try == 6:
                    user_money += 1000000
                elif guessed_number_try == 7:
                    user_money += 40000000

            # Deduct ticket price
            user_money -= ticket_price

            print("Day:", day, "| Ticket:", ticket, "| Guessed Numbers:", guessed_numbers, "| Matched:", guessed_number_try, "| Current User Money", user_money)

guess_lotto_numbers()
