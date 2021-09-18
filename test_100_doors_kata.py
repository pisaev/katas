from unittest.mock import call

from mock import Mock
from pytest import fixture


class Door:
	def __init__(self, state):
		self._state = state

	def toggleState(self):
		if self._state == "open":
			self._state = "closed"
		else:
			self._state = "open"

	def showState(self, output):
		output(self._state)


class Closed_Doors:
	def __init__(self, num_doors):
		self._doors = [Door("Dummy")] + [Door("closed") for i in range(num_doors)]

	def visit(self):
		for step in range(1, len(self._doors)):
			for i, door in enumerate(self._doors):
				if i % step ==0 :
					door.toggleState()

	def showState(self, output):
		for door in self._doors[1::]:
			door.showState(output)


'''
100 doors in a row are all initially closed. You make 100 passes by the doors. 
The first time through, you visit every door and toggle the door (if the door is closed, you open it; 
if it is open, you close it).
The second time you only visit every 2nd door (door #2, #4, #6, ...).
The third time, every 3rd door (door #3, #6, #9, ...), etc, until you only visit the 100th door.

Question: What state are the doors in after the last pass? Which are open, which are closed?

As a player I want to visit 100 doors, changing its state, using the rule of each time step n-th door
In order to see the final state
'''

@fixture
def output():
	return Mock()

def test_doors_created_in_closed_state(output):
	doors = Closed_Doors(1)
	doors.showState(output)

	calls = [call("closed")]
	output.assert_has_calls(calls)

	doors = Closed_Doors(3)
	doors.showState(output)

	calls = [call("closed")] * 3
	output.assert_has_calls(calls)


def test_visit_toggle_first_to_open_state(output):
	doors = Closed_Doors(1)
	doors.visit()
	doors.showState(output)

	calls = [call("open")]
	output.assert_has_calls(calls)


def test_visit_toggle_second_to_closed(output):
	doors = Closed_Doors(2)
	doors.visit()
	doors.showState(output)

	calls = [call("open"), call("closed")]
	output.assert_has_calls(calls)


def test_visit_toggle_third_door_to_closed(output):
	doors = Closed_Doors(3)
	doors.visit()
	doors.showState(output)

	calls = [call("open"), call("closed"), call("closed")]
	output.assert_has_calls(calls)


def test_visit_toggle_4th_door_to_open(output):
	doors = Closed_Doors(4)
	doors.visit()
	doors.showState(output)

	calls = [call("open"), call("closed"), call("closed"), call("open")]
	output.assert_has_calls(calls)


def test_visit_toggle_5th_door_to_closed(output):
	doors = Closed_Doors(5)
	doors.visit()
	doors.showState(output)

	calls = [call("open"), call("closed"), call("closed"), call("open"), call("closed")]
	output.assert_has_calls(calls)
