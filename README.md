# Ingredients-based-recipe-finder
Find recipes based on the ingredients you have at home.
A small python app to find Indian recipes using the ingredients you have. Type your ingredients and get top matching recipes with steps and images.

Features:
Search recipes by ingredients
Top 3 matches with score
Shows ingredients and process

How to Use:
1. Run the app:
         recipe finder.py
2. Enter ingredients separated by commas (tomato, potato, oil).
3. Click Find Recipes.
4. Click any recipe button to see full details.

Quick setup:
Make sure Python3 is installed (tkinter comes preinstalled with python)  and Download 'recipe finder.py' and then Run the program.

Notes:
You can add more recipes in the RECIPES list in "recipe finder.py" file.
Match score = number of keywords matched.

Code details:
1. Recipes are stored in a list of dictionaries (name, ingredient, steps).
2. User ingredients are taken from the input box and split into a list.
3. A small function checks which recipes match the entered ingredients.
4. Tkinter is used for the GUI.
5. Search button runs the match function and prints results.
6. Messagebox is used for simple alerts.
7. Code is kept easy so new recipes can be added anytime.
                    
