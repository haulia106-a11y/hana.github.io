import tkinter as tk
from tkinter import messagebox
import random


def evaluate_reason(reason):
    reason = reason.lower()

    # ===== KATEGORI =====

    epic = [
        "burnout",
        "mental breakdown",
        "sakit",
        "demam",
        "rumah sakit",
        "kecelakaan",
        "darurat",
        "kematian",
        "kelahiran",
        "bencana",
        "kebakaran",
        "pertengkaran",
        "benci",
        "stres",
        "digigit ular",
        "ditabrak mobil"
    ]

    classic = [
        "capek",
        "lelah",
        "stress",
        "stres",
        "banyak tugas",
        "kurang tidur"
        "nangis",
        "mati listrik",
        "acara keluarga",
        "ibadah",
        "disuruh orang tua"
    ]

    minor = [
        "ketiduran",
        "mager",
        "malas",
        "rebahan",
        "menjaga adik",
        "baca novel",
        "makan"
    ]

    not_excuse = [
        "gak mau",
        "gamau",
        "ogah",
        "hewan melahirkan",
        "mau main",
        "diserang semut",
        "diculik alien",
        "kutukan kuno",
        "mencari jati diri",
        "bertapa",
        "lupa bernapas",
        "hibernasi",
        "misi rahasia",
        "wawancara hantu",
        "dikejar angsa",
        "sidang kucing",
        "mati gaya",
        "main game"
    ]

    # ===== MENENTUKAN KATEGORI =====

    if any(word in reason for word in epic):
        category = "Epic Suffering 💎"
        rate = 99

    elif any(word in reason for word in classic):
        category = "Classic Struggle ⭐"
        rate = 75

    elif any(word in reason for word in minor):
        category = "Minor Issue ☕"
        rate = 40

    elif any(word in reason for word in not_excuse):
        category = "Not an Excuse 🪨"
        rate = 5

    else:
        # Alasan random
        roll = random.randint(1, 100)

        if roll >= 80:
            category = "Epic Suffering 💎"
            rate = 99

        elif roll >= 50:
            category = "Classic Struggle ⭐"
            rate = 75

        elif roll >= 20:
            category = "Minor Issue ☕"
            rate = 40

        else:
            category = "Not an Excuse 🪨"
            rate = 5

    # ===== GACHA =====

    gacha = random.randint(1, 100)

    if gacha <= rate:

        if category == "Not an Excuse 🪨":
            result = (
                "🌌 Against All Odds\n"
                "Permission Granted."
            )

        else:
            result = (
                "✅ Permission Granted\n"
                "Take your break."
            )

    else:

        if category == "Epic Suffering 💎":
            result = (
                "💀 Lost the 99/1\n"
                "Permission Denied."
            )

        else:
            result = (
                "❌ Permission Denied"
            )

    return category, f"{rate}%", result


def submit():

    reason = entry_reason.get()

    if reason.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a reason first."
        )
        return

    category, probability, result = evaluate_reason(reason)

    label_category.config(
        text=f"Category: {category}"
    )

    label_probability.config(
        text=f"Acceptance Rate: {probability}"
    )

    label_result.config(
        text=result
    )


# ===== GUI =====

root = tk.Tk()

root.title("Nana")
root.geometry("500x600")
root.configure(bg="#F2E8D5")


title = tk.Label(
    root,
    text="Nana",
    font=("Georgia", 32, "bold"),
    bg="#F2E8D5",
    fg="#7C8554"
)
title.pack(pady=20)


subtitle = tk.Label(
    root,
    text="Permission to Pause",
    font=("Arial", 16),
    bg="#F2E8D5"
)
subtitle.pack()


label_input = tk.Label(
    root,
    text="Enter your reason:",
    bg="#F2E8D5"
)
label_input.pack(pady=10)


entry_reason = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
entry_reason.pack()


button = tk.Button(
    root,
    text="Ask Nana",
    command=submit,
    bg="#7C8554",
    fg="white"
)
button.pack(pady=20)


label_category = tk.Label(
    root,
    text="Category:",
    bg="#F2E8D5",
    font=("Arial", 12)
)
label_category.pack(pady=10)


label_probability = tk.Label(
    root,
    text="Acceptance Rate:",
    bg="#F2E8D5",
    font=("Arial", 12)
)
label_probability.pack(pady=10)


label_result = tk.Label(
    root,
    text="",
    bg="#F2E8D5",
    font=("Arial", 14),
    wraplength=350
)
label_result.pack(pady=20)


root.mainloop()