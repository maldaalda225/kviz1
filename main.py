import tkinter as tk

# Funkce pro výpočet počtu písmen, slov a vět
def pocet():
    text = text_entry.get()  # Získání textu z textového pole
    pocet_pismen = sum(1 for char in text if char.isalpha())
    pocet_slov = len(text.split())
    pocet_vet = text.count(".") + text.count("!") + text.count('?')
    
    # Aktualizace textu v jednotlivých Label
    label_zadana_veta["text"] = f"Zadana veta: {text}"
    label_pocet_vet["text"] = f"Pocet vet: {pocet_vet}"
    label_pocet_slov["text"] = f"Pocet slov: {pocet_slov}"
    label_pocet_pismen["text"] = f"Pocet symbolu: {pocet_pismen}"

root = tk.Tk()

# Vstupní pole pro text
tk.Label(root, text="Zadejte větu: ").grid(row=0, column=0)
text_entry = tk.Entry(root)
text_entry.grid(row=0, column=1)

# Tlačítko pro výpočet
vysledek_button = tk.Button(root, text="Vypocitej", command=pocet)
vysledek_button.grid(row=1, column=1)

# Label pro zobrazení výsledků
label_zadana_veta = tk.Label(root, text="Zadana veta: ")
label_zadana_veta.grid(row=2, column=0)

label_pocet_vet = tk.Label(root, text="Pocet vet: ")
label_pocet_vet.grid(row=3, column=0)

label_pocet_slov = tk.Label(root, text="Pocet slov: ")
label_pocet_slov.grid(row=4, column=0)

label_pocet_pismen = tk.Label(root, text="Pocet symbolu: ")
label_pocet_pismen.grid(row=5, column=0)

# Spuštění hlavní smyčky aplikace
root.mainloop()
