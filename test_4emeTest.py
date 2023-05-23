#$ pytest test_4emeTest.py -s -v -k "not login" (exclure un text)



import pytest



def test_login():
    print("Ce connecter sur google")

def test_creation_Compte():
    print("Création d'un compte google")