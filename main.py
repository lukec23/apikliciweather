import requests

koordinate = [
    {"ime": "Ljubljana", "lat": 46.05, "lon": 14.51},
    {"ime": "London", "lat": 51.51, "lon": -0.13},
    {"ime": "New York", "lat": 40.71, "lon": -74.01},
    {"ime": "Tokyo", "lat": 35.68, "lon": 139.69},
    {"ime": "Sydney", "lat": -33.87, "lon": 151.21},
    {"ime": "Kairo", "lat": 30.04, "lon": 31.24},
    {"ime": "São Paulo", "lat": -23.55, "lon": -46.63},
    {"ime": "Mumbai", "lat": 19.08, "lon": 72.88}
]

# 1: Poišči mesto z najvišjo maksimalno temperaturo v naslednjih 7 dneh
# Namig: Uporabi max() na ["daily"]["temperature_2m_max"]
"""
max_tmp=0
max_temp_mesto=""
for k in koordinate:
    url=f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=temperature_2m_max&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    max_temp=max(call["daily"]["temperature_2m_max"])

    if max_temp > max_tmp:
        max_tmp=max_temp
        max_temp_mesto=k["ime"]
print(max_temp_mesto,max_tmp)
"""
# 2: Katero mesto bo imelo največ padavin skupaj v naslednjih 7 dneh?
# Namig: Seštej vse vrednosti v ["daily"]["precipitation_sum"]
"""
a=0
max_padavin_mesto=""
for k in koordinate:
    url= f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=precipitation_sum&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    temp=sum(call["daily"]["precipitation_sum"])

    if temp>a:
        a=temp
        max_padavin_mesto=k["ime"]
print(max_padavin_mesto,a)
"""
# 3: Najdi najhladneje mesto v naslednjih 7 dneh
# Namig: Nekatera mesta lahko nimajo podatkov, preveri dolžino seznama!
"""
najhladnej=0
najhladnej_mesto=""
for k in koordinate:
    url=f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=temperature_2m_min&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    m=min(call["daily"]["temperature_2m_min"])

    if m<najhladnej:
        najhladnej=m
        najhladnej_mesto=k["ime"]
print(najhladnej_mesto,najhladnej)
"""
# 4: Poišči mesto z največjim temperaturnim razponom (max - min) za prvi dan
# Namig: Uporabi indeks [0] za prvi dan napovedi
"""
razpon_max=0
mesto=""
for k in koordinate:
    url=f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=temperature_2m_min,temperature_2m_max&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    velik=call["daily"]["temperature_2m_max"][0]
    mal=call["daily"]["temperature_2m_min"][0]

    if velik-mal>razpon_max:
        razpon_max=velik-mal
        mesto=k["ime"]
print(razpon_max,mesto)
"""
# 5: Izpiši vsa mesta, kjer bo jutri padalo (precipitation_sum[1] > 0)
# Namig: Jutri je na indeksu [1], danes je [0]
"""
mesto=[]
for k in koordinate:
    url=f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=precipitation_sum&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    pada=call["daily"]["precipitation_sum"][1]

    if pada > 0:
        mesto.append(k["ime"])
print(mesto)"""
# 6: Koliko mest bo imelo jutri maksimalno temperaturo nad 20°C?
# Namig: Preštej mesta, kjer je temperature_2m_max[1] > 20
mesto=[]
for k in koordinate:
    url=f"https://api.open-meteo.com/v1/forecast?latitude={k["lat"]}&longitude={k["lon"]}&daily=temperature_2m_max&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    v=call["daily"]["temperature_2m_max"][1]

    if v > 20:
        mesto.append(k["ime"])
print(mesto)

# 7: Katero mesto ima najhitrejši veter v naslednjih 7 dneh? Izpiši tudi hitrost vetra.
# Namig: Preveri max() vrednost v ["daily"]["wind_speed_10m_max"]

# 8: V katerem mestu je najdaljši dan (razlika med zahodom in vzhodom sonca)?
# Namig: Uporabi DateTime https://www.w3schools.com/python/python_datetime.asp

# 9: Ugotovi, koliko mest bo  v naslednjih 7 dneh brez padavin
# Namig: Preveri, če ima mesto vsaj eno ničlo v precipitation_sum

# 10: Poljubna naloga!
