"""Matemaatilised tehted"""
import math


# küsime kasutajalt ujuvkomaarvu kujul kolmnurga kaatetid a ja b

print("Mis on kaateti a ja b väärtused ujuvkomaarvudena?")
# koosta muutuja a, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

a = float(input("Sisesta kaatet a väärtus"))

# koosta muutuja b, lisa võimalus kasutajal sisestada arv, muuda see ujuvkomaarvuks

b = float(input("Sisesta kaatet b väärtus"))

# meie ülesandeks on leida hüpoteenus c, kolmnurga ümbermõõt ja pindala NB(vastused peavad olema ümardatud sajandikeni)

hupotenuus = round(math.sqrt(a ** 2 + b ** 2), 2)
print(f"Hüpotenuusi väärtus on c={hupotenuus}")

umbermoot = round((a + b + hupotenuus), 2)
print(f"Ümbermõõdu väärtus on P={umbermoot}")

pindala = round(((a * b) / 2), 2)
print(f"Pindala väärtus on S={pindala}")
