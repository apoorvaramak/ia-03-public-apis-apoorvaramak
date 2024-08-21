import pytest  
from hockey_api import get_team_id, teams_playing_today


def test_get_team_blackhawks():
    assert get_team_id("Chicago Blackhawks") == 678

def test_get_invalid_team_yotes():
    assert get_team_id("Arizona Yotes") == 0

def test_get_teams_playing_april_tenth():
    assert "Chicago Blackhawks" and "Arizona Coyotes" in teams_playing_today("2024-04-10")

@pytest.mark.xfail
def test_get_teams_not_playing_april_tenth():
    assert "San Jose Sharks" in teams_playing_today("2024-04-10")

@pytest.mark.xfail
def test_invalid_teams_playing_april_tenth():
    assert "London Knights" in teams_playing_today("2024-04-10")

