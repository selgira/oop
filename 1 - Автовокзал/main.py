import csv
from classes import Proizvoditel, Remont
import tkinter as tk
from tkinter import messagebox

# ----------------- Загрузка CSV -----------------
def load_proizvoditeli():
    proiz = {}
    with open("data/proizvoditeli.csv", newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            p = Proizvoditel(row[0], row[1])
            proiz[row[0]] = p.nazvanie
    return proiz

def load_remonty():
    remonty = []
    with open("data/remonty.csv", newline='', encoding='utf-8') as f:
        for row in csv.reader(f):
            r = Remont(*row)
            remonty.append(r)
    return remonty

# ----------------- Функции для заданий -----------------
def spisok_nevipolnennykh(remonty):
    nevip = [r for r in remonty if r.data_isp == ""]
    with open("data/nevipolnennye.txt", "w", encoding='utf-8') as f:
        for r in nevip:
            f.write(str(r) + "\n")
    print("Список невыполненных ремонтов записан в nevipolnennye.txt")

def tablica_sravneniya(remonty, proiz):
    counts = {}
    for r in remonty:
        if r.kod_kategorii == "2":  # 2 = Сложный ремонт
            counts[r.kod_tehniki] = counts.get(r.kod_tehniki, 0) + 1
    with open("data/sravnenie.txt", "w", encoding='utf-8') as f:
        for kod, kol in counts.items():
            f.write(f"{proiz.get(kod, 'Неизвестно')}: {kol}\n")
    print("Сравнительная таблица сложных ремонтов записана в sravnenie.txt")

# ----------------- Главное меню консоли -----------------
def main():
    proiz = load_proizvoditeli()
    remonty = load_remonty()

    while True:
        print("\n1. Список невыполненных ремонтов")
        print("2. Сравнительная таблица сложных ремонтов")
        print("0. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            spisok_nevipolnennykh(remonty)
        elif choice == "2":
            tablica_sravneniya(remonty, proiz)
        elif choice == "0":
            break
        else:
            print("Неверный выбор")

# ----------------- Простая визуалка Tkinter -----------------
def gui():
    proiz = load_proizvoditeli()
    remonty = load_remonty()
    
    root = tk.Tk()
    root.title("Гарантийная мастерская")

    def nevip():
        spisok_nevipolnennykh(remonty)
        messagebox.showinfo("Готово", "Список невыполненных ремонтов создан")

    def sravn():
        tablica_sravneniya(remonty, proiz)
        messagebox.showinfo("Готово", "Сравнительная таблица создана")

    tk.Button(root, text="Невыполненные ремонты", command=nevip).pack(pady=5)
    tk.Button(root, text="Сравнение сложных ремонтов", command=sravn).pack(pady=5)
    tk.Button(root, text="Выход", command=root.destroy).pack(pady=5)

    root.mainloop()

# ----------------- Запуск -----------------
if __name__ == "__main__":
    # main()       # Раскомментируй, если хочешь консольное меню
    gui()          # Раскомментируй, если хочешь визуальное меню
