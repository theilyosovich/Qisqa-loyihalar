import random

import os
def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

clear_console()

words = [
# Hayvonot dunyosi (1–200)
"it","mushuk","ot","sigir","qo‘y","echki","tuya","eshak","bo‘ri","tulki",
"ayiq","yo‘lbars","sher","qoplon","fil","jirafa","zebra","maymun","gorilla","pingvin",
"burgut","lochin","qaldirg‘och","kabutar","qarg‘a","to‘ti","boyqush","turna","laylak","o‘rdak",
"g‘oz","tovuq","xo‘roz","kurka","ilon","kaltakesak","toshbaqa","qurbaqa","timsoh",
"akula","kit","delfin","baliq","sazan","laqqa","karp","forel","meduza","ahtapot",
"ari","asalari","kapalak","chumoli","qo‘ng‘iz","pashsha","chivin","o‘rgimchak",
"qisqichbaqa","chayon","otquloq","kirpi","quyon","sichqon","kalamush","olmaxon",
"kiyik","bug‘u","jayron","kenguru","panda","koala","begemot","nosorog",
"qoplonbaliq","ilvirs","tovusbaliq","ilonbaliq","morj","tyulen",
"yak","lama","alpaka","kalamushcha","tovonqush","qirg‘iy","tasqara",
"chittak","zarangqush","qoraqush","oqqush","qirg‘ovul","kaklik","bedana",
"ilonqush","suvilon","cho‘rtanbaliq","mo‘ylovli baliq","yulduzbaliq",
"qumoy","ko‘rshapalak","salamandra","triton","iguana","anakonda","piton",
"mantiya","dengiz oti","dengiz yulduzi","mollyuska","midya","ustritsa",
"chig‘anoq","qumchumchuq","qizilishton","kaptar","qumoyqush","tulkicha",
"bo‘richa","ayiqcha","kuchukcha","mushukcha","qulunchak","toycha",
"buzoq","qo‘zichoq","echkicha","jo‘ja","kurkachoq","iloncha","baliqcha",
"ariqurti","kapalakcha","chigirtka","o‘txo‘r","yirtqich","suvjonivori",
"quruqlikjonivori","parranda","sutemizuvchi","sudraluvchi","amfibiya",
"hasharot","yovvoyi","xonaki","noyob","qizilkitob"
,

# Atrof-muhit va tabiat (201–350)
"tabiat","o‘rmon","dasht","cho‘l","tog‘","vodiy","daryo","ko‘l","dengiz","okean",
"orol","qirg‘oq","sohil","buloq","ariq","kanal","sharshara","qoya","jarlik",
"g‘or","muzlik","qor","yomg‘ir","do‘l","shamol","bo‘ron","tuman","chaqmoq",
"momaqaldiroq","quyosh","oy","yulduz","sayyora","osmon","bulut","kamalak",
"tong","shafaq","kech","tun","sahro","voha","yaylov","ekinzor","bog‘",
"dala","maysa","o‘t","gul","lola","atirgul","rayhon","yalpiz","shuvoq",
"archa","qarag‘ay","terak","tol","chinor","eman","zarang","olma","anor",
"shaftoli","o‘rik","uzum","gilos","nok","banan","apelsin","limon","xurmo",
"anjir","kivi","pomidor","bodring","sabzi","kartoshka","piyoz","sarimsoq",
"qalampir","baqlajon","karam","ismaloq","salat","qovoq","tarvuz","qovun",
"iqlim","ekologiya","ifloslanish","tozalik","tabiatni_asrash","qayta_ishlash",
"energiya","quyosh_energiyasi","shamol_energiyasi","suv_energiyasi",
"resurs","zaxira","muvozanat","biosfera","atmosfera","gidrosfera",
"litosfera","flora","fauna","landshaft","eroziya","cho‘llanish"
,

# Sport (351–500)
"futbol","basketbol","voleybol","gandbol","tennis","stoltennis","badminton",
"xokkey","regbi","kriket","golf","beysbol","futzal","shaxmat","shashka",
"dzyudo","karate","taekvondo","boks","kurash","sambo","erkin_kurash",
"yunon_rum_kurashi","og‘ir_atletika","yengil_atletika","marafon","yugurish",
"saklash","uloqtirish","suzish","suv_polosı","sinxron_suzish","sakrash",
"gimnastika","akrobatika","fitnes","bodibilding","krossfit","yoga","pilates",
"velosport","mototsikl","avtosport","formula","karting","triathlon",
"pentatlon","ot_sporti","kamondan_otish","otish","biatlon","chang‘i",
"snoubord","figura_uchish","xokkey_maydoni","skeytbord","roller","alpinizm",
"tog‘ga_chiqish","parashyut","del­taplan","serfing","kayak","kanoye",
"eshkak_esish","armrestling","e_sport","kibersport","turnir","musobaqa",
"chempionat","liga","kubok","medal","oltin","kumush","bronza","hakem",
"murabbiy","jamoa","o‘yinchi","darvozabon","himoyachi","hujumchi",
"yarimhimoyachi","zaxira","transfer","taktika","strategiya","g‘alaba",
"mag‘lubiyat","durang"
,

# San’at va madaniyat (501–650)
"san’at","musiqa","rasm","haykaltaroshlik","me’morchilik","adabiyot",
"she’riyat","nasr","roman","hikoya","qissa","ertak","doston",
"maqola","esse","drama","komediya","tragediya","teatr","sahna",
"aktyor","aktrisa","rejissyor","ssenariy","rol","tomosha",
"kino","film","multfilm","serial","operator","montaj",
"animatsiya","grafika","dizayn","interyer","eksteryer",
"moda","uslub","libos","naqqoshlik","miniatyura",
"kulolchilik","zargarlik","kashtachilik","gilamdo‘zlik",
"do‘ppi","atlas","adras","chapan","so‘zana","maqom",
"shashmaqom","navo","ohang","ritm","melodiya",
"nota","cholg‘u","doira","dutor","tanbur","rubob",
"nay","karnay","surnay","pianino","gitara","skripka",
"baraban","saksofon","truba","konsert","festival",
"ko‘rgazma","muzey","galereya","madaniyat","meros",
"an’ana","urfodat","bayram","marosim","to‘y",
"nikoh","tug‘ilgan_kun","yubiley","sayil","tomosha",
"ijod","ilhom","iste’dod","mahorat","ustoz","shogird"
,

# Texnologiya va kundalik so‘zlar (651–1000)
"telefon","smartfon","kompyuter","noutbuk","planshet","klaviatura",
"sichqoncha","monitor","printer","skaner","internet","veb",
"sayt","ilova","dastur","kod","algoritm","ma’lumot","fayl",
"papka","server","bulut","xavfsizlik","parol","login",
"telegram","bot","kanal","guruh","xabar","emoji",
"email","video","audio","kamera","mikrofon",
"zaryad","batareya","quvvat","elektr","rozetka",
"lampochka","televizor","muzlatgich","kir_yuvish_mashinasi",
"konditsioner","pech","gaz","suv","choy","qahva",
"non","osh","palov","sho‘rva","lag‘mon","manti",
"somsa","kabob","shashlik","salat","shirinlik",
"tort","pishiriq","meva","sabzavot","nonushta",
"tushlik","kechki_ovqat","idish","qoshiq","vilka",
"pichoq","stakan","choynak","soat","kalendar",
"kun","hafta","oy","yil","vaqt","reja",
"ish","mehnat","dam","ta’til","sayohat",
"yo‘l","transport","avtobus","mashina","taksi",
"poyezd","samolyot","velosiped","metro","bekat",
"uy","xonadon","xona","eshik","deraza",
"stol","stul","karavot","shkaf","gilam",
"kitob","daftar","ruchka","qalam","o‘chirg‘ich",
"sumka","kiyim","poyabzal","ko‘ylak","shim",
"kurtka","palto","sharf","qalpoq","oyna",
"tabassum","do‘st","oila","ota","ona",
"aka","uka","opa","singil","farzand",
"baxt","orzu","maqsad","umid","sabr"
]


