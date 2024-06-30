from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session


@pytest.fixture
def mock_session() -> MagicMock:
    return MagicMock(spec=Session)


@pytest.fixture
def mock_bad_commit_session() -> MagicMock:
    mock_bad_session = MagicMock(spec=Session)
    mock_bad_session.commit.side_effect = Exception
    return mock_bad_session


@pytest.fixture
def mock_none_response() -> MagicMock:
    mock_none_response = MagicMock(spec=Session)
    mock_none_response.query().filter().first.return_value = None
    return mock_none_response


@pytest.fixture
def mock_bad_query_session() -> MagicMock:
    mock_bad_query_session = MagicMock(spec=Session)
    mock_bad_query_session.query.side_effect = Exception
    return mock_bad_query_session
