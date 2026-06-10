"""
Bateria de proves per als fitxers:
- prova_escrita01.py
- prova_escrita02.py
"""

import unittest

from Prova_escrita_01 import (
    buscar_per_titol,
    afegir_a_biblioteca,
    joc_mes_car,
    videojocs
)

from Prova_escrita_02 import (
    crear_sequencia,
    numeros_senars_majors,
    primera_posicio,
    diagonal_principal
)


class TestProvaEscrita01(unittest.TestCase):
    """
    Proves unitàries dels exercicis de prova_escrita01.py
    """

    def test_buscar_per_titol_existent(self):
        """
        Comprova que es retorna el videojoc correcte
        quan el títol existeix.
        """
        resultat = buscar_per_titol("Cyberpunk 2077", videojocs)

        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["genere"], "RPG")

    def test_buscar_per_titol_insensible_majuscules(self):
        """
        Comprova que la cerca no diferencia
        entre majúscules i minúscules.
        """
        resultat = buscar_per_titol("fifa 24", videojocs)

        self.assertIsNotNone(resultat)
        self.assertEqual(resultat["titol"], "FIFA 24")

    def test_buscar_per_titol_inexistent(self):
        """
        Comprova que retorna None si el joc no existeix.
        """
        resultat = buscar_per_titol("Minecraft", videojocs)

        self.assertIsNone(resultat)

    def test_afegir_a_biblioteca_correctament(self):
        """
        Comprova que un joc existent s'afegeix
        correctament a la biblioteca.
        """
        biblioteca = []

        resultat = afegir_a_biblioteca(
            "Cyberpunk 2077",
            videojocs,
            biblioteca
        )

        self.assertEqual(resultat, "✅ Joc afegit!")
        self.assertEqual(len(biblioteca), 1)

    def test_afegir_joc_duplicat(self):
        """
        Comprova que no es poden afegir
        jocs duplicats.
        """
        biblioteca = []

        afegir_a_biblioteca(
            "Cyberpunk 2077",
            videojocs,
            biblioteca
        )

        resultat = afegir_a_biblioteca(
            "Cyberpunk 2077",
            videojocs,
            biblioteca
        )

        self.assertEqual(
            resultat,
            "⚠️ Ja està a la biblioteca"
        )

    def test_afegir_joc_inexistent(self):
        """
        Comprova que es retorna el missatge
        adequat si el joc no existeix.
        """
        biblioteca = []

        resultat = afegir_a_biblioteca(
            "Minecraft",
            videojocs,
            biblioteca
        )

        self.assertEqual(
            resultat,
            "❌ Joc no trobat"
        )

    def test_joc_mes_car(self):
        """
        Comprova que es retorna el videojoc
        amb el preu més alt.
        """
        resultat = joc_mes_car(videojocs)

        self.assertEqual(resultat["titol"], "FIFA 24")
        self.assertEqual(resultat["preu"], 69.99)


class TestProvaEscrita02(unittest.TestCase):
    """
    Proves unitàries dels exercicis de prova_escrita02.py
    """

    def test_crear_sequencia_correcta(self):
        """
        Comprova la creació correcta
        d'una seqüència.
        """
        resultat = crear_sequencia(1, 5)

        self.assertEqual(
            resultat,
            [1, 2, 3, 4, 5]
        )

    def test_crear_sequencia_parametres_invalids(self):
        """
        Comprova que retorna una llista buida
        amb valors invàlids.
        """
        self.assertEqual(crear_sequencia(-1, 5), [])
        self.assertEqual(crear_sequencia(5, 1), [])
        self.assertEqual(crear_sequencia("1", 5), [])

    def test_numeros_senars_majors(self):
        """
        Comprova el filtratge de nombres
        senars majors que el límit.
        """
        resultat = numeros_senars_majors(
            [1, 2, 3, 4, 5, 6, 7],
            3
        )

        self.assertEqual(resultat, [5, 7])

    def test_numeros_senars_majors_invalid(self):
        """
        Comprova la validació dels paràmetres.
        """
        self.assertEqual(
            numeros_senars_majors([], 3),
            []
        )

        self.assertEqual(
            numeros_senars_majors([1, 2, 3], "3"),
            []
        )

    def test_primera_posicio_existent(self):
        """
        Comprova que es retorna la primera
        posició d'un element existent.
        """
        resultat = primera_posicio(
            [10, 20, 30, 20],
            20
        )

        self.assertEqual(resultat, 1)

    def test_primera_posicio_inexistent(self):
        """
        Comprova que retorna -1 quan
        l'element no existeix.
        """
        resultat = primera_posicio(
            [10, 20, 30],
            40
        )

        self.assertEqual(resultat, -1)

    def test_diagonal_principal_correcta(self):
        """
        Comprova l'obtenció correcta
        de la diagonal principal.
        """
        matriu = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]

        resultat = diagonal_principal(matriu)

        self.assertEqual(resultat, [1, 5, 9])

    def test_diagonal_principal_matriu_no_quadrada(self):
        """
        Comprova que retorna una llista buida
        si la matriu no és quadrada.
        """
        matriu = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]

        self.assertEqual(
            diagonal_principal(matriu),
            []
        )


if __name__ == "__main__":
    unittest.main()