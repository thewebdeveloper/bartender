import random

questions = {
	"strong": "Do ye like yer drinks strong?",
	"salty": "Do ye like it with a salty tang?",
	"bitter": "Are ye a lubber who likes it bitter?",
	"sweet": "Would ye like a bit of sweetness with yer poison?",
	"fruity": "Are ye one for a fruity finish?",
}

ingredients = {
	"strong": ["glug of rum", "slug of whisky", "splash of gin"],
	"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
	"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
	"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
	"fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def ask_for_drink():
	'''
	This function asks the pirates for thier styles in drinks, and thier answer 'yes' or 'no' will define thier styles.
	Each answer being added to the dictionary, mapped with boolean, and finally return the new dictionary(styles). 
	'''
	styles = {}
	for k,v in questions.items():
		style = input("Bartender: {} (Hint: if yes, your answer should be inserted as 'yes' or 'y')\nPirate: ".format(v))
		if style == 'yes' or style == 'y':
			styles[k] = True
		else:
			styles[k] = False
	return styles
	
	
def make_drink(preferences):
	'''
	This function gets the drink styles of the pirates from ask_for_drink function, checks the ingredients of each style,
	choose one type of each ingredient list randomly, and add it to the drink list of the pirates.
	'''
	drink = []
	for k,v in preferences.items():
		if v == True:
			ingredient = random.choice(ingredients[k]) 
			drink.append(ingredient)
	return drink


if __name__ == '__main__':
	print(make_drink(ask_for_drink()))
