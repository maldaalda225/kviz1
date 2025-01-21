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
