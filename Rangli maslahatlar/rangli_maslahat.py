from colorama import Fore ,  Style , init # Back
import random
#   back orqa rangdan foydalanmaymiz, bu matn chiqish sifatini buzadi

maslahatlar = [
    "Har kuni o‘zingiz uchun yangi narsa o‘rganishga vaqt ajrating. Hatto kichik narsalar ham bilim doirangizni kengaytiradi va miyangizni faol holatda saqlaydi. Kitob o‘qing, maqolalar tahlil qiling va yangi ko‘nikmalarni sinab ko‘ring.",
    
    "Har kuni kamida 30 daqiqa jismoniy mashq qiling. Yugurish, yurish yoki oddiy cho‘zilishlar sizning organizmingizni sog‘lom qiladi, kayfiyatingizni ko‘taradi va stressni kamaytiradi.",
    
    "O‘zingizni samarali his qilish uchun kundalik rejalar tuzing. Muhim ishlarni birinchi qilishingiz, ortiqcha chalg‘ituvchi narsalarni kamaytirishingiz va maqsadga erishishingizga yordam beradi.",
    
    "Organizmingizni yaxshi ishlashi uchun sog‘lom ovqatlaning. Meva, sabzavot va oqsilga boy taomlar tanangizga energiya beradi, shirinlik va fastfoodni cheklash esa sog‘ligingizni saqlashga yordam beradi.",
    
    "Har kecha yetarli va sifatli uyqu oling. 7–8 soat uyqu tanangizni tiklaydi, kayfiyatingizni yaxshilaydi va aqliy ishlash qobiliyatingizni oshiradi. Dam olishni rejalashtiring va ekran oldida kechqurun vaqtni kamaytiring.",
    
    "Har kuni ijobiy fikrlarga e’tibor qarating. Salbiy fikrlarni tanqidiy baholang va ularni ijobiy imkoniyatlarga aylantiring. Bu stressni kamaytiradi va ruhiy sog‘ligingizni mustahkamlaydi.",
    
    "Hayotingizda kichik va katta maqsadlar belgilang. Ularni yozib chiqing va qadam-baqadam bajarishga harakat qiling. Maqsadga erishish sizga o‘z-o‘ziga ishonch beradi va motivatsiyani oshiradi.",
    
    "Oila va do‘stlar bilan vaqt o‘tkazing. Yaxshi suhbat, qo‘llab-quvvatlash va kulgi hayotingizni boyitadi. Yangi odamlar bilan tanishish va ijobiy aloqalar o‘rnatish ruhiy sog‘liqni mustahkamlaydi.",
    
    "Har kuni ijodiy bir narsa qilishga harakat qiling. Rasm chizish, yozish, musiqa chalish yoki hatto yangi retsept sinash aqliy qobiliyatingizni rivojlantiradi va ruhingizni ko‘taradi.",
    
    "O‘zingizni tanqid qiling va o‘sishga intiling. Har qanday xatolikni tajriba sifatida qabul qiling, yangi ko‘nikmalarni o‘rganing va har kuni bir oz yaxshilaning. Bu sizni muvaffaqiyatga yaqinlashtiradi."
]

init(autoreset=True) #  Xar bir printdan keyin ranglarni reset qilishi uchun, aks holda rang o'zgarmaydi.


fore_ranglar = [Fore.RED, Fore.BLUE, Fore.GREEN , Fore.MAGENTA, Fore.CYAN ]

stillar = [Style.BRIGHT , Style.DIM, Style.NORMAL, Style.RESET_ALL]

fore = random.choice(fore_ranglar)
stil = random.choice(stillar)
matn = random.choice(maslahatlar)

ism = input("""\nAssalomu aleykum foydalanuvchi, ismingiz nima?
>>> """)

print(f"""\n🙋{ism.upper()} tanishganimdan xursandman! 
👇Sizga quyidagi xayotingizni rang barang qiluvchi rangli tavsiyalarni bermoqchiman.\n""")

print(fore + stil + matn)


