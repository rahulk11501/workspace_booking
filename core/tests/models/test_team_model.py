# core/tests/models/test_team_model.py
import pytest
from core.tests.factories.team_factory import TeamFactory

@pytest.mark.django_db
def test_team_creation():
    team = TeamFactory()
    assert team.id is not None
    assert team.name
    assert len(team.members.all()) >= 2
