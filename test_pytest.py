"""
Bateria de proves per a Prova_escrita_03.py

Tots els tests utilitzen pytest.mark.parametrize segons
els requisits de l'exercici.
"""

import pytest
import Prova_escrita_03


# =====================================================
# TESTS trobar_edat_maxima
# =====================================================

@pytest.mark.parametrize(
    "persones, resultat_esperat",
    [
        (
            [
                {"nom": "Anna", "edat": 25},
                {"nom": "Marc", "edat": 42},
                {"nom": "Jordi", "edat": 58},
            ],
            58,
        ),
        ([], -1),
        (
            [
                {"nom": "Anna", "edat": 25},
                {"nom": "Marc"},
            ],
            -1,
        ),
        (
            [
                {"nom": "Anna", "edat": 25},
                {"nom": "Marc", "edat": "42"},
            ],
            -1,
        ),
    ],
)
def test_trobar_edat_maxima(persones, resultat_esperat):
    """
    Comprova el comportament de trobar_edat_maxima
    amb dades vàlides i invàlides.

    Casos comprovats:
    - Llista correcta.
    - Llista buida.
    - Diccionaris incomplets.
    - Edats amb tipus incorrecte.
    """

    # Executem la funció
    resultat = Prova_escrita_03.trobar_edat_maxima(persones)

    # Verifiquem el resultat
    assert resultat == resultat_esperat


# =====================================================
# TESTS trobar_producte_mes_car
# =====================================================

@pytest.mark.parametrize(
    "llista_productes, resultat_esperat",
    [
        (
            [
                {"nom": "A", "preu": 100},
                {"nom": "B", "preu": 250},
                {"nom": "C", "preu": 50},
            ],
            {"nom": "B", "preu": 250},
        ),
        (
            [],
            None,
        ),
    ],
)
def test_trobar_producte_mes_car(llista_productes, resultat_esperat):
    """
    Comprova que es retorna el producte amb el
    preu més alt o None si la llista és buida.
    """

    # Modifiquem temporalment la variable global
    Prova_escrita_03.productes = llista_productes

    # Executem la funció
    resultat = Prova_escrita_03.trobar_producte_mes_car()

    # Verificació
    assert resultat == resultat_esperat


# =====================================================
# TESTS comptar_empleats_per_departament
# =====================================================

@pytest.mark.parametrize(
    "empresa, resultat_esperat",
    [
        (
            {
                "nom": "Empresa Test",
                "departaments": [
                    {
                        "nom": "IT",
                        "empleats": [
                            {"nom": "Anna"},
                            {"nom": "Marc"},
                            {"nom": "Jordi"},
                        ],
                    },
                    {
                        "nom": "RRHH",
                        "empleats": [
                            {"nom": "Laura"},
                        ],
                    },
                ],
            },
            {
                "IT": 3,
                "RRHH": 1,
            },
        ),
        (
            {
                "nom": "Empresa Buida",
                "departaments": [],
            },
            {},
        ),
    ],
)
def test_comptar_empleats_per_departament(empresa,resultat_esperat,):
    """
    Comprova que la funció retorna correctament
    el nombre d'empleats per departament.

    També es comprova el cas d'una empresa
    sense departaments.
    """

    # Executem la funció
    resultat = Prova_escrita_03.comptar_empleats_per_departament(empresa)

    # Verifiquem el resultat
    assert resultat == resultat_esperat