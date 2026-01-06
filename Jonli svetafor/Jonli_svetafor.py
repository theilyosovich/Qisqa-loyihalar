"""
Mavzu: Jonli svetafor

Amaliyot egasi: theilyosovich (Karim) 

Amaliyot sanasi: 2026-yil, 6-yanvar

GitHub profil: https://github.com/theilyosovich

"""

from colorama import Fore, init , Style
import time
import os

init(autoreset=True)

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def jonli_sanoq(matn, rang, soniya):
    for i in range(soniya, 0, -1):
        print(rang + f"{matn} ({i})", end="\r")
        time.sleep(1)
    print(" " * 50, end="\r")  
    #\r --> bu Carriage return. Qator boshiga o'tkazish buyrug'i
    
def svetaforni_boshqar(chiroq):
    clear()

    if chiroq == "Yashil":
        print("🟢",  
        "\n🔴",
        "\n🟡")
        jonli_sanoq("Oldinga harakatlanish mumkin!", Fore.GREEN + Style.BRIGHT , 5)

    elif chiroq == "Sariq":
        print("🟡",  
        "\n🟢",
        "\n🔴")
        jonli_sanoq("Tayyorlaning!", Fore.YELLOW + Style.BRIGHT, 3)

    elif chiroq == "Qizil":
        print("🔴",  
        "\n🟡",
        "\n🟢")
        jonli_sanoq("Harakatlanish mumkin emas!", Fore.RED + Style.BRIGHT, 5)

while True:
    svetaforni_boshqar("Yashil")
    svetaforni_boshqar("Sariq")
    svetaforni_boshqar("Qizil")