def get_word():
    word=random.choice(words)
    
    while "-" in word or " " in word:
        word=random.choice(words)
        
    return word.upper()
    
    
def display(user_letters, word):
    display_letters = ""
    for letter in word:
        if letter in user_letters:
            display_letters += letter
        else: 
            display_letters += "-"
    return display_letters
    
def play():
    word = get_word()
    word_letters = set(word)
    user_letters=set()
    urinishlar = 0
    
    print(f"\nMen {len(word)} xonali so'z o'yladim. Topa olasizmi?")
    
    while word_letters:
        print(display(user_letters, word))
        
        if user_letters:
            print(f"Shu vaqtgacha kiritgan xarflaringiz: {', '.join(sorted(user_letters))}")
        
        letter = input("\n🔤Xarf kiriting: ").upper().strip()
        
        if not letter.isalpha() or len(letter) != 1:
            print("❗ Iltimos, faqat bitta harf kiriting.\n")
            continue
        if letter in user_letters:
            print("⚠️Bu harfni oldin kiritgansiz! Boshqa harf kiriting.\n")
            continue
        user_letters.add(letter)
        urinishlar = urinishlar + 1
        
        if letter in word_letters:
            word_letters.remove(letter)
            print(f"✅ {letter} harfi to'g'ri!")
        else:
            print(f"❌ {letter} harfi bu so'zda yo'q.")
        user_letters.add(letter)
    print(f"\n🏆Tabriklayman {word} so'zini {urinishlar} urinishda topdingiz!\n")
    
play()
   
    
    
    