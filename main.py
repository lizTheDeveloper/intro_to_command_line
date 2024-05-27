flour_cost = 2.5  # per kg
sugar_cost = 1.5  # per kg
butter_cost = 3.0  # per kg
water_cost = 0.01 # per liter
salt_cost = 1 # per kg
yeast_cost = 0.05 # per oz
eggs_cost = 0.2 # per egg
milk_cost = 0.8 # per liter
chocolate_chips_cost = 4.0 # per kg
vanilla_extract_cost = 20 # per liter
baking_powder_cost = 0.02 # per gram
baking_soda_cost = 0.015 # per gram
cinnamon_cost = 0.03 # per gram
raisins_cost = 5.0 # per kg

# Recipes Below
recipe_name = "Dinner Rolls"
# Ingredients required for dinner rolls

flour_needed = 1  # kg
water_needed = 0.3  # liter
yeast_needed = 0.02  # oz
salt_needed = 0.01  # kg
butter_needed = 0.1  # kg
  

# Cost calculation

total_flour_cost = (flour_needed * flour_cost)
total_water_cost = (water_needed * water_cost)
total_yeast_cost = (yeast_needed * yeast_cost)
total_salt_cost = (salt_needed * salt_cost)
total_butter_cost = (butter_needed * butter_cost)

total_cost = total_flour_cost + total_water_cost + total_yeast_cost + total_salt_cost + total_butter_cost

print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")



## Pancakes Recipe
recipe_name = "Pancakes"

# Ingredients required for pancakes

flour_needed = 0.3  # kg
sugar_needed = 0.05  # kg
butter_needed = 0.1  # kg
milk_needed = 0.4  # liter
eggs_needed = 2  # eggs
baking_powder_needed = 10  # grams
baking_soda_needed = 5  # grams

total_flour_cost = (flour_needed * flour_cost)
total_sugar_cost = (sugar_needed * sugar_cost)
total_eggs_cost = (eggs_needed * eggs_cost)
total_milk_cost = (milk_needed * milk_cost)
total_water_cost = (water_needed * water_cost)
total_yeast_cost = (yeast_needed * yeast_cost)
total_salt_cost = (salt_needed * salt_cost)
total_butter_cost = (butter_needed * butter_cost)
total_baking_powder_cost = (baking_powder_needed * baking_powder_cost)
total_baking_soda_cost = (baking_soda_needed * baking_soda_cost)

total_cost = total_flour_cost + total_sugar_cost + total_eggs_cost + total_milk_cost + total_water_cost + total_yeast_cost + total_salt_cost +total_butter_cost + total_baking_powder_cost + total_baking_soda_cost

print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")



def calculate_total_cost(
        recipe_name="default recipe name",
        flour_needed=0,
        sugar_needed=0,
        butter_needed=0,
        milk_needed=0,
        eggs_needed=0,
        baking_powder_needed=0,
        baking_soda_needed=0,
        water_needed=0,
        yeast_needed=0,
        salt_needed=0,
        chocolate_chips_needed=0,
        vanilla_extract_needed=0,
        cinnamon_needed=0,
        raisins_needed=0
    ):

    total_flour_cost = (flour_needed * flour_cost)
    total_sugar_cost = (sugar_needed * sugar_cost)
    total_eggs_cost = (eggs_needed * eggs_cost)
    total_milk_cost = (milk_needed * milk_cost)
    total_water_cost = (water_needed * water_cost)
    total_yeast_cost = (yeast_needed * yeast_cost)
    total_salt_cost = (salt_needed * salt_cost)
    total_butter_cost = (butter_needed * butter_cost)
    total_baking_powder_cost = (baking_powder_needed * baking_powder_cost)
    total_baking_soda_cost = (baking_soda_needed * baking_soda_cost)
    total_chocolate_chips_cost = chocolate_chips_needed * chocolate_chips_cost
    total_vanilla_extract_cost = vanilla_extract_needed * vanilla_extract_cost
    total_baking_powder_cost = baking_powder_needed * baking_powder_cost
    total_baking_soda_cost = baking_soda_needed * baking_soda_cost
    total_cinnamon_cost = cinnamon_needed * cinnamon_cost
    total_raisins_cost = raisins_needed * raisins_cost

    total_cost = total_flour_cost + total_sugar_cost + total_eggs_cost + total_milk_cost + total_water_cost + total_yeast_cost + total_salt_cost +total_butter_cost + total_baking_powder_cost + total_baking_soda_cost + total_chocolate_chips_cost + total_vanilla_extract_cost + total_cinnamon_cost + total_raisins_cost

    print(f"Total cost to make {recipe_name}: ${total_cost:.2f}")




calculate_total_cost(
    recipe_name = "Pancakes",
    flour_needed = 0.3,  # kg
    sugar_needed = 0.05,  # kg
    butter_needed = 0.1,  # kg
    milk_needed = 0.4,  # liter
    eggs_needed = 2,  # eggs
    baking_powder_needed = 10, # grams
    baking_soda_needed = 5  # grams
)