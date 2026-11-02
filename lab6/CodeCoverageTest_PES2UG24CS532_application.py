
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------- GAME SCORE TESTS ----------------

def test_negative_points():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_basic_game_scores():
    assert game_score(0, 0) == "0-0"
    assert game_score(1, 0) == "15-0"
    assert game_score(2, 1) == "30-15"


def test_deuce():
    assert game_score(3, 3) == "deuce"


def test_game_winner_a():
    assert game_score(5, 3) == "game A"
    assert game_score(4, 0) == "game A"


def test_game_winner_b():
    assert game_score(3, 5) == "game B"
    assert game_score(0, 4) == "game B"


def test_advantage_a():
    assert game_score(4, 3) == "advantage A"


def test_advantage_b():
    assert game_score(3, 4) == "advantage B"


# ---------------- SET WINNER TESTS ----------------

def test_set_winner_a():
    assert set_winner(6, 4) == "A"
    assert set_winner(7, 6) == "A"


def test_set_winner_b():
    assert set_winner(4, 6) == "B"
    assert set_winner(6, 7) == "B"


def test_set_undecided():
    assert set_winner(3, 2) is None


# ---------------- MATCH STATUS TESTS ----------------

def test_match_a_wins():
    assert match_status(3, 1, 5) == "A wins"


def test_match_b_wins():
    assert match_status(1, 3, 5) == "B wins"


def test_match_decider():
    assert match_status(2, 2, 5) == "decider"


def test_match_in_progress():
    assert match_status(1, 0, 5) == "in progress"
