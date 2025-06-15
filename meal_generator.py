import random as rd

proteins = ['chicken','salmon', 'pork','corvina', 'beef', 'trout', 'turkey', 'tilapia']
carbs = ['yuca', 'sweet potato', 'rice', 'potato', 'amaranth', 'quinoa', 'wheat', 'sweet plantain', 'maiz', 'plantain (verde)']
fruits = ['pear', 'banana', 'mandarin', 'grapes', 'mango', 'cooked apple', 'papaya', 'orange', 'granadilla', 'red fruits', 'pepino', 'coconut water', 'peach', 'cantelope', 'kiwi', 'watermelon', 'chirimoya']
vegetables = ['avacado', 'broccoli', 'cooked carrot', 'tomato', 'cauliflower', 'zuccini', 'pepinillo']

proteins_counter = 0
carbs_counter = 0
fruits_counter = 0
vegetables_counter = 0
day = 1

def make_meal():
    selected_protein = proteins[proteins_counter]
    selected_carb = carbs[carbs_counter]
    selected_fruit = fruits[fruits_counter]
    selected_vegetable = vegetables[vegetables_counter]
    print(f"""
    Day {day} lunch is...
    Protein: {selected_protein}
    Carb: {selected_carb}
    Fruit: {selected_fruit}
    Vegetable: {selected_vegetable}
"""
)

make_meal()
