from colorama import Fore ,Style,init #Back
#   back orqa rangdan foydalanmaymiz, bu matn chiqish sifatini buzadi
import random
import os
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

clear_console()


maslahatlar = [
    "\n🔹Har kuni o‘zingiz uchun yangi narsa o‘rganishga vaqt ajrating. \n🔹Hatto kichik narsalar ham bilim doirangizni kengaytiradi va miyangizni faol holatda saqlaydi. \n🔹Kitob o‘qing, maqolalar tahlil qiling va yangi ko‘nikmalarni sinab ko‘ring.",
    
    "\n🔹Har kuni kamida 30 daqiqa jismoniy mashq qiling. \n🔹Yugurish, yurish yoki oddiy cho‘zilishlar sizning organizmingizni sog‘lom qiladi, kayfiyatingizni ko‘taradi va stressni kamaytiradi.",
    
    "\n🔹O‘zingizni samarali his qilish uchun kundalik rejalar tuzing. \n🔹Muhim ishlarni birinchi qilishingiz, ortiqcha chalg‘ituvchi narsalarni kamaytirishingiz va maqsadga erishishingizga yordam beradi.",
    
    "\n🔹Organizmingizni yaxshi ishlashi uchun sog‘lom ovqatlaning. \n🔹Meva, sabzavot va oqsilga boy taomlar tanangizga energiya beradi, shirinlik va fastfoodni cheklash esa sog‘ligingizni saqlashga yordam beradi.",
    
    "\n🔹Har kecha yetarli va sifatli uyqu oling. \n🔹7–8 soat uyqu tanangizni tiklaydi, kayfiyatingizni yaxshilaydi va aqliy ishlash qobiliyatingizni oshiradi.\n🔹Dam olishni rejalashtiring va ekran oldida kechqurun vaqtni kamaytiring.",
    
    "\n🔹Har kuni ijobiy fikrlarga e’tibor qarating. \n🔹Salbiy fikrlarni tanqidiy baholang va ularni ijobiy imkoniyatlarga aylantiring.\n🔹Bu stressni kamaytiradi va ruhiy sog‘ligingizni mustahkamlaydi.",
    
    "\n🔹Hayotingizda kichik va katta maqsadlar belgilang.\n🔹Ularni yozib chiqing va qadam-baqadam bajarishga harakat qiling. \n🔹Maqsadga erishish sizga o‘z-o‘ziga ishonch beradi va motivatsiyani oshiradi.",
    
    "\n🔹Oila va do‘stlar bilan vaqt o‘tkazing.\n🔹Yaxshi suhbat, qo‘llab-quvvatlash va kulgi hayotingizni boyitadi.\n🔹Yangi odamlar bilan tanishish va ijobiy aloqalar o‘rnatish ruhiy sog‘liqni mustahkamlaydi.",
    
    "\n🔹Har kuni ijodiy bir narsa qilishga harakat qiling.\n🔹Rasm chizish, yozish, musiqa chalish yoki hatto yangi retsept sinash aqliy qobiliyatingizni rivojlantiradi va ruhingizni ko‘taradi.",
    
    "\n🔹O‘zingizni tanqid qiling va o‘sishga intiling.\n🔹Har qanday xatolikni tajriba sifatida qabul qiling, yangi ko‘nikmalarni o‘rganing va har kuni bir oz yaxshilaning. Bu sizni muvaffaqiyatga yaqinlashtiradi."
]

init(autoreset=True) #  Xar bir printdan keyin ranglarni reset qilishi uchun, aks holda rang o'zgarmaydi.


fore_ranglar = [Fore.RED, Fore.BLUE, Fore.GREEN , Fore.MAGENTA, Fore.CYAN ]

stillar = [Style.BRIGHT , Style.DIM, Style.NORMAL, Style.RESET_ALL]

fore = random.choice(fore_ranglar)
stil = random.choice(stillar)
matn = random.choice(maslahatlar)

ism = input("""\nAssalomu aleykum foydalanuvchi, mening ismim Karim. Sizning ismingiz nima?
>>> """)

print(f"""\n🙋{ism.upper()} tanishganimdan xursandman! 
👇Sizga quyidagi xayotingizni rang barang qiluvchi rangli tavsiyalarni bermoqchiman.\n""")

print(fore + stil + matn)
rangli_matn = Fore.BLUE + Style.BRIGHT + "Colorama" + Style.RESET_ALL


print(f"\nQuyidagi xavola orqali {rangli_matn} kutubxonasi haqida o'qib olishingiz mumkun!"
      
f"\nhttps://telegra.ph/Pythonda-Colorama-kutubxonasi-Konsolda-rangli-va-jonli-matnlar-01-04")




