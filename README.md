# Session Expiration Bug

High-level bug: `UserSession.is_valid` calculates idle duration using `self.created_at` rather than `self.last_activity_at`. As a result, active users who frequently interact with the application are forcefully expired and logged out once `max_idle_seconds` elapses from their initial login.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected result: A session created 1 hour ago with activity 30 seconds ago should remain valid for `max_idle_seconds = 300`, but the buggy implementation returns `False`.
