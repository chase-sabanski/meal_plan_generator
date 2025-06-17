import os

proteins = ['chicken','salmon', 'pork','corvina', 'beef', 'trout', 'turkey', 'tilapia']
carbs = ['yuca', 'sweet potato', 'rice', 'potato', 'amaranth', 'quinoa', 'wheat', 'sweet plantain', 'maiz', 'plantain (verde)']
fruits = ['pear', 'banana', 'mandarin', 'grapes', 'mango', 'cooked apple', 'papaya', 'orange', 'granadilla', 'red fruits', 'pepino', 'coconut water', 'peach', 'cantelope', 'kiwi', 'watermelon', 'chirimoya']
vegetables = ['avocado', 'broccoli', 'cooked carrot', 'tomato', 'cauliflower', 'zucchini', 'pepinillo']

# extends the list of foods so that I don't have to reset at the end of a list, lazy(?) but functional
while len(proteins) < 100:
    proteins.extend(proteins)
while len(carbs) < 100:
    carbs.extend(carbs)
while len(fruits) < 100:
    fruits.extend(fruits)
while len(vegetables) < 100:
    vegetables.extend(vegetables)

counter = {
    "protein": 0,
    "carb": 0,
    "fruit": 0,
    "vegetable": 0,
    "day": 1
}

# two days are paired together to so that lunch for day x is dinner for day y and vice versa. A bit messy, but functional.
def make_meal_plan():
    return(f"""
Day {counter['day']} meals are...

    BREAKFAST
    =======================================
    Protein: boiled egg
    Fruit: {fruits[counter['fruit']]}

    LUNCH
    =======================================
    Protein: {proteins[counter['protein']]}
    Carb: {carbs[counter['carb']]}
    Fruit: {fruits[counter['fruit']]}
    Vegetable: {vegetables[counter['vegetable']]}

    SNACK
    =======================================
    Fruit: {fruits[counter['fruit']]}

    DINNER
    =======================================
    Protein: {proteins[counter['protein'] + 1]}
    Carb: {carbs[counter['carb'] + 1]}
    Vegetable: {vegetables[counter['vegetable'] + 1]}

Day {counter['day'] + 1} meals are...

    BREAKFAST
    =======================================
    Protein: boiled egg
    Fruit: {fruits[counter['fruit'] + 1]}

    LUNCH
    =======================================
    Protein: {proteins[counter['protein'] + 1]}
    Carb: {carbs[counter['carb'] + 1]}
    Fruit: {fruits[counter['fruit'] + 1]}
    Vegetable: {vegetables[counter['vegetable'] + 1]}

    SNACK
    =======================================
    Fruit: {fruits[counter['fruit'] + 1]}

    DINNER
    =======================================
    Protein: {proteins[counter['protein']]}
    Carb: {carbs[counter['carb']]}
    Vegetable: {vegetables[counter['vegetable']]}
"""
)

meals = []

# loops through the make_meal_plan() 15 times because running the function once creates meals for 2 days. 2 x 15 = 30 days.
# increments the counter by 2 each loop so that only two days have overlapping foods
for meal in range(15):
    meals.append(make_meal_plan())
    counter = {k: v+2 for k,v in counter.items()}

# Changes the cwd to the directory of the file
current_directory = os.path.dirname(__file__)
os.chdir(current_directory)

output = ''.join(meals)
with open("meal_plan.txt", "w") as f:
    f.write(output)
