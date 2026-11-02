
import pytest
from tennis_scoring import game_score, set_winner, match_status


# ---------------- GAME SCORE BRANCH TESTS ----------------

def test_negative_points_a():
    with pytest.raises(ValueError):
        game_score(-1, 0)


def test_negative_points_b():
    with pytest.raises(ValueError):
        game_score(0, -1)


def test_game_score_basic_branches():
    assert game_score(0, 0) == "0-0"
    assert game_score(3, 0) == "40-0"
    assert game_score(0, 3) == "0-40"


def test_deuce_and_advantage_branches():
    assert game_score(3, 3) == "deuce"
    assert game_score(4, 3) == "advantage A"
    assert game_score(3, 4) == "advantage B"


def test_game_winner_branches():
    assert game_score(5, 3) == "game A"
    assert game_score(3, 5) == "game B"
    assert game_score(4, 0) == "game A"
    assert game_score(0, 4) == "game B"


# ---------------- SET WINNER BRANCH TESTS ----------------

def test_set_a_winning_branches():
    assert set_winner(6, 4) == "A"
    assert set_winner(7, 6) == "A"


def test_set_b_winning_branches():
    assert set_winner(4, 6) == "B"
    assert set_winner(6, 7) == "B"


def test_set_winner_boundary_conditions():
    assert set_winner(6, 5) is None
    assert set_winner(5, 6) is None
    assert set_winner(6, 6) is None
    assert set_winner(7, 5) == "A"
    assert set_winner(5, 7) == "B"


# ---------------- MATCH STATUS BRANCH TESTS ----------------

def test_match_a_wins_branch():
    assert match_status(3, 1, 5) == "A wins"


def test_match_b_wins_branch():
    assert match_status(1, 3, 5) == "B wins"


def test_match_decider_branch():
    assert match_status(2, 2, 5) == "decider"


def test_match_in_progress_branch():
    assert match_status(1, 0, 5) == "in progress"
