from datetime import datetime, timedelta
from session import UserSession


def test_active_session_with_recent_activity_is_valid():
    start = datetime(2026, 1, 1, 9, 0, 0)
    active = datetime(2026, 1, 1, 10, 59, 0)
    now = datetime(2026, 1, 1, 11, 0, 0)
    sess = UserSession("s1", "u1", start, active)
    assert sess.is_valid(now, max_idle_seconds=300) is True


def test_idle_session_exceeding_timeout_expires():
    start = datetime(2026, 1, 1, 9, 0, 0)
    active = datetime(2026, 1, 1, 9, 10, 0)
    now = datetime(2026, 1, 1, 9, 20, 0)
    sess = UserSession("s2", "u2", start, active)
    assert sess.is_valid(now, max_idle_seconds=300) is False
