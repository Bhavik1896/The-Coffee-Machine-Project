# TODO 1 :- Print All The Resource of A Coffee machine

from data import resources, MENU
is_on = True
money = 0

# TODO 2 :- Prompt user by asking “What would you like? (espresso/latte/cappuccino):"


def is_resource_sufficient(order_ingridients):
	is_enough = False
	for item in order_ingridients:
		if order_ingridients[item] >= resources[item]:
			print(f"SORRY there is not enough {item}")
			is_enough = False
		is_enough = True
def process_coins():
	"""Returns total calculated from coin inserted"""
	print("Please insert coins")
	total = int(input("How may quaters?"))*0.25
	total += int(input("How may dimes?")) * 0.1
	total += int(input("How may nickles?"))*0.05
	total += int(input("How may pennies?"))*0.01
	return total
def is_transaction_successful(money_received, drink_cost):
	if money_received >= drink_cost:
		change = round(money_received-drink_cost, 2)
		print(f"You had made it complete and here is your ${change} change")
		global money
		money += drink_cost
	else:
		print("Sorry that's not enough money. Money refunded.")
def make_coffee(order_ingredients, drink_name):
	for item in order_ingredients:
		resources[item] -= order_ingredients[item]
	print(f"Here is Your {choice} ☕️")


while is_on:
	choice = input("What would you like? (espresso/latte/cappuccino)").lower()
# TODO 7 :- Turn off the Coffee Machine by entering “off”to the prompt.
	if choice == "off":
		is_on = False
		
	elif choice == "report":
		print(f"Water: {resources['water']}ml")
		print(f"Milk: {resources['milk']}ml")
		print(f"Coffee: {resources['coffee']}g")
		print(f"Money: ${money}")
	else:
		drink = MENU[choice]
		print(drink)
		is_resource_sufficient(drink['ingredients'])
		payment = process_coins()
		is_transaction_successful(payment, drink["cost"])
		make_coffee(drink['ingredients'], drink)
# TODO 3 :- Check resources sufficient?




# TODO 4 :- Process coins.
# TODO 5 :- Check transaction successful?
# TODO 6 :- Make Coffee


