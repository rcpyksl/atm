database={
    "ali":{

        "account":1000,
        "credit":200

          },

    "veli":{

        "account":2000,
        "credit":500

           },

    "deli":{

        "account":3000,
        "credit":0

           }
         }


def finduser():

    password=int(input("password: "))

    if password == 1:
        kull = "ali"
        print("--------Ali bey hoşgeldiniz------")
        print("--------hesap bilgileriniz-------")
        print("Bakiyeniz      : ", database[kull]["account"])
        print("kart borcunuz  : ", database[kull]["credit"])
        return kull

    elif password ==2:

        kull = "veli"
        print("--------veli bey hoşgeldiniz------")
        print("--------hesap bilgileriniz--------")
        print("Bakiyeniz      : ", database[kull]["account"])
        print("kart borcunuz  : ", database[kull]["credit"])
        return kull

    elif password == 3:
        kull = "deli"
        print("--------deli bey hoşgeldiniz------")
        print("--------hesap bilgileriniz--------")
        print("Bakiyeniz      : ", database[kull]["account"])
        print("kart borcunuz  : ", database[kull]["credit"])
        return kull

    else:
        print("yanlış şifre")
        return False
        

x = finduser()

#işlemler
if x is not False:
    print("\n-------- işlem seçiniz------------")
    islem=int(input(" 1:para yatır \n 2:para çek \n 3:kredi kartı borç öde \n 4:nakit avans çek \n 5:para transferi  \n ==>"))
else:
    exit()

def pay():

    pymiktar=int(input("yatıralacak para miktarı : "))
    yb = database[x]["account"] + pymiktar
    print("yeni bakiye : ", yb)

def pac():

    pymiktar=int(input("çekilecek para miktarı : "))
    if pymiktar > database[x]["account"]:
        print("bakiye yetersiz: ", database[x]["account"])

    else:
        yb = database[x]["account"] - pymiktar
        print("yeni bakiye : ", yb)

def kkbö():

    pymiktar=int(input("ödenecek para miktarı : "))
    if pymiktar > database[x]["account"]:
        print("bakiye yetersiz: ", database[x]["account"])
    else:
        yb = database[x]["account"] - pymiktar
        kkb = database[x]["credit"] - pymiktar
        print("yeni bakiye : ", yb, "\n kalan kart borcu: ", kkb)

def na():

    pymiktar=int(input("avans para miktarı : "))
    kkb = database[x]["credit"] + pymiktar
    print("kart borcu : ", kkb)
        

def pt():

    pymiktar=int(input("transfer miktarı : "))
    if pymiktar > database[x]["account"]:
        print("bakiye yetersiz : ", database[x]["account"])
    else:
        kime=input("kime : ")
        yb = database[x]["account"] - pymiktar
        print("yeni bakiye : ", yb)
        print(kime, "'nin yeni bakiyesi : ", database[kime]["account"]+pymiktar)

if islem == 1:
    pay()

if islem == 2:
    pac()

if islem == 3:
    kkbö()

if islem == 4:
    na()

if islem == 5:
    pt()