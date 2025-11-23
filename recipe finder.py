import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

# --- 1. RECIPE DATABASE (35 Famous Indian Dishes) ---

RECIPE_DATABASE = [
    # --- 5 Highly Detailed Indian Recipes (Indices 01-05) ---
    {
        "name": "Chicken Tikka Masala",
        "keywords": ["chicken", "yogurt", "tomato", "cream", "garam masala", "chili"],
        "ingredients": ["1 lb Chicken Breast", "1 cup Tomato Puree", "Cream", "Butter", "Garam Masala", "Yogurt"],
        "process": "Marinate, grill chicken, then simmer in a rich tomato and cream sauce.",
    },
    {
        "name": "Palak Paneer (Spinach & Cheese)",
        "keywords": ["spinach", "paneer", "cheese", "cream", "ginger", "garlic", "ghee"],
        "ingredients": ["1 bunch Fresh Spinach", "200g Paneer (cubed)", "Onion", "Ginger-Garlic Paste", "Cream", "Cumin Seeds", "Ghee"],
        "process": "Blanch and puree spinach. Sauté spices and onion. Add puree, finish with paneer and cream.",
    },
    {
        "name": "Vegetable Biryani",
        "keywords": ["rice", "vegetable", "yogurt", "onion", "biryani masala", "mint", "coriander"],
        "ingredients": ["1 cup Basmati Rice", "Mixed Vegetables", "1/4 cup Plain Yogurt", "Biryani Masala", "Fried Onion", "Ghee", "Whole Spices"],
        "process": "Partially cook rice. Marinate vegetables. Layer rice and vegetables and cook (dum method).",
    },
    {
        "name": "Dal Tadka (Spicy Lentils)",
        "keywords": ["lentil", "ghee", "cumin", "turmeric", "onion", "ginger", "garlic", "chili"],
        "ingredients": ["1 cup Mixed Lentils", "4 cups Water", "2 tbsp Ghee", "1 tsp Cumin Seeds", "Turmeric Powder", "Onion (chopped)", "Garlic (sliced)"],
        "process": "Boil lentils. Prepare a hot tempering (tadka) of ghee, cumin, onion, garlic, and chilies. Pour over the lentils.",
    },
    {
        "name": "Aloo Gobi (Potato & Cauliflower)",
        "keywords": ["potato", "cauliflower", "turmeric", "ginger", "coriander", "cumin", "tomato"],
        "ingredients": ["2 large Potatoes (cubed)", "1 medium Cauliflower (florets)", "Ginger Paste", "Turmeric Powder", "Cumin Powder", "Tomato (chopped)", "Vegetable Oil"],
        "process": "Sauté spices and ginger. Add potatoes and cauliflower. Add tomato and water. Cover and cook until tender.",
    },
    # --- 30 Placeholder Recipes (Indices 06-35) ---
    { "name": "Samosa (Fried Pastry)", "keywords": ["potato", "pea", "flour", "oil", "cumin", "ginger"], "ingredients": ["Potatoes (mashed)", "All-purpose Flour", "Peas", "Ginger Paste", "Cumin Powder", "Oil for deep frying"], "process": "Prepare dough and filling. Fill dough, seal, and deep fry until golden. (Simplified)" },
    { "name": "Chole Bhature (Chickpea Curry)", "keywords": ["chickpea", "flour", "onion", "tomato", "garam masala", "yogurt"], "ingredients": ["Chickpeas (boiled)", "All-purpose Flour", "Yogurt", "Onion & Tomato paste", "Chole Masala powder", "Oil for frying"], "process": "Cook chickpea curry (chole). Prepare and fry bhature dough. Serve hot. (Simplified)" },
    { "name": "Rajma Chawal (Kidney Beans)", "keywords": ["kidney bean", "rajma", "rice", "tomato", "onion", "ginger"], "ingredients": ["Rajma (soaked overnight)", "Basmati Rice", "Tomato Puree", "Onion (chopped)", "Ginger-Garlic Paste", "Rajma Masala", "Ghee"], "process": "Boil rajma. Prepare a spicy gravy. Add rajma and simmer. Serve with rice. (Simplified)" },
    { "name": "Vada Pav (Potato Slider)", "keywords": ["potato", "bun", "flour", "chickpea", "mustard", "chili"], "ingredients": ["Potatoes (mashed)", "Besan (Chickpea Flour)", "Pav Buns", "Mustard Seeds", "Curry Leaves", "Dry Garlic Chutney"], "process": "Prepare spiced potato balls (vadas), dip in batter, and fry. Serve in a bun with chutney. (Simplified)" },
    { "name": "Gajar Halwa (Carrot Dessert)", "keywords": ["carrot", "milk", "sugar", "ghee", "cardamom", "nut"], "ingredients": ["Carrots (grated)", "Milk", "Sugar", "Ghee", "Cardamom Powder", "Assorted Nuts"], "process": "Cook carrots and milk until milk reduces. Add ghee, sugar, and spices. Cook until thick. (Simplified)" },
    { "name": "Rogan Josh (Lamb Curry)", "keywords": ["lamb", "mutton", "yogurt", "ginger", "fennel", "cardamom"], "ingredients": ["Lamb Shoulder (cubed)", "Yogurt", "Ginger Powder", "Fennel Powder", "Cardamom Pods", "Kashmiri Chili Powder", "Ghee"], "process": "Marinate lamb in spices. Cook in ghee and yogurt. Simmer slowly until meat is tender. (Simplified)" },
    { "name": "Malai Kofta (Creamy Balls)", "keywords": ["potato", "paneer", "cream", "nut", "tomato", "ginger", "cashew"], "ingredients": ["Paneer (grated)", "Potatoes (mashed)", "Flour", "Heavy Cream", "Tomato Puree", "Cashew Paste", "Oil for frying"], "process": "Mix paneer and potato for koftas; fry. Prepare gravy using cream, cashew, and tomato. Add koftas. (Simplified)" },
    { "name": "Jalebi (Syrupy Sweet)", "keywords": ["flour", "yogurt", "sugar", "saffron", "cardamom", "ghee"], "ingredients": ["All-purpose Flour", "Yogurt", "Baking Powder", "Sugar Syrup", "Saffron Strands", "Ghee for frying"], "process": "Prepare and ferment batter. Pipe batter into hot ghee. Soak in warm syrup. (Simplified)" },
    { "name": "Dosa (Rice Crepe)", "keywords": ["rice", "lentil", "urad", "fenugreek", "fermentation", "oil"], "ingredients": ["Rice", "Urad Dal", "Fenugreek Seeds", "Salt", "Oil or Ghee"], "process": "Soak, grind, and ferment batter. Pour thinly onto hot griddle. Cook until crisp. (Simplified)" },
    { "name": "Idli Sambar (Steamed Cake)", "keywords": ["rice", "lentil", "urad", "vegetable", "tamarind", "sambar powder"], "ingredients": ["Idli Batter", "Mixed Vegetables", "Tamarind Pulp", "Sambar Powder", "Tur Dal", "Mustard Seeds", "Curry Leaves"], "process": "Steam idli batter. Cook tur dal and vegetables for sambar. Temper sambar. Serve together. (Simplified)" },
    { "name": "Uttapam (Savory Pancake)", "keywords": ["rice", "lentil", "vegetable", "onion", "tomato", "chili", "oil"], "ingredients": ["Idli/Dosa Batter", "Onion (chopped)", "Tomato (diced)", "Green Chilies", "Cilantro", "Oil or Ghee"], "process": "Pour thick batter onto tawa. Top with vegetables immediately. Cook until golden brown. (Simplified)" },
    { "name": "Shahi Paneer (Royal Curry)", "keywords": ["paneer", "cream", "cashew", "tomato", "ginger", "cardamom", "butter"], "ingredients": ["200g Paneer", "Tomato Puree", "Heavy Cream", "Cashew Paste", "Cardamom Powder", "Ginger Paste", "Butter", "Kasoori Methi"], "process": "Sauté tomato puree in butter. Add cashew paste, spices, and cream. Simmer. Add paneer cubes. (Simplified)" },
    { "name": "Masala Dosa (Stuffed Crepe)", "keywords": ["rice", "lentil", "potato", "onion", "chutney", "ghee"], "ingredients": ["Dosa Batter", "3 Boiled Potatoes (mashed)", "Onion (chopped)", "Mustard Seeds", "Curry Leaves", "Coconut Chutney"], "process": "Make thin dosa. Prepare potato masala filling. Stuff the dosa with the filling. (Simplified)" },
    { "name": "Fish Curry (Goan Style)", "keywords": ["fish", "coconut", "chili", "tamarind", "turmeric", "onion"], "ingredients": ["1 lb Fish Steaks", "Coconut Milk", "Tamarind Paste", "Goan Masala Paste", "Turmeric Powder", "Green Chilies", "Oil"], "process": "Sauté masala. Add coconut milk and tamarind. Simmer. Add fish and cook gently. (Simplified)" },
    { "name": "Gulab Jamun (Deep-fried Sweet)", "keywords": ["khoya", "milk", "sugar", "cardamom", "ghee", "frying"], "ingredients": ["1 cup Khoya", "Flour", "Sugar Syrup", "Cardamom Powder", "Ghee for deep frying"], "process": "Mix khoya and flour to form balls. Deep fry. Soak in warm syrup. (Simplified)" },
    { "name": "Tandoori Chicken (Grilled)", "keywords": ["chicken", "yogurt", "ginger", "garlic", "chili", "tandoori masala", "lemon"], "ingredients": ["1 lb Chicken pieces", "Yogurt", "2 tbsp Tandoori Masala", "Ginger-Garlic Paste", "Lemon Juice", "Red Chili Powder", "Oil or Butter"], "process": "Marinate chicken in yogurt and spices. Grill or bake until cooked and charred. (Simplified)" },
    { "name": "Jeera Rice (Cumin Rice)", "keywords": ["rice", "cumin", "ghee", "water", "coriander"], "ingredients": ["1 cup Basmati Rice", "Ghee", "Cumin Seeds", "Water", "Salt", "Fresh Coriander"], "process": "Heat ghee, add cumin. Add rice, water, and salt. Cook covered until done. (Simplified)" },
    { "name": "Pani Puri (Crispy Water Balls)", "keywords": ["puri", "potato", "chickpea", "tamarind", "mint", "pani", "chili"], "ingredients": ["Puri (crispy balls)", "Boiled Potato & Chickpeas", "Tamarind Chutney", "Mint Leaves", "Green Chilies", "Black Salt", "Water"], "process": "Prepare spiced water (pani). Fill puri with potato mix and then pani. Serve quickly. (Simplified)" },
    { "name": "Aloo Paratha (Stuffed Flatbread)", "keywords": ["wheat", "potato", "onion", "chili", "cumin", "ghee"], "ingredients": ["Whole Wheat Flour", "Potatoes (boiled, mashed)", "Onion (minced)", "Amchur", "Coriander leaves", "Ghee"], "process": "Prepare potato stuffing. Stuff dough with filling, roll, and cook on tawa with ghee. (Simplified)" },
    { "name": "Rasam (South Indian Soup)", "keywords": ["tamarind", "tomato", "pepper", "cumin", "lentil", "broth"], "ingredients": ["Tamarind Pulp", "Tomatoes", "Tur Dal (cooked)", "Rasam Powder", "Mustard Seeds", "Curry Leaves", "Ghee"], "process": "Boil tamarind water, tomato, and spices. Add cooked tur dal. Temper with mustard seeds in ghee. (Simplified)" },
    { "name": "Methi Thepla (Fenugreek Flatbread)", "keywords": ["fenugreek", "flour", "yogurt", "chili", "oil", "cumin"], "ingredients": ["Whole Wheat Flour", "Fresh Methi Leaves", "Yogurt", "Ginger-Chili Paste", "Turmeric Powder", "Oil"], "process": "Mix flour, methi, yogurt, spices to dough. Roll and cook on tawa. (Simplified)" },
    { "name": "Kofta Curry (Meatball Curry)", "keywords": ["meat", "lamb", "spice", "yogurt", "ginger", "tomato", "onion"], "ingredients": ["Ground Meat (lamb or beef)", "Yogurt", "Tomato Puree", "Onion Paste", "Garam Masala", "Ginger-Garlic Paste", "Oil for frying"], "process": "Mix meat with spices, form kofta, and fry. Prepare gravy and simmer kofta. (Simplified)" },
    { "name": "Masala Chai (Spiced Tea)", "keywords": ["milk", "water", "tea", "ginger", "cardamom", "sugar", "clove"], "ingredients": ["Milk", "Water", "Black Tea Leaves", "Ginger (crushed)", "Cardamom Pods", "Clove", "Sugar"], "process": "Boil water, ginger, cardamom, and tea. Add milk and sugar. Simmer, strain. (Simplified)" },
    { "name": "Hyderabadi Biryani", "keywords": ["chicken", "rice", "yogurt", "saffron", "spice", "mint", "coriander"], "ingredients": ["Chicken", "Basmati Rice", "Yogurt", "Biryani Masala", "Saffron Milk", "Fried Onions", "Mint Leaves", "Ghee"], "process": "Marinate chicken. Layer partially cooked rice and chicken in a pot. Dum cook until done. (Simplified)" },
    { "name": "Dhokla (Steamed Cake)", "keywords": ["besan", "chickpea", "yogurt", "steaming", "mustard", "chili"], "ingredients": ["Besan (Chickpea Flour)", "Yogurt", "Ginger-Chili Paste", "Eno Fruit Salt", "Mustard Seeds", "Curry Leaves", "Oil"], "process": "Mix batter, add Eno, steam. Temper with mustard and curry leaves. (Simplified)" },
    { "name": "Kulfi (Indian Ice Cream)", "keywords": ["milk", "sugar", "cardamom", "pistachio", "saffron", "freezing"], "ingredients": ["Full-fat Milk", "Sugar", "Cardamom Powder", "Saffron Strands", "Pistachios (chopped)", "Sweetened Condensed Milk"], "process": "Reduce milk. Add sugar, spices. Cool, pour into molds, freeze. (Simplified)" },
    { "name": "Sambar (Vegetable Lentil Stew)", "keywords": ["lentil", "vegetable", "tamarind", "sambar powder", "tur dal", "mustard"], "ingredients": ["Tur Dal", "Mixed Vegetables", "Tamarind Pulp", "Sambar Powder", "Asafoetida", "Mustard Seeds", "Ghee"], "process": "Cook dal and veg. Add tamarind and sambar powder. Temper with mustard. (Simplified)" },
    { "name": "Khandvi (Rolled Snack)", "keywords": ["besan", "yogurt", "turmeric", "mustard", "ginger", "oil"], "ingredients": ["Besan", "Sour Yogurt", "Ginger-Chili Paste", "Turmeric Powder", "Mustard Seeds", "Curry Leaves", "Oil"], "process": "Cook besan and yogurt batter until thick. Spread thinly, roll, temper. (Simplified)" },
    { "name": "Besan Cheela (Savory Pancake)", "keywords": ["besan", "onion", "tomato", "chili", "coriander", "ginger"], "ingredients": ["Besan", "Water", "Chopped Onion", "Tomato, Coriander, Green Chili", "Ginger Paste", "Oil"], "process": "Mix besan, water, spices, and veg for batter. Cook on griddle. (Simplified)" },
    { "name": "Puri (Fried Flatbread)", "keywords": ["wheat", "flour", "oil", "salt", "frying"], "ingredients": ["Whole Wheat Flour", "Water", "Oil for deep frying", "Salt"], "process": "Make tight dough. Roll thin circles. Deep fry until puffed. (Simplified)" },
]

