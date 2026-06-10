videojocs = [
    {
        "titol": "The Legend of Zelda",
        "any_llancament": 2017,
        "genere": "Aventura",
        "plataforma": "Nintendo Switch",
        "puntuacio": 9.7,
        "desenvolupador": {
            "nom": "Nintendo",
            "pais": "Japó"
        },
        "dlcs": ["Master Trials", "Champions' Ballad"],
        "preu": 59.99
    },
    {
        "titol": "Cyberpunk 2077",
        "any_llancament": 2020,
        "genere": "RPG",
        "plataforma": "PC",
        "puntuacio": 7.8,
        "desenvolupador": {
            "nom": "CD Projekt Red",
            "pais": "Polònia"
        },
        "dlcs": ["Phantom Liberty"],
        "preu": 29.99
    },
    {
        "titol": "FIFA 24",
        "any_llancament": 2023,
        "genere": "Esports",
        "plataforma": "PlayStation",
        "puntuacio": 8.2,
        "desenvolupador": {
            "nom": "EA Sports",
            "pais": "Estats Units"
        },
        "dlcs": [],
        "preu": 69.99
    }
]

biblioteca_personal = []


# Exercici 2: Funció de cerca(2, 5 punts)
# Escriu una funció que busqui un videojoc pel títol(insensible a majúscules) i el retorni(el diccionari).Si no el troba, retorna None.

def buscar_per_titol(titol, videojocs):
    for joc in videojocs:
        if joc["titol"].lower() == titol.lower():
            return joc
    return None


# Escriu aquí el teu codi (4-5 línies)


# Exercici 3: Gestió de biblioteca(3 punts)
# Escriu una funció afegir_a_biblioteca(titol, videojocs, biblioteca) que: Busqui el joc utilitzant buscar_per_títol() Si el joc no existeix, retorni "❌ Joc no trobat" Si el joc ja està a la biblioteca, retorni "⚠️ Ja està a la biblioteca" Si tot va bé, l'afegeixi i retorni "✅ Joc afegit!"


def afegir_a_biblioteca(titol, videojocs, biblioteca):
    joc = buscar_per_titol(titol, videojocs)

    if joc is None:
        return "❌ Joc no trobat"

    if joc in biblioteca:
        return "⚠️ Ja està a la biblioteca"

    biblioteca.append(joc)
    return "✅ Joc afegit!"


# Exercici4: Estadístiques(1, 5 punts)
# Escriu una funció joc_mes_car() que retorni el videojoc(diccionari) amb el preu més alt de la llista videojocs.


def joc_mes_car(videojocs):
    mes_car = videojocs[0]

    for joc in videojocs:
        if joc["preu"] > mes_car["preu"]:
            mes_car = joc

    return mes_car
