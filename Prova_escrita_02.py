# Exercici 1 (2 punts)
# Escriu una funció crear_sequencia(inici, final) que generi una llista amb tots els números des de inici fins a final (ambdós inclosos). Valida que inici i final siguin dos enters positius i inici sigui més petit que final, sinó és així retorna una llista buida.

def crear_sequencia(inici, final):
    if not isinstance(inici, int) or not isinstance(final, int):
        return []

    if inici < 0 or final < 0 or inici >= final:
        return []

    sequencia = []

    for num in range(inici, final + 1):
        sequencia.append(num)

    return sequencia

# Exercici 2 (2 punts)
# Crea una funció numeros_senars_majors(llista, limit) que retorni una nova llista amb només els números senars que siguin majors que limit. Valida que llista sigui una llista no buida i que limit sigui un número enter, sinó retorna una llista buida.

def numeros_senars_majors(llista, limit):
    if not isinstance(llista, list) or len(llista) == 0:
        return []

    if not isinstance(limit, int):
        return []

    resultat = []

    for num in llista:
        if num % 2 != 0 and num > limit:
            resultat.append(num)

    return resultat


# Exercici 3 (2 punts)
# Fes una funció primera_posicio(llista, element) que trobi la posició de la primera aparició d'un element a la llista. Si no existeix, ha de retornar -1. No pots utilitzar el mètode .index()

def primera_posicio(llista, element):
    for i in range(len(llista)):
        if llista[i] == element:
            return i

    return -1

# Exercici 4 (2 punts)
# Escriu una funció diagonal_principal(matriu) que retorni una llista amb els elements de la diagonal principal d'una matriu quadrada . Valida que matriu sigui una llista de llistes no buida, que totes les files tinguin la mateixa longitud i que sigui quadrada (mateix número de files i columnes), sinó retorna una llista buida.

def diagonal_principal(matriu):
    if not isinstance(matriu, list) or len(matriu) == 0:
        return []

    n = len(matriu)

    for fila in matriu:
        if not isinstance(fila, list):
            return []

        if len(fila) != n:
            return []

    diagonal = []

    for i in range(n):
        diagonal.append(matriu[i][i])

    return diagonal
