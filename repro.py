from datetime import datetime, timedelta
from session import UserSession

login_time = datetime(2026, 1, 1, 10, 0, 0)
# User has been logged in for 1 hour, but active 30 seconds ago
last_active = datetime(2026, 1, 1, 11, 0, 0)
now = datetime(2026, 1, 1, 11, 0, 30)

session = UserSession(
    session_id="sess_123",
    user_id="user_456",
    created_at=login_time,
    last_activity_at=last_active,
)

# Idle limit is 300 seconds (5 minutes)
valid = session.is_valid(now, max_idle_seconds=300)
print(f"Session valid: actual={valid}, expected=True")

if not valid:
    print("BUG DETECTED: Active session was prematurely expired because created_at was used instead of last_activity_at!")
    raise SystemExit(1)
raise SystemExit(0)
