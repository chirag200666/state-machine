from workflow import Workflow
from my_states import PendingState, ApprovedState, RejectedState

import unittest
 
class TestWorkflow(unittest.TestCase):
    """
    Test Workflow class with all its functions
    """
 
    def test_workflow_init_pending(self):
        """
        Test Init of worflow with pending state
        """
        workflow = Workflow('pending')
        self.assertEqual(workflow.state, PendingState())

    def test_workflow_init_approve(self):
        """
        Test Init of worflow with approved state
        """
        workflow = Workflow('approved')
        self.assertEqual(workflow.state, ApprovedState())

    def test_workflow_init_reject(self):
        """
        Test Init of worflow with rejected state
        """
        workflow = Workflow('rejected')
        self.assertEqual(workflow.state, RejectedState())

    def test_workflow_init_none(self):
        """
        Test Init of worflow with none state
        """
        workflow = Workflow('abc')
        self.assertEqual(workflow.state, None)

 
    def test_change_approved_to_pending(self):
        """
        Test state change from approved to pending with hold event
        """
        workflow = Workflow('approved')
        workflow.on_event('hold')
        self.assertEqual(workflow.state, PendingState())
 
    def test_change_approved_to_rejected(self):
        """
        Test state change from approved to rejected with reject event
        """
        workflow = Workflow('approved')
        workflow.on_event('reject')
        self.assertEqual(workflow.state, RejectedState())

    def test_change_approved_to_approved(self):
        """
        Test no state change from approved to approved with approve event
        """
        workflow = Workflow('approved')
        workflow.on_event('approve')
        self.assertEqual(workflow.state, ApprovedState())

    def test_change_pending_to_rejected(self):
        """
        Test state change from pending to rejected with reject event
        """
        workflow = Workflow('pending')
        workflow.on_event('reject')
        self.assertEqual(workflow.state, RejectedState())

    def test_change_pending_to_approved(self):
        """
        Test state change from pending to approved with approve event
        """
        workflow = Workflow('pending')
        workflow.on_event('approve')
        self.assertEqual(workflow.state, ApprovedState())

    def test_change_pending_to_pending(self):
        """
        Test no state change from pending to pending with hold event
        """
        workflow = Workflow('pending')
        workflow.on_event('hold')
        self.assertEqual(workflow.state, PendingState())

    def test_change_pending_to_pending_multiple_events(self):
        """
        Test no state change from pending to pending with full circle of event ending at hold
        """
        workflow = Workflow('pending')
        workflow.on_event('hold')
        workflow.on_event('approve')
        workflow.on_event('reject')
        workflow.on_event('hold')
        self.assertEqual(workflow.state, PendingState())

    def test_change_rejected_to_pending(self):
        """
        Test state change from rejected to pending with hold event
        """
        workflow = Workflow('rejected')
        workflow.on_event('hold')
        self.assertEqual(workflow.state, PendingState())

    def test_change_rejected_to_rejected(self):
        """
        Test no state change from rejected to rejected with rejecte event
        """
        workflow = Workflow('rejected')
        workflow.on_event('reject')
        self.assertEqual(workflow.state, RejectedState())

    def test_dont_change_rejected_to_approved(self):
        """
        Test no state change from rejected to rejected with approve event
        """
        workflow = Workflow('rejected')
        workflow.on_event('approve')
        self.assertEqual(workflow.state, RejectedState())

 
 
if __name__ == '__main__':
    unittest.main()