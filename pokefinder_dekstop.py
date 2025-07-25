import tkinter as tk
import requests

window = tk.Tk()
window.title("Pokémon Finder")
window.geometry("800x600")

# Title Label
lab = tk.Label(window, text="Pokémon Finder", font=("Arial", 16, "bold"))
lab.pack(pady=5)

# Entry Box
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

# Result Label
result_label = tk.Label(window, text="", wraplength=280, font=("Arial", 10), justify="left")
result_label.pack(pady=10)

# Button Action
def on_click():
    user = entry.get().lower().strip()

    url = f"https://pokeapi.co/api/v2/pokemon/{user}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        name = data['name'].title()
        poke_id = data['id']
        types = [t['type']['name'] for t in data['types']]
        abilities = [a['ability']['name'] for a in data['abilities']]
        height = data['height'] / 10  # in meters
        weight = data['weight'] / 10  # in kilograms
        base_exp = data['base_experience']

        result = (
            f"ID: {poke_id}\n"
            f"Name: {name}\n"
            f"Types: {', '.join(types)}\n"
            f"Abilities: {', '.join(abilities)}\n"
            f"Height: {height} m\n"
            f"Weight: {weight} kg\n"
            f"Base Experience: {base_exp}"
        )
    else:
        result = "Pokémon not found. Try a different name or ID."

    result_label.config(text=result)

# Button
translate_btn = tk.Button(window, text="Find Pokémon", command=on_click)
translate_btn.pack(pady=5)

window.mainloop()