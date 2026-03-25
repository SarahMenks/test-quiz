import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

# --- Commit 2: 10 more tests ---
def test_create_multiple_choices():
    question = Question(title='q1')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    choice3 = question.add_choice('c', False)
    assert len(question.choices) == 3

def test_create_choice_with_empty_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('', False)

def test_remove_choice_by_id():
    question = Question(title='q1')
    choice = question.add_choice('a', False)
    question.remove_choice_by_id(choice.id)
    assert len(question.choices) == 0

def test_remove_choice_with_invalid_id():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.remove_choice_by_id('invalid_id')

def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question(title='q1', points=0)
    with pytest.raises(Exception):
        Question(title='q1', points=101)
    with pytest.raises(Exception):
        Question(title='q1', points=-1)

def test_create_choice_with_invalid_text():
    question = Question(title='q1')
    with pytest.raises(Exception):
        question.add_choice('a'*101, False)
    with pytest.raises(Exception):
        question.add_choice('', False)

def test_create_choice_with_valid_text():
    question = Question(title='q1')
    choice = question.add_choice('a'*99, False)
    assert choice.text == 'a'*99

def test_remove_all_choices():
    question = Question(title='q1')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', True)
    question.remove_all_choices()
    assert len(question.choices) == 0

def test_set_correct_choices():
    question = Question(title='q1')
    choice1 = question.add_choice('a', False)
    choice2 = question.add_choice('b', False)
    question.set_correct_choices([choice1.id])
    assert choice1.is_correct
    assert not choice2.is_correct

def test_set_correct_choices_with_invalid_id():
    question = Question(title='q1')
    choice1 = question.add_choice('a', False)
    with pytest.raises(Exception):
        question.set_correct_choices(['b'])
