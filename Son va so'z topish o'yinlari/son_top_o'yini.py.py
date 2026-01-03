import random
import math
import os
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

clear_console()
def son_top(x):
    tasodifiy_son = random.randint(1, x)
    print(f"\n Men 1 dan {x} gacha oraliqda son o‘yladim.")
    print("👉 Uni topishga harakat qiling!\n")

    taxminlar = 0

    while True:
        taxmin = input("🔢 Taxminni kiriting: ").strip()

        if not taxmin.isdigit():
            print("❗ Iltimos, faqat son kiriting.\n")
            continue

        taxmin = int(taxmin)
        taxminlar += 1

        if taxmin < tasodifiy_son:
            print("⬆️ Kattaroq son ayting.\n")
        elif taxmin > tasodifiy_son:
            print("⬇️ Kichikroq son ayting.\n")
        else:
            print("✅ To‘g‘ri topdingiz!\n")
            break

    print(f"🎉 Tabriklayman! Siz {taxminlar} ta urinishda topdingiz.\n")
    return taxminlar


def son_top_bot(x):
    urinish = math.ceil(math.log2(x))

    input(
        f"\n🤖 1 dan {x} gacha istalgan son o‘ylang.\n"
        f" Men uni eng ko‘pi bilan {urinish} ta urinishda topaman.\n"
        f"➡️ Tayyor bo‘lsangiz Enter bosing..."
    )

    quyi = 1
    yuqori = x
    taxminlar = 0

    print("\n🚀 Boshladik!\n")

    while True:
        taxminlar += 1
        taxmin = (quyi + yuqori) // 2

        javob = input(
            f"❓ Siz {taxmin} sonini o‘yladingizmi?\n"
            f"👉 Kattaroq bo‘lsa (+), kichikroq bo‘lsa (-), to‘g‘ri bo‘lsa (t): "
        ).strip().lower()

        if javob == "+":
            quyi = taxmin + 1
        elif javob == "-":
            yuqori = taxmin - 1
        elif javob == "t":
            print("\n✅ Ajoyib! Topdim!")
            break
        else:
            print("❗ Noto‘g‘ri belgi. Faqat +, - yoki t kiriting.\n")
            taxminlar -= 1  # noto‘g‘ri javob urinishga sanalmaydi

    print(f"🤖 Men {taxminlar} ta urinishda topdim!\n")
    return taxminlar


def play(x):
    while True:
        clear_console()
        print("\n==============================")
        print("🎮 SON TOPISH O‘YINI")
        print("==============================")

        taxminlar_bot = son_top_bot(x)
        taxminlar_user = son_top(x)

        if taxminlar_bot < taxminlar_user:
            print(f"🤖 Men yutdim! ({taxminlar_bot} < {taxminlar_user})\n")
        elif taxminlar_bot > taxminlar_user:
            print(f"🏆 Siz yutdingiz! ({taxminlar_user} < {taxminlar_bot})\n")
        else:
            print("⚖️ Durrang! Kuchlar teng.\n")

        yana = input("🔁 Yana o‘ynaysizmi? [1 = Ha / 0 = Yo‘q]: ").strip()
        if yana != "1":
            print("\n👋 O‘yin tugadi. Rahmat!")
            break


play(int(input("\n1 dan X gacha bo'lgan oraliqda o'ynaymiz. X ni kiriting: ")))

