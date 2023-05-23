# Importe le module pytest. pytest est une bibliothèque pour l'écriture de tests en Python.
import pytest


# Cette version de la fonction setup utilise le mot-clé 'yield' pour créer une fixture pytest.
# Cette fixture exécute le code avant le 'yield' avant chaque test, et le code après le 'yield' après chaque test.
# @pytest.fixture(scope="function") est un décorateur de pytest qui indique qu'une fonction doit être traitée comme une fixture.
# Une fixture est une fonction qui est exécutée avant (et parfois après) chaque test, et qui est utilisée pour configurer l'environnement de test.
# Dans ce cas, le paramètre 'scope="function"' signifie que la fixture doit être exécutée une fois pour chaque fonction de test individuelle.
@pytest.fixture(scope="module")
def setup():
    # Affiche le message "Ouvrir la BD" avant chaque test.
    print("Ouvrir la BD")
    yield
    # Affiche le message "Fermer la BD" après chaque test.
    print("Fermer la BD")

@pytest.fixture(scope="function")
def before():
    # Affiche le message "Ouvrir le navigateur" avant chaque test.
    print("Ouvrir le navigateur")
    yield
    # Affiche le message "Fermer le navigateur" après chaque test.
    print("Fermer le navigateur")

# Ceci est une fonction de test. Son nom commence par 'test_', donc pytest sait qu'il doit l'exécuter lorsqu'il exécute les tests.
# @pytest.mark.usefixtures("setup","before") est un décorateur pytest qui indique que les fixtures nommées "setup" et "before" doivent être appelées avant chaque test dans la fonction de test ou le module de test qui suit.
# Ces fixtures seront exécutées dans l'ordre où elles sont listées dans l'appel à usefixtures.
# Si ces fixtures retournent des données, ces données ne seront pas directement accessibles aux tests. Pour avoir accès aux données retournées par une fixture, vous devriez plutôt utiliser les arguments de la fonction de test.
@pytest.mark.usefixtures("setup","before")
def test_login():
    print("Ce connecter sur google")


# Une autre fonction de test. Cette fois, elle simule la création d'un compte Google.
@pytest.mark.usefixtures("setup","before")

def test_creation_Compte():
    print("Création d'un compte google")