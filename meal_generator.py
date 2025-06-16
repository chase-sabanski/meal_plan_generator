proteins = ['chicken','salmon', 'pork','corvina', 'beef', 'trout', 'turkey', 'tilapia']
carbs = ['yuca', 'sweet potato', 'rice', 'potato', 'amaranth', 'quinoa', 'wheat', 'sweet plantain', 'maiz', 'plantain (verde)']
fruits = ['pear', 'banana', 'mandarin', 'grapes', 'mango', 'cooked apple', 'papaya', 'orange', 'granadilla', 'red fruits', 'pepino', 'coconut water', 'peach', 'cantelope', 'kiwi', 'watermelon', 'chirimoya']
vegetables = ['avacado', 'broccoli', 'cooked carrot', 'tomato', 'cauliflower', 'zuccini', 'pepinillo']

counter = {
    "protein": 0,
    "carb": 0,
    "fruit": 0,
    "vegetable": 0,
    "day": 1
}

def make_meal():
    print(f"""
    Day {counter['day']} lunch is...
    Protein: {proteins[counter['protein']]}
    Carb: {carbs[counter['carb']]}
    Fruit: {fruits[counter['fruit']]}
    Vegetable: {vegetables[counter['vegetable']]}
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
    make_meal()
    counter = {k: v+1 for k,v in counter.items()}
