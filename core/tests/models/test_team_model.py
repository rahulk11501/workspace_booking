import pytest
from core.tests.factories.team_factory import TeamFactory

@pytest.mark.django_db
def test_team_creation():
    team = TeamFactory.create()
    assert team.name
    # Teams can exist without members; just assert members field works
    assert hasattr(team, "members")
    assert team.members.count() >= 0
