# Ingredients-based-recipe-finder

Project title: 
Ingredients based recipe finder

Overview of the project :
This is a small desktop app made using Python and Tkinter, where users can type ingredients they have at home and the app will try to find the top 3 matching Indian recipes.
The purpose of this project is to give a very easy idea of how ingredient-based recipe searching works.

Features:
Search Indian recipes by writing ingredients.
It will give top 3 matches with clickable buttons.
Shows ingredients and process.


Technologies/Tools used:
Python 3
Tkinter GUI Library
ScrolledText widget
Simple list based recipe database.


How to Use:
1. Run the app:
         python recipe finder.py
2. Enter ingredients separated by commas (tomato, potato, oil).
3. Click Find Recipes.
4. Click any recipe button to see full details.

Quick setup:
Make sure Python3 is installed (tkinter comes preinstalled with python)  and Download 'recipe finder.py' and then Run the program.


Instruction for testing:
1.Try searching with few different ingredient combos and see if results coming properly.
2.Check if Top 3 recipes are showing and buttons are working fine.
3.Click on each recipe and confirm the full details is opening correctly.
4.Give some totally unmatched ingredients to make sure the “no recipe found” message is working.
5.Restart the app once to see it running smoothly without any random error.


Code details:
1. Recipes are stored in a list of dictionaries (name, ingredient, steps).
2. User ingredients are taken from the input box and split into a list.
3. A small function checks which recipes match the entered ingredients.
4. Tkinter is used for the GUI.
5. Search button runs the match function and prints results.
6. Messagebox is used for simple alerts.
7. Code is kept easy so new recipes can be added anytime.
                    
