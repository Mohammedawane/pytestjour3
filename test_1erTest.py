#étape1: Installation du pytest: pip install pytest
#étape2: Création d'un fichier python en respectant les regles de nommage: test_.....
#étape3: Importer pytest

import pytest
#étape4: Creation des fonctions:
#$ pytest test_1erTest.py -s -v

def test_login():
    print("Ce connecter sur google:")

def test_creation_Compte():
        print("Création d'un compte google:")