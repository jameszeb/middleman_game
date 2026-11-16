class middle_mans:
    items=[]

class lady_selling_items:
    radio = 'Radio'
    car = 'Ford'
    bird = 'Bird'
    ladies_items = [radio,car,bird]

    def __init__(self,request):
        self.request = request

middle_man =  middle_mans()
lady= lady_selling_items(700)
print('The first offer from a lady haggler is for her ' + str(lady_selling_items.car))
my_offer = input("How much should you offer her? *hint less than $1000: ")

did_not_accept_offer = True

####Car
while(did_not_accept_offer):

    if int(my_offer) < 700:
        print('She did not accept your offer')
        my_offer = input("Please try again and present another offer: ")

    elif int(my_offer) >= 1000:
        print("too large")


    else:
        print(f'Congratulations! You succesfully bought a {lady_selling_items.car} for $' + my_offer + '\n')
        did_not_accept_offer = False
        middle_man.items.append(my_offer)

did_not_accept_offer = True
print(f"Now up for sale is a {lady_selling_items.bird}. ")
my_second_offer = input("How much should you offer her? *hint less than $50: ")
#Bird
while (did_not_accept_offer):

    if int(my_second_offer) > 15 and int(my_second_offer)< 50:
        print(f'Congratulations! You succesfully bought a {lady_selling_items.bird} for $' + my_second_offer + '\n')
        did_not_accept_offer = False
        middle_mans.items.append(my_second_offer)

    elif int(my_second_offer) >= 50 :
        print("too large")

    else:
        print('She did not accept your offer')
        my_second_offer = input("Please try again and present another offer: ")

did_not_accept_offer = True
print(f"Now up for sale is a {lady_selling_items.radio}. ")
my_third_offer = input("How much should you offer her? *hint less than $70: ")
#radio
while (did_not_accept_offer):

    if int(my_third_offer) > 50:
            print(f'Congratulations! You succesfully bought a {lady_selling_items.radio} for $' + my_third_offer + '\n')
            did_not_accept_offer = False
            middle_mans.items.append(my_third_offer)

    elif int(my_third_offer) > 90 :
            print("too large")

    else:
            print('She did not accept your offer')
            my_third_offer = input("Please try again and present another offer: ")

did_not_accept_offer = True
x=0
total = 0
for item in middle_mans.items:
    print('\nThe ' + lady_selling_items.ladies_items[x] + ' Costs $' +  item)
    total += int(item)
    x += 1

print("\nThe total amount that you spent is $" + str(total))
resell = input('would you like to sell your items and try to make more money?')

if resell == 'yes' or resell == 'y':
    print("\nWonderful! Let's begin")
else:
    print("\n   No problem! Exiting")
    exit()
## Resell code
print("\nSomeone approaches you to give you offers on your purchased items....")
list_of_purched_items = []
total_of_items_sold = 0
for item in lady_selling_items.ladies_items:
    list_of_purched_items.append(item)

for item in list_of_purched_items:
    price = input(f'How much would you like to sell your {item} for? ')
    total_of_items_sold += int(price)

print(f"\nThe total amount of money that you made is ${total_of_items_sold - total}. ")













