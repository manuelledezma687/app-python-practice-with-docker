import random
from fastapi import FastAPI


app = FastAPI()

@app.get("/breakfast")
def get_breakfast():
    Fruits = ["Frutillas cortadas","Naranjas","1 o 2 Manzanas","Kiwi","1 Banana","Porción de Papaya","Porción de Pera"]
    Proteins = ["Panqueques","Galletas con Mermelada o Queso crema","1 Arepa","Huevos revueltos","Homelet con Vegetables","Sandwich de Jamón y queso","Huevo cocido"]
    drinks = ["Café","Mate","Yogurt"]
    return "Su Desayuno: " + random.choice(Fruits) +", " + random.choice(Proteins) +" y "+ random.choice(drinks)
