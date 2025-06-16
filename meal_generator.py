proteins = ['chicken','salmon', 'pork','corvina', 'beef', 'trout', 'turkey', 'tilapia']
carbs = ['yuca', 'sweet potato', 'rice', 'potato', 'amaranth', 'quinoa', 'wheat', 'sweet plantain', 'maiz', 'plantain (verde)']
fruits = ['pear', 'banana', 'mandarin', 'grapes', 'mango', 'cooked apple', 'papaya', 'orange', 'granadilla', 'red fruits', 'pepino', 'coconut water', 'peach', 'cantelope', 'kiwi', 'watermelon', 'chirimoya']
vegetables = ['avocado', 'broccoli', 'cooked carrot', 'tomato', 'cauliflower', 'zucchini', 'pepinillo']

counter = {
    "protein": 0,
    "carb": 0,
    "fruit": 0,
    "vegetable": 0,
    "day": 1
}

def make_meal_plan():
    print(f"""
    Day {counter['day']} meals are...

    BREAKFAST
    =======================================
    Protein: boiled egg
    Fruit: 

    LUNCH
    =======================================
    Protein: {proteins[counter['protein']]}
    Carb: {carbs[counter['carb']]}
    Fruit: {fruits[counter['fruit']]}
    Vegetable: {vegetables[counter['vegetable']]}

    SNACK
    =======================================
    Fruit: 

    DINNER
    =======================================
    Protein: 
    Carb: 
    Vegetable: 
"""
)

for meal in range(30):
    if counter['protein'] == len(proteins) - 1:
        counter['protein'] = 0
    if counter['carb'] == len(carbs) - 1:
        counter['carb'] = 0
    if counter['fruit'] == len(fruits) - 1:
        counter['fruit'] = 0
    if counter['vegetable'] == len(vegetables) - 1:
        counter['vegetable'] = 0
    make_meal_plan()
    counter = {k: v+1 for k,v in counter.items()}
