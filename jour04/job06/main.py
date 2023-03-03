from voiture import Voiture
from moto import Moto

mercedes = Voiture("Mercedes","Classe A",2020,18500)
mercedes.infoVehicule()
print("\n")
yamaha = Moto("Yahama","1200 Vmax",1987,4500)
yamaha.infoVehicule()
print("\n")
mercedes.demarrer()
print("\n")
yamaha.demarrer()


