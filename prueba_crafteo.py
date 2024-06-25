class Item:
	def __init__(self,name):
		self.name = name

	def __repr__(self):
		return self.name


class Recipe:
	def __init__(self,output, ingredients):
		self.output = output
		self.ingredients = ingredients

	def __repr__(self):
		ingredients_str = ', '.join([f'{v}x {k}' for k, v in self.ingredients.items()])
		return f'{self.output} <- {ingredients_str}'

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity=1):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item] >= quantity:
                self.items[item] -= quantity
                if self.items[item] == 0:
                    del self.items[item]
            else:
                print(f"Not enough {item.name} in inventory.")
        else:
            print(f"No {item.name} in inventory.")

    def has_items(self, items):
        for item, quantity in items.items():
            if self.items.get(item, 0) < quantity:
                return False
        return True

    def craft(self, recipe):
        if self.has_items(recipe.ingredients):
            for item, quantity in recipe.ingredients.items():
                self.remove_item(item, quantity)
            self.add_item(recipe.output)
            print(f"Crafted {recipe.output.name}!")
        else:
            print("Not enough ingredients to craft this item.")

    def __repr__(self):
        return f'Inventory: {self.items}'


if __name__ == '__main__':
	# Define items
	wood = Item('Wood')
	stone = Item('Stone')
	stick = Item('Stick')
	pickaxe = Item('Pickaxe')

	# Define recipes
	stick_recipe = Recipe(stick, {wood: 2})
	pickaxe_recipe = Recipe(pickaxe, {stick: 2, stone: 3})

	# Create inventory and add items
	inventory = Inventory()
	inventory.add_item(wood, 10)
	inventory.add_item(stone, 10)
	#inventory.add_item(stick, 10)

	print(inventory)

	# Craft items
	inventory.craft(stick_recipe)
	inventory.craft(stick_recipe)
	print(inventory)
	inventory.craft(pickaxe_recipe)

	print(inventory)
