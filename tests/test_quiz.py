from quiz.quiz import Quiz
import pytest
import json

def test_fichier_introuvable():
    # arrange
    filename = './tests/json/fichier_qui_n_existe_pas'
    # act
    quizApp = Quiz()
    try:
        quizApp.run(filename)
    # assert
    except FileNotFoundError:
        assert True
    else:
        assert False

def test_pas_un_json():
    # arrange
    filename = './tests/json/test_pas_un_json.json'
    # act
    quizApp = Quiz()
    try:
        quizApp.run(filename)
    # assert
    except json.decoder.JSONDecodeError:
        assert True
    else:
        assert False

def test_pas_le_bon_format():
    # arrange
    filename = './tests/json/test_pas_le_bon_format.json'
    # act
    quizApp = Quiz()
    try:
        quizApp.run(filename)
    # assert
    except Exception as e:
        if str(e) == 'Erreur le json n’est pas formaté correctement.':
            assert True
        else:
            assert False

def test_le_nombre_de_carte():
    # arrange
    filename = './tests/json/test_le_nombre_de_carte.json'
    # act
    quizApp = Quiz()
    quizApp.run(filename)
    count = quizApp.get_count_question()
    # assert
    assert count == 2

def test_question_correspond_reponse():
    # arrange
    filename = './tests/json/test_question_correspond_reponse.json'
    # act
    quizApp = Quiz()
    quizApp.run(filename)
    flashcards = quizApp.get_flashcards()
    # assert
    assert flashcards[0].get_recto() == 'recto1'
    assert flashcards[0].get_verso() == 'verso1'

    assert flashcards[1].get_recto() == 'recto2'
    assert flashcards[1].get_verso() == 'verso2'

    assert flashcards[2].get_recto() == 'recto3'
    assert flashcards[2].get_verso() == 'verso3'

def test_question_entiere():
    # arrange
    filename = './tests/json/test_question_entiere.json'
    # act
    quizApp = Quiz()
    quizApp.run(filename)
    flashcards = quizApp.get_flashcards()
    # assert
    assert flashcards[0].get_recto() == "Définit une interface pour la création d'objets dans une classe mère, mais délègue aux sous-classes le choix des types d'objets à créer."
    assert flashcards[0].get_verso() == 'Factory Method'

    assert flashcards[1].get_recto() == "Permet de créer des familles d'objets apparentés sans préciser leur classe concrète."
    assert flashcards[1].get_verso() == 'Abstract Factory'

    assert flashcards[2].get_recto() == "Permet de construire des objets complexes étape par étape. Ce patron permet de construire différentes variations ou représentations d'un objet en utilisant le même code de construction."
    assert flashcards[2].get_verso() == 'Builder'
