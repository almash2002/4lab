''' 1.	Кіші және бас әріптерді қамтитын жол енгізіледі.
Бір жағдайда бірдей жолды шығару қажет,
ол қай әріптердің үлкенірек екеніне байланысты.
Егер тең болса, кіші әріпке түрлендіріңіз.
Мысалы, «HeLLo World» жолы енгізілсе,
оны «hello world» түрлендіру керек,
себебі бастапқы жолда кіші әріптер көбірек.
Кодыңызда for циклды пайдаланыңыз. upper()
(бас әріпті түрлендіру) және lower ()
(кіші әріпті түрлендіру), сонымен қатар жолдың
немесе таңбаның регистрін тексеретін isupper() және islower() әдістері.'''

string = str(input())
upper = 0
lower = 0
for i in string:
    if i.isupper():
        upper += 1
    else:
        lower += 1
if upper > lower:
    print(string.upper())
else:
    print(string.lower())