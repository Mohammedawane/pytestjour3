# Importe le module pytest. pytest est une bibliothèque pour l'écriture de tests en Python.
import pytest

# La fonction setup_module est exécutée une fois avant le début de l'exécution de tous les tests dans un module de test.
def setup_module(module):
    print("Ouvrir la BD")
#Elle est exécutée une fois après l'achèvement de tous les tests dans un module de test.
def teardown_module(module):
    print("Fermer la BD")


# La fonction setup_function est une fonction spéciale reconnue par pytest. Elle sera exécutée avant chaque fonction de test.
def setup_function(function):
    print("Ouvrir le navigateur")

# La fonction teardown_function est une autre fonction spéciale reconnue par pytest. Elle sera exécutée après chaque fonction de test.
def teardown_function(function):
    print("Fermer le navigateur")

# Ceci est une fonction de test. Son nom commence par 'test_', donc pytest sait qu'il doit l'exécuter lorsqu'il exécute les tests.
def test_login():
    print("Ce connecter sur google")

# Une autre fonction de test. Cette fois, elle simule la création d'un compte Google.
def test_creation_Compte():
    print("Création d'un compte google")