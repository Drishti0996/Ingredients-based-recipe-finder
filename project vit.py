import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import os

# ----------------- 1. SIMPLE RECIPE DATABASE -----------------
RECIPES = [
    {"name": "Chicken Tikka Masala", 
     "keywords": ["chicken", "yogurt", "tomato", "cream", "garam masala"], 
     "ingredients": ["1 lb Chicken", "Tomato Puree", "Cream", "Butter", "Garam Masala", "Yogurt"],
     "process": "Marinate chicken, grill, simmer in tomato & cream sauce.", 
     "image_file": "recipe_01_chicken_tikka_masala.jpg"},
    
    {"name": "Palak Paneer", 
     "keywords": ["spinach", "paneer", "cheese", "cream"], 
     "ingredients": ["Spinach", "Paneer", "Onion", "Ginger-Garlic Paste", "Cream", "Ghee"],
     "process": "Blanch spinach, sauté spices & onion, add puree, paneer, cream.", 
     "image_file": "recipe_02_palak_paneer.jpg"},
    
    {"name": "Vegetable Biryani", 
     "keywords": ["rice", "vegetable", "yogurt", "onion"], 
     "ingredients": ["Basmati Rice", "Mixed Vegetables", "Yogurt", "Biryani Masala", "Fried Onion", "Ghee"],
     "process": "Partially cook rice, marinate veggies, layer & cook (dum method).",
     "image_file": "recipe_03_vegetable_biryani.jpg"},
]

# Ensure images folder exists
if not os.path.exists("images"):
    os.makedirs("images")
    print("Created 'images' folder. Place recipe images here.")

# ----------------- 2. GUI APP CLASS -----------------
class RecipeFinder:
    tk_image_ref = None  # keep reference for Tkinter images

    BG = "#282c34"
    FG = "#ffffff"
    ACCENT_GREEN = "#98c379"
    ACCENT_RED = "#e06c75"
    ACCENT_YELLOW = "#e5c07b"

    def __init__(self, master):
        self.master = master
        master.title("🇮🇳 Indian Recipe Finder")
        master.geometry("800x700")
        master.configure(bg=self.BG)

        # Header
        tk.Label(master, text="🍲 Recipe Finder (Top 3)", font=("Arial", 24, "bold"),
                 bg=self.BG, fg=self.ACCENT_YELLOW).pack(pady=15)

        # Ingredient Input
        tk.Label(master, text="Enter ingredients (comma-separated):", font=("Arial", 12),
                 bg=self.BG, fg=self.FG).pack()
        self.entry = tk.Entry(master, width=50, font=("Arial", 14), bd=3, relief=tk.RIDGE,
                              bg="#3a3f4a", fg=self.FG, insertbackground=self.FG)
        self.entry.pack(pady=8)

        tk.Button(master, text="🔍 Find Recipes", font=("Arial", 12, "bold"),
                  bg=self.ACCENT_GREEN, fg=self.BG, padx=10, pady=5,
                  command=self.find_recipes).pack(pady=10)

        # Top matches buttons
        self.button_frame = tk.Frame(master, bg=self.BG)
        self.button_frame.pack(pady=5, fill=tk.X)

        # Recipe details area
        self.text_area = scrolledtext.ScrolledText(master, width=90, height=25, wrap=tk.WORD,
                                                   font=("Consolas", 11), bg="#3a3f4a", fg=self.FG,
                                                   insertbackground=self.FG)
        self.text_area.pack(padx=10, pady=10)
        self.text_area.insert(tk.END, "Enter ingredients and click 'Find Recipes' to start.")
        self.text_area.config(state='disabled')

    # ----------------- SHOW DETAILED RECIPE -----------------
    def show_recipe(self, recipe, match_count):
        self.text_area.config(state='normal')
        self.text_area.delete(1.0, tk.END)

        # IMAGE
        img_path = f"images/{recipe['image_file']}"
        try:
            img = Image.open(img_path)
            img.thumbnail((250, 150))
            tk_img = ImageTk.PhotoImage(img)
            RecipeFinder.tk_image_ref = tk_img
            self.text_area.image_create(tk.END, image=tk_img)
            self.text_area.insert(tk.END, "\n")
        except:
            self.text_area.insert(tk.END, "[Image not found]\n")

        # RECIPE NAME
        self.text_area.insert(tk.END, f"\n{recipe['name'].upper()}\n", "dish_name")
        self.text_area.insert(tk.END, f"\nMatch Score: {match_count}\n\n", "header")

        # Ingredients
        self.text_area.insert(tk.END, "Ingredients:\n", "header")
        for ing in recipe['ingredients']:
            self.text_area.insert(tk.END, f" • {ing}\n")
        self.text_area.insert(tk.END, "\nProcess:\n", "header")
        self.text_area.insert(tk.END, f"{recipe['process']}\n")

        self.text_area.config(state='disabled')
        self.text_area.tag_configure("dish_name", font=("Arial", 20, "bold"), foreground=self.ACCENT_GREEN)
        self.text_area.tag_configure("header", font=("Arial", 12, "bold"), foreground=self.ACCENT_YELLOW)

    # ----------------- FIND RECIPES -----------------
    def find_recipes(self):
        user_input = self.entry.get().lower()
        ingredients = [i.strip() for i in user_input.split(",") if i.strip()]
        if not ingredients:
            messagebox.showinfo("Input Required", "Please enter at least one ingredient.")
            return

        matches = []
        for r in RECIPES:
            score = sum(1 for k in r["keywords"] if k in ingredients)
            if score > 0:
                matches.append({"recipe": r, "score": score})

        matches.sort(key=lambda x: x["score"], reverse=True)
        self.button_frame.destroy()
        self.button_frame = tk.Frame(self.master, bg=self.BG)
        self.button_frame.pack(pady=5, fill=tk.X)

        if not matches:
            tk.Label(self.button_frame, text="No recipes found.", fg=self.ACCENT_RED, bg=self.BG).pack()
            self.text_area.config(state='normal')
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "Try different ingredients.")
            self.text_area.config(state='disabled')
            return

        # Top 3 buttons
        for i, m in enumerate(matches[:3]):
            btn = tk.Button(self.button_frame, text=f"Rank {i+1}: {m['recipe']['name']} (Match {m['score']})",
                            font=("Arial", 10, "bold"), bg=self.ACCENT_GREEN, fg=self.BG,
                            command=lambda r=m['recipe'], s=m['score']: self.show_recipe(r, s))
            btn.pack(side=tk.LEFT, padx=5, pady=5)

# ----------------- 3. RUN APP -----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeFinder(root)
    root.mainloop()
