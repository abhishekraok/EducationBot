import json
import random

from Action import StateFunctions


class State():
    def __init__(self):
        self.state_name = ''
        self.following_states = []
        self.next_distribution = []

    def __repr__(self):
        return self.state_name + ' with ' + str(self.following_states) + ' next states'


class StateCollection:
    def __init__(self):
        self.states = {}

    def next_state(self, current_state_name, intent):
        current_state = self.states[current_state_name]
        next_states_list = current_state.following_states
        return random.choice[next_states_list]

    def load(self, json_states_file):
        with open(json_states_file, 'r') as f:
            self.decoded = json.load(f)
        for json_state in self.decoded['states']:
            new_state = State()
            new_state.state_name = json_state['state_name']
            if(not callable(getattr(StateFunctions, new_state.state_name))):
                message = 'The state ' + new_state.state_name + ' has no method associated with it'
                print message
                raise Exception(message)
            new_state.following_states = json_state['following_states']
            new_state.next_distribution = json_state['next_distribution']
            self.states[new_state.state_name] = new_state

    def starting_state(self):
        # There should always be a start
        return self.states['start']


