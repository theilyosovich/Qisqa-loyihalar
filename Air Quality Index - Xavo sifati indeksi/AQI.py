"""
Mavzu: Kiritilgan havo ifloslanish darajasi (AQI) bo‘yicha holatni aniqlash.

Amaliyot egasi: theilyosovich (Karim) 

Amaliyot sanasi: 2026-yil, 1-yanvar

GitHub profil: https://github.com/theilyosovich

"""

#Funksiya yozish qismi boshlandi

def air_quality_index(aqi):
    
    """Ushbu funksiya foydalanuvchidan xavo sifati indeksini (aqi) qabul qiladi va
    natijani string qilib qaytarib, xar bir xolat uchun tavsiyalar beradi."""
        
    if aqi < 0:
        return "Noto'g'ri qiymat kiritdingiz."
    
    if aqi <= 50:

        return """Yaxshi🟢
\nTavsiyalar:
    
🔹Tashqarida bemalol sayr qilish mumkin.

🔹Sport va jismoniy mashqlar uchun qulay.

🔹Derazalarni ochib xonani shamollatish mumkin.

🔹Maxsus ehtiyot chorasi talab qilinmaydi."""
        
    if 51 < aqi <=100:
        return """O'rtacha🟡
\nTavsiyalar:

🔹Ochiq havoda uzoq vaqt qolmaslik tavsiya etiladi.

🔹Bolalar va keksalar ehtiyot bo‘lsin.

🔹Yengil jismoniy mashqlar bilan cheklanish maqsadga muvofiq.

🔹Xonani qisqa muddat shamollatish mumkin."""
    
    if 101 < aqi <= 150:
        return """Sog'liq uchun zararli🟠
\nTavsiyalar:

🔹Ochiq havoda kamroq bo‘ling.

🔹Jismoniy faollikni kamaytiring.

🔹Nafas yo‘llari bilan bog‘liq muammosi borlar niqob taqsin.

🔹Derazalarni uzoq vaqt ochib qo‘ymaslik tavsiya etiladi."""
    
    if 151 < aqi <=200:
        return """Xavfli🔴
\nTavsiyalar:

🔹Imkon qadar uyda qoling.

🔹Ochiq havoda sport bilan shug‘ullanmang.

🔹Tibbiy niqob (yoki respirator) taqish tavsiya etiladi.

🔹Bolalar, keksalar va bemorlar tashqariga chiqmasin."""
    
    if aqi > 200:
        return """Xayot uchun xavfli💀
\nTavsiyalar:

🔹Tashqariga chiqish qat’iyan tavsiya etilmaydi.

🔹Derazalarni mahkam yoping.

🔹Havoni tozalovchi qurilmalardan foydalaning.

🔹Favqulodda holatlarda sog‘liqni saqlash tavsiyalariga amal qiling."""

#Funksiya yozish qismi tugadi

#Funksiyadan foydalanish qismi boshlandi

#Qiymat xatoligini oldini olish qismi boshlandi
while True:
    try:
        aqi_value=int(input("\n\nAQI qiymatini kiriting: "))
        break
    
    except ValueError:
        print("Xato! Iltimos, faqat son kiriting: ")
#Qiymat xatoligini oldini olish qismi tugadi

natija=air_quality_index(aqi_value)
print("\nHavo holati:" ,natija)


#Funksiyadan foydalanish qismi tugadi