# Final verification
if len(RECIPE_DATABASE) != 35:
    print(f"FATAL ERROR: Database size is {len(RECIPE_DATABASE)} and should be 35. Please check the RECIPE_DATABASE list.")


# --- 2. THE TKINTER GUI APPLICATION CLASS ---

class RecipeFinderApp:
    # Removed: tk_image_ref = None (Not needed without images)
    
    # --- COLOR PALETTE ---
    BG_MAIN = "#282c34" 
    FG_MAIN = "#ffffff" 
    ACCENT_GREEN = "#98c379"
    ACCENT_RED = "#e06c75" 
    ACCENT_YELLOW = "#e5c07b"

    def __init__(self, master):
        self.master = master
        master.title("🇮🇳 Simple Indian Recipe Finder (35 Dishes)")
        master.geometry("900x800")
        master.configure(bg=self.BG_MAIN)
        
        # UI Setup
        header_font = ("Arial", 26, "bold")
        
        tk.Label(master, text="🇮🇳 Simple Indian Recipe Search (Top 3)", font=header_font, bg=self.BG_MAIN, fg=self.ACCENT_YELLOW).pack(pady=20)
        
        # Input Section
        tk.Label(master, text=f"Enter Ingredients (separated by commas). Searching across {len(RECIPE_DATABASE)} Indian recipes:", 
                 font=("Arial", 13), bg=self.BG_MAIN, fg=self.FG_MAIN).pack()
        
        self.entry_ingredients = tk.Entry(master, width=60, font=("Arial", 14), bd=3, relief=tk.RIDGE, 
                                          bg="#3a3f4a", fg=self.FG_MAIN, insertbackground=self.FG_MAIN)
        self.entry_ingredients.pack(pady=10, padx=20)

        # Button
        self.find_button = tk.Button(master, text="🔍 Find Top 3 Recipes", command=self.find_recipes, 
                                     bg=self.ACCENT_GREEN, fg=self.BG_MAIN, font=("Arial", 15, "bold"), 
                                     activebackground="#79b062", padx=15, pady=8)
        self.find_button.pack(pady=15)

        # Interactive Results Display Area
        tk.Label(master, text="--- Clickable Top 3 Matches ---", font=("Arial", 16, "underline"), bg=self.BG_MAIN, fg=self.FG_MAIN).pack()
        
        self.button_frame = tk.Frame(master, bg=self.BG_MAIN, bd=2, relief=tk.SUNKEN)
        self.button_frame.pack(pady=10, padx=20, fill=tk.X)
        
        tk.Label(master, text="Recipe Detail View:", font=("Arial", 13, "bold"), bg=self.BG_MAIN, fg=self.FG_MAIN).pack(pady=5)
        
        self.results_area = scrolledtext.ScrolledText(master, width=100, height=20, wrap=tk.WORD, 
                                                     font=("Consolas", 11), padx=15, pady=15, bd=2, relief=tk.SUNKEN, 
                                                     bg="#3a3f4a", fg=self.FG_MAIN, insertbackground=self.FG_MAIN, state='disabled')
        self.results_area.pack(padx=20, pady=10)
        
        # Configure tags for improved text display
        self.results_area.tag_configure("dish_name_tag", font=("Arial", 26, "bold"), foreground=self.ACCENT_GREEN)
        self.results_area.tag_configure("body_text_tag", font=("Consolas", 12))
        self.results_area.tag_configure("header_tag", font=("Arial", 14, "bold"), foreground=self.ACCENT_YELLOW)

        # Initial Message
        self.results_area.config(state='normal')
        self.results_area.insert(tk.END, "Enter ingredients and click 'Find Top 3 Recipes' to begin.")
        self.results_area.config(state='disabled')


    def show_detailed_view(self, recipe_data, match_count):
        """Displays the full, organized recipe details."""
        
        self.results_area.config(state='normal')
        self.results_area.delete(1.0, tk.END)
        
        # --- 1. IMAGE/NAME FRAME REMOVED ---
        
        # --- 2. TEXT INSERTION (Simplified) ---
        dish_name_text = recipe_data['name'].upper().split('(')[0].strip()
        
        # Use tags for formatting
        self.results_area.insert(tk.END, dish_name_text + "\n", "dish_name_tag")
        self.results_area.insert(tk.END, "=" * 80 + "\n")
        
        # Match Score
        self.results_area.insert(tk.END, f"MATCH SCORE: {match_count} ingredient(s) matched.\n\n", "header_tag")
        
        # Ingredients Section
        self.results_area.insert(tk.END, ">>> INGREDIENTS NEEDED:\n", "header_tag")
        ingredients_text = "\n".join([f"  • {ingredient}" for ingredient in recipe_data['ingredients']])
        self.results_area.insert(tk.END, ingredients_text + "\n\n", "body_text_tag")
        
        # Process Section
        self.results_area.insert(tk.END, ">>> PROCESS INSTRUCTIONS:\n", "header_tag")
        self.results_area.insert(tk.END, f"{recipe_data['process']}\n", "body_text_tag")
        
        self.results_area.config(state='disabled')


    def find_recipes(self):
        # 1. Input Processing
        user_input = self.entry_ingredients.get().lower()
        input_list = [item.strip() for item in user_input.split(',') if item.strip()]

        if not RECIPE_DATABASE:
            messagebox.showerror("Data Error", "Recipe database is empty.")
            return
            
        # 2. Search Logic (Matching Score)
        matching_recipes = []
        
        for recipe in RECIPE_DATABASE:
            match_count = sum(1 for keyword in recipe["keywords"] if keyword in input_list)
            
            if match_count > 0:
                matching_recipes.append({"recipe": recipe, "matches": match_count})
        
        matching_recipes.sort(key=lambda x: x["matches"], reverse=True)

        # Limit to Top 3 Matches
        display_matches = matching_recipes[:3]

        # 3. Clear the button frame 
        for widget in self.button_frame.winfo_children():
            widget.destroy()
            
        # 4. Display Buttons for Top 3 Matches
        if not display_matches:
            tk.Label(self.button_frame, text="No matching recipes found.", fg=self.ACCENT_RED, font=("Arial", 12), bg=self.BG_MAIN).pack(padx=10, pady=10)
        else:
            for i, match_item in enumerate(display_matches):
                recipe = match_item["recipe"]
                match_info = match_item["matches"]
                
                button_text = f"Rank {i+1}: {recipe['name']} (Match: {match_info}) - CLICK HERE!"
                
                # Highlight Rank 1
                if i == 0:
                    btn_bg = self.ACCENT_YELLOW
                    btn_fg = self.BG_MAIN 
                    btn_active_bg = "#d6b05e"
                else:
                    btn_bg = self.ACCENT_GREEN
                    btn_fg = self.BG_MAIN
                    btn_active_bg = "#79b062"
                    
                tk.Button(self.button_frame, 
                          text=button_text, 
                          font=("Arial", 11, "bold"), 
                          bg=btn_bg,
                          fg=btn_fg,
                          activebackground=btn_active_bg,
                          command=lambda r=recipe, m=match_info: self.show_detailed_view(r, m)
                         ).pack(side=tk.LEFT, padx=5, pady=5)
                         
        # Update the detailed area with instructions
        self.results_area.config(state='normal')
        self.results_area.delete(1.0, tk.END)
        self.results_area.insert(tk.END, "Click one of the buttons above to view the full details for that recipe.")
        self.results_area.config(state='disabled')


# --- 3. THE EXECUTION BLOCK ---

if __name__ == '__main__':
    if len(RECIPE_DATABASE) != 35:
         print(f"FATAL WARNING: Database size is {len(RECIPE_DATABASE)}, not 35. Please check the RECIPE_DATABASE list.")
    
    # Removed: Image folder check
    
    root = tk.Tk()
    app = RecipeFinderApp(root)
    root.mainloop()
