# workflow.py

from my_states import PendingState, ApprovedState, RejectedState

class Workflow(object):
    """ 
    A simple state machine that mimics the functionality of a workflow from a 
    high level.
    """

    def __init__(self, state_name):
        """ Initialize the components. """

        # Start with a default state.
        if state_name == 'pending':
            self.state = PendingState()
        elif state_name == 'approved':
            self.state = ApprovedState()
        elif state_name == 'rejected':
            self.state = RejectedState()
        else:
            #throw error if needed
            self.state = None

    def on_event(self, event):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(event)

workflow = Workflow('pending')
print('string workflow with state: ', workflow.state)
workflow.on_event('pending')
workflow.on_event('approve')
print('state after few events: ',workflow.state)
workflow.on_event('pending')
workflow.on_event('reject')
print('final state: ',workflow.state)