"""
Mavzu: Mini bank hisob raqami tizimi

Amaliyot egasi: theilyosovich (Karim) 

Amaliyot sanasi: 2026-yil, 2-yanvar

GitHub profil: https://github.com/theilyosovich

"""
# Consoledagi ma'lumotlarni tozalash kodi yozishni boshladni
import os

def clear_console(): 
    os.system('cls')
clear_console( )
# Consoledagi ma'lumotlarni tozalash kodi yozishni tugadi.

xaqiqiy_hisob_raqam=123123123
balance=0
history=[]
    

print("""\nBank tizimiga xush kelibsiz!""")

#   Hisob raqamini tasdiqlash qismi boshlandi
def Hisob_raqamni_tasdiqlash(haqiqiy_raqam):
   
    while True:
        kiritish=input("\nShaxsiy hisob raqamingizni kiriting: ")
        
        if not kiritish:     # 1-Tekshiruv
            print("\nKechirasiz, hisob raqam bo'sh bo'lmasligi kerak. Qaytadan urinib ko'ring.")
            continue
        
        try:    # 2-Tekshiruv
            hisob_raqam_kiritish = int(kiritish)
            
        except ValueError:
            print("\nXato! Hisob raqami faqat sonlardan iborat bo'lishi kerak! Qaytadan urinib ko'ring. ")
            continue
        
        if hisob_raqam_kiritish == haqiqiy_raqam:     # 3-Tekshiruv
            print("\nTizimga muvaffaqqiyatli kirdingiz!")
            return hisob_raqam_kiritish
        else:
            print(f"\nKechirasiz, \"{hisob_raqam_kiritish}\" hisob raqami aniqlanmadi. Qaytadan urinib ko'ring.")
#   Hisob raqamini tasdiqlash qismi tugadi

#Balansni ko'rsatish qismi boshlandi
def balansni_tekshir():
    """Hisob raqamning joriy balansini ko'rsatadi"""
    global balance
    print(f"\n\n💰Sizning xozirgi balansingiz – {balance} so'm")
#Balansni ko'rsatish qismi tugadi

#Hisobga pul qo'shish qismi boshlandi
def pul_kirit():
    """Hisob raqamga pul kiritadi"""
    global balance, history
    
    while True:
        try:
            miqdor=int(input("\nQo'shmoqchi bo'lgan pul miqdorini kiriting: "))
            
            if miqdor <=0:
                print("\nNoto'g'ri miqdor. Musbat son kiriting.")
                continue
            break
        except ValueError:
            print("\nNoto'g'ri format: Iltimos, faqat son kiriting! ")
    balance=balance + miqdor
    history.append({"turi":"KIRIM","miqdor":miqdor})
    print(f"\n✅Balansingizga {miqdor} muvaffaqqiyatli qo'shildi. Joriy balans: {balance} so'm")
#Hisobga pul qo'shish qismi tugadi

#Hisobdan pul chiqarish qismi boshlandi
def pul_chiqar():
    """Hisob raqamdan pul yechadi"""
    global balance, history
    
    while True:
       try:
           miqdor=int(input("\nChiqarib bo'lgan miqdoringizni kiriting: "))
           if miqdor <= 0:
               print("\nNoto'g'ri miqdor. Musbat son kiriting: ")
               continue
           
      
           if miqdor > balance:
               print(f"\nBalansingizda yetarlicha mablag' yo'q. Mavjud balans: {balance}")
               continue
           
           balance=balance - miqdor
           history.append({"turi":"CHIQIM","miqdor":miqdor})
           print(f"\n✅Balansingizdan {miqdor} so'm yechildi. Joriy balans: {balance}")
           break
       except ValueError:
           print("\nNoto'g'ri format.Iltimos faqat son kiriting: ")
#Hisobdan pul chiqarish qismi tugadi

#Amaliyot tarixini ko'rish qismi boshlandi
def amaliyotlar_tarixini_tekshir():
    """Hisob raqam ustida bajarilgan barcha amallar tarixini ko'rsatadi."""
    global history
    print("\nAmaliyotlar tarixi:")

    if not history:
        print("\nXali xech qanday amallar bajarilmadi.")
        return
    for qism in history:
        turi=qism['turi']
        miqdor=qism['miqdor']
        
        if turi == "KIRIM":
            print(f"  ➕ Pul kirdi: ={miqdor} so'm")
        elif turi == "CHIQIM":
            print(f"  ➖ Pul chiqdi: ={miqdor} so'm")
    print(f"Joriy balans: {balance} so'm")
#Amaliyot tarixini ko'rish qismi tugadi

#Tizimdan chiqish qismi boshlandi
def chiqish():
    """Tizimdan chiqish so'rovini amalga oshiradi"""
    print("\n\nTizimdan chiqish so'rov qabul qilindi. Foydalanganingiz uchun tashakkur!")
#Tizimdan chiqish qismi tugadi

#Asosiy menyu qismi boshlandi
def asosiy_menyu():
    """Asosiy menyuni ko'rsatadi va foydalanuvchi tanloviga qarab funksiyalarni chaqiradi"""
    
    tasdiqlangan_hisob = Hisob_raqamni_tasdiqlash(xaqiqiy_hisob_raqam)
    
    while True:
        clear_console()
        print("""
              ASOSIY MENYU
              
1. Balansni ko'rish
2. Hisobga pul qo'shish
3. Hisobdan pul chiqarish
4. Amaliyotlar tarixini ko'rish
5. Tizimdan chiqish""")

        tanlov=input("\nAmaliyotni tanlang (1-5) : ")
        if tanlov == "1":
            balansni_tekshir()
        elif tanlov == "2":
            pul_kirit()
        elif tanlov == "3":
            pul_chiqar()
        elif tanlov == "4":
            amaliyotlar_tarixini_tekshir()
        elif tanlov == "5":
            chiqish()
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, 1-5 gacha tanlovni tanlang.")
#Asosiy menyu qismi tugadi

if __name__ == "__main__":
    asosiy_menyu()
"""Bu qator dasturni faqat to'g'ridan-to'g'ri ishga tushirilsa ishlaydi. Dastur qaysi qismdan boshlashini aytamiz."""


           
        
           
    



    
    