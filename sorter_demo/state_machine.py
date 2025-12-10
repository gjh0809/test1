class StateMachine:
    """Very small event handler to track pipeline state."""

    def __init__(self):
        self.last_event = None

    def handle(self, event: str):
        self.last_event = event
        # Real implementation would trigger transitions, logging, alarms.
        return event

