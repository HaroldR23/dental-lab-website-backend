from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session


@pytest.fixture
def mock_session() -> MagicMock:
    return MagicMock(spec=Session)

@pytest.fixture
def mock_bad_session() -> MagicMock:
    mock_bad_session = MagicMock(spec=Session)
    mock_bad_session.commit.side_effect = Exception
    return mock_bad_session
