import random
import sys
import json
import tkinter as tk
from tkinter import messagebox
from datetime import date
from pathlib import Path
from PIL import Image, ImageTk  

if getattr(sys, 'frozen', False):
    BASE_DIR = Path(sys._MEIPASS)
    SCRIPT_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).parent
    SCRIPT_DIR = BASE_DIR

DATA_FILE = SCRIPT_DIR / "heroes_data.json"
IMAGES_DIR = SCRIPT_DIR / "images"

if DATA_FILE.exists():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        Heroes = json.load(f)
else:
    Heroes = [
        {"name": "Adam Warlock", "is_lord": False, "lord_date": None},
        {"name": "Angela", "is_lord": False, "lord_date": None},
        {"name": "Black Cat", "is_lord": False, "lord_date": None},
        {"name": "Black Panther", "is_lord": False, "lord_date": None},
        {"name": "Black Widow", "is_lord": False, "lord_date": None},
        {"name": "Blade", "is_lord": False, "lord_date": None},
        {"name": "Bruce Banner", "is_lord": False, "lord_date": None},
        {"name": "Captain America", "is_lord": False, "lord_date": None},
        {"name": "Cloak & Dagger", "is_lord": False, "lord_date": None},
        {"name": "Cyclops", "is_lord": False, "lord_date": None},
        {"name": "Daredevil", "is_lord": False, "lord_date": None},
        {"name": "Devil Dinosaur", "is_lord": False, "lord_date": None},
        {"name": "Doctor Strange", "is_lord": False, "lord_date": None},
        {"name": "DpsPool", "is_lord": False, "lord_date": None},
        {"name": "Elsa Bloodstone", "is_lord": False, "lord_date": None},
        {"name": "Emma Frost", "is_lord": False, "lord_date": None},
        {"name": "Gambit", "is_lord": False, "lord_date": None},
        {"name": "Gorr The God Butcher", "is_lord": False, "lord_date": None},
        {"name": "Groot", "is_lord": False, "lord_date": None},
        {"name": "Hawkeye", "is_lord": False, "lord_date": None},
        {"name": "HealPool", "is_lord": False, "lord_date": None},
        {"name": "Hela", "is_lord": False, "lord_date": None},
        {"name": "Human Torch", "is_lord": False, "lord_date": None},
        {"name": "Invisible Woman", "is_lord": False, "lord_date": None},
        {"name": "Iron Fist", "is_lord": False, "lord_date": None},
        {"name": "Iron Man", "is_lord": False, "lord_date": None},
        {"name": "Jeff The Land Shark", "is_lord": False, "lord_date": None},
        {"name": "Jubilee", "is_lord": False, "lord_date": None},
        {"name": "Loki", "is_lord": False, "lord_date": None},
        {"name": "Luna Snow", "is_lord": False, "lord_date": None},
        {"name": "Magik", "is_lord": False, "lord_date": None},
        {"name": "Magneto", "is_lord": False, "lord_date": None},
        {"name": "Mantis", "is_lord": False, "lord_date": None},
        {"name": "Mister Fantastic", "is_lord": False, "lord_date": None},
        {"name": "Moon Knight", "is_lord": False, "lord_date": None},
        {"name": "Namor", "is_lord": False, "lord_date": None},
        {"name": "Peni Parker", "is_lord": False, "lord_date": None},
        {"name": "Phoenix", "is_lord": False, "lord_date": None},
        {"name": "Psylocke", "is_lord": False, "lord_date": None},
        {"name": "Rocket Raccoon", "is_lord": False, "lord_date": None},
        {"name": "Rogue", "is_lord": False, "lord_date": None},
        {"name": "Scarlet Witch", "is_lord": False, "lord_date": None},
        {"name": "Spider-Man", "is_lord": False, "lord_date": None},
        {"name": "Squirrel Girl", "is_lord": False, "lord_date": None},
        {"name": "Star-Lord", "is_lord": False, "lord_date": None},
        {"name": "Storm", "is_lord": False, "lord_date": None},
        {"name": "Tankpool", "is_lord": False, "lord_date": None},
        {"name": "The Hood", "is_lord": False, "lord_date": None},
        {"name": "The Punisher", "is_lord": False, "lord_date": None},
        {"name": "The Thing", "is_lord": False, "lord_date": None},
        {"name": "Thor", "is_lord": False, "lord_date": None},
        {"name": "Ultron", "is_lord": False, "lord_date": None},
        {"name": "Venom", "is_lord": False, "lord_date": None},
        {"name": "White Fox", "is_lord": False, "lord_date": None},
        {"name": "Winter Soldier", "is_lord": False, "lord_date": None},
        {"name": "Wolverine", "is_lord": False, "lord_date": None},
    ]

Chosen = random.choice(Heroes)

if Chosen["is_lord"]:
    image_name = f"{Chosen['name']}_Lord.png"
    status_text = f"{Chosen['name']} is already a LORD\n(achieved on {Chosen['lord_date']})"
else:
    image_name = f"{Chosen['name']}.png"
    status_text = f"{Chosen['name']} is not a Lord yet"

image_path = IMAGES_DIR / image_name

root = tk.Tk()
root.title("Marvel Rivals - Lord Checker")
root.resizable(False, False)

try:
    img = Image.open(image_path)

    if Chosen["name"] == "The Thing":
        img = img.resize((1920, 1080), Image.Resampling.LANCZOS)  # bigger size
    else:
        img = img.resize((700, 700), Image.Resampling.LANCZOS)    # normal size

    photo = ImageTk.PhotoImage(img)   # ← this must be outside the if/else

except Exception as e:
    messagebox.showerror("Error", f"Could not load image:\n{image_path}\n\n{e}")
    root.destroy()
    exit()

label_img = tk.Label(root, image=photo)
label_img.pack(padx=20, pady=10)

label_status = tk.Label(root, text=status_text, font=("Arial", 12))
label_status.pack(pady=5)

def make_lord():
    if Chosen["is_lord"]:
        messagebox.showinfo("Already Lord", f"{Chosen['name']} is already a Lord!")
        return

    Chosen["is_lord"] = True
    Chosen["lord_date"] = str(date.today())

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(Heroes, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Success", f"{Chosen['name']} is now a LORD!\nDate: {Chosen['lord_date']}")
    root.destroy()  

def close_window():
    root.destroy()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=15)

if not Chosen["is_lord"]:
    btn_yes = tk.Button(btn_frame, text="Make Lord (Y)", width=15, command=make_lord)
    btn_yes.pack(side="left", padx=10)

btn_no = tk.Button(btn_frame, text="Close", width=15, command=close_window)
btn_no.pack(side="left", padx=10)

root.mainloop()