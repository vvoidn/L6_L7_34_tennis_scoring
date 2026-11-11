import pytest
from hypothesis import given, strategies as st
from tennis_scoring import parse_score, game_lead, set_spread


# 1. PARSE SCORE TESTS

@given(st.integers(min_value=0), st.integers(min_value=0))
def test_parse_score_valid(a, b):
    assert parse_score(f"{a}-{b}") == (a, b)


@given(st.one_of(st.none(), st.text().filter(
    lambda s: s.count('-') != 1
)))
def test_parse_score_invalid(s):
    with pytest.raises(ValueError):
        parse_score(s)


# 2. GAME LEAD TESTS

@given(
    st.sampled_from(['0', '15', '30', '40']),
    st.sampled_from(['0', '15', '30', '40'])
)
def test_game_lead_valid(a, b):
    points = {'0': 0, '15': 1, '30': 2, '40': 3}
    assert game_lead(f"{a}-{b}") == points[a] - points[b]


@given(st.one_of(st.none(), st.text()))
def test_game_lead_invalid(s):
    with pytest.raises(ValueError):
        game_lead(s)


# 3. SET SPREAD TESTS

@given(st.lists(st.integers(min_value=0), min_size=1))
def test_set_spread_valid(games):
    csv = ','.join(map(str, games))
    assert set_spread(csv) == max(games) - min(games)


@given(st.one_of(st.none(), st.text().filter(
    lambda s: not all(part.strip().isdigit()
                      for part in s.split(','))
)))
def test_set_spread_invalid(s):
    with pytest.raises(ValueError):
        set_spread(s)
