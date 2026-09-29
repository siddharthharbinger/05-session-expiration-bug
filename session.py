from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserSession:
    session_id: str
    user_id: str
    created_at: datetime
    last_activity_at: datetime
    is_revoked: bool = False

    def touch(self, now: datetime) -> None:
        """Update last activity timestamp."""
        self.last_activity_at = now

    def is_valid(self, now: datetime, max_idle_seconds: int) -> bool:
        """Return True if session is not revoked and has not exceeded idle timeout."""
        if self.is_revoked:
            return False
        # Bug: checks idle timeout against created_at instead of last_activity_at
        idle_seconds = (now - self.created_at).total_seconds()
        return idle_seconds <= max_idle_seconds
