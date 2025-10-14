# core/tests/schemas/test_team_schema.py
import pytest
from core.domain.schemas.team_schema import TeamSchema
from core.tests.factories.team_factory import TeamFactory

@pytest.mark.django_db
def test_team_schema_validation():
    team = TeamFactory()
    schema = TeamSchema.model_validate(team)  # works now
    assert schema.name == team.name
    assert len(schema.members) == team.members.count()
    for member_schema, member_model in zip(schema.members, team.members.all()):
        assert member_schema.name == member_model.name
        assert member_schema.age == member_model.age
        assert member_schema.gender == member_model.gender
