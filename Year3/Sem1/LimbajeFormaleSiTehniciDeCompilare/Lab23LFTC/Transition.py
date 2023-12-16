class Transition:
    def __init__(self, from_state, to_state, label):
        self._from_state = from_state
        self._to_state = to_state
        self._label = label

    @property
    def from_state(self):
        return self._from_state

    @from_state.setter
    def from_state(self, from_state):
        self._from_state = from_state

    @property
    def to_state(self):
        return self._to_state

    @to_state.setter
    def to_state(self, to_state):
        self._to_state = to_state

    @property
    def label(self):
        return self._label

    @label.setter
    def label(self, label):
        self._label = label

    def __str__(self):
        return f'Transition(from_state={self._from_state}, to_state={self._to_state}, label={self._label})'
