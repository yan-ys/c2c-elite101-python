import time
def order_food():
    print('----------Ordering Food Page----------')
    time = input('What time you would like your taxi to arrive X:XX: ')
    am_or_pm = input('AM or PM: ')
    try:
        distance = int(input('How many miles away is your destination: '))
        food_price = int(input('How much money does your order cost? '))
        confirm_order = input('Enter 1 to confirm your order or any other key to cancel: ')
        if confirm_order == '1':
            print(f'----------Receipt For {name}----------')
            print(f'Food order confirmed. Your food will arive at {time}{am_or_pm}.')
            print('Your delivery fee will be ' + str(1.5*distance) + " dollars. Your total will be " + str(1.5*distance+food_price) + "dollars")
        else:
            print('Food order canceled.')
    except:
        print('Invalid input...returning to main menu.')
        print('Taxi order canceled.')
def review():
    print('----------Reviews Page----------')
    app_or_driver = input('Enter 1 to leave a review for the app or 2 to review your delivery person: ')
    if app_or_driver == '1':
        rating = input('Rate us from 1-5 stars: ')
        if rating == '5' or '4':
            print('Thank you!')
        else:
            print('How can we improve? ')
            feedback = input('Enter your valued feedback: ')
    else:
        review_who = input('Enter the name of the delivery person you want to review: ')
        rating = input('Rate your delivery person from 1-5 stars: ')
        print(f'You rated {review_who} {rating} stars.')
        if rating == '5' or rating == '4':
            print('Thank you for your feedback on our drivers.')
        else:
            print('What went wrong? ')
            feedback = input('Enter your valued feedback: ')
            refund_wanted = input('Enter 1 if you would like to request a refund: ')
            if refund_wanted == '1':
                refund()
def refund():
    print('----------Refunds Page----------')
    refund_reason = input('Enter reason for refund: ')
    want_a_refund = input('Enter 1 to confirm your refund request, 2 to re-order food, and any other key to cancel: ')
    if want_a_refund == '1':
        refund_to_where = input('Enter 1 for app credit refund (with bonus credit) or 2 to refund the funds to the original payment method ')
        try:
            refund_amount = int(input('Enter an estimate of your order amount to be refunded: '))
            if refund_to_where == '1':
                print('Refund request sent...if request is approved you will recieve bonus app credit of ' + str(refund_amount*1.05) + ' dollars in 1-3 business days')
            else:
                print('Refund request sent...if request is approved you will recieve your refunded funds in your original payment method.')
        except:
            print('Please enter a valid refund amount...exiting')
    elif want_a_refund == '2':
        print('-----Re-ordering food page-----')
        food_to_reorder = input('What food what you like to re-order: ')
        print(f'Re-ordering {food_to_reorder}, your original payment will be used to cover this transaction')
    else:
        print('Refund request canceled...')




def chatbot(choice):
    while choice != '4':
        print(f'\nHi, {name}! Welcome to the food delivery app support chatbot. How can I help you?')
        print('\t1. order food\n\t2. leave a review\n\t3. request a refund\n\t4. exit the conversation')
        choice = input('Enter the number of your choice: ')
        if choice == '1':
            order_food()
        elif choice == '2':
            review()
        elif choice == '3':
            refund()
        elif choice == '4':
            print(f'Goodbye {name}! Thank you for using the food delivery chatbot.')
            quit()
        else:
            print('Please enter a valid option.')
        time.sleep(4)



print("Welcome to food delivery chatbot")
choice = None
name = input('Enter your name: ')
try:
    age = int(input('Enter your age: '))
except:
    print('Please enter a valid age...closing chatbot')
    quit()
if age < 13:
    print('You need to be at least 13 to use the taxi chatbot\nEnding conversation...')
else:
    chatbot(choice)
