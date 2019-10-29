# my_states.py

from state import State

# Start of our states
class PendingState(State):
    """
    The state which indicates that the order/item is pending.
    """

    def on_event(self, event):
        if event == 'approve':
            return ApprovedState()
        elif event == 'reject':
            return RejectedState()

        return self


class ApprovedState(State):
    """
       The state which indicates that the order/item is approved.
    """

    def on_event(self, event):
        if event == 'reject':
            return RejectedState()
        elif event == 'hold':
            return PendingState()

        return self

class RejectedState(State):
    """
        The state which indicates that the order/item has been rejected.
    """

    def on_event(self, event):
        if event == 'hold':
            return PendingState()
        elif event == 'hold':
            return PendingState()

        return self
# End of our states.