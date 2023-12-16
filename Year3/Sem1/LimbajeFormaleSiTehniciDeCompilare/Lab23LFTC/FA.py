import re


def print_list_of_strings(list_name, _list):
    print(f'{list_name} = {{{", ".join(_list)}}}')


class FA:
    def __init__(self, filename):
        self.filename = filename
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = ""
        self.output_states = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    self.process_line(line.strip())
        except Exception as e:
            print(f"Error when initializing FA: {e}")

    def process_line(self, line):
        match = re.match(r"^([a-z_]*)=", line)
        if match:
            key = match.group(1)
            value = line.split("=")[1].strip()
            self.process_assignment(key, value)
        else:
            raise Exception(f"Invalid line: {line}")

    def process_assignment(self, key, value):
        if key == "states":
            self.states = re.findall(r'\b\w+\b', value)
        elif key == "alphabet":
            # Extract alphabet values between curly braces
            self.alphabet = re.findall(r'{(.*?)}', value)[0].split(', ')
        elif key == "out_states":
            self.output_states = re.findall(r'\b\w+\b', value)
        elif key == "initial_state":
            self.initial_state = value
        elif key == "transitions":
            self.process_transitions(value)
        else:
            raise Exception("Invalid key in file")

    def process_transitions(self, value):
        transitions = re.findall(r'\(([^;)]*)\)', value)
        for transition in transitions:
            values = [v.strip() for v in transition.split(",")]
            self.transitions.append(Transition(values[0], values[1], values[2]))

    def print_states(self):
        print_list_of_strings("states", self.states)

    def print_alphabet(self):
        print_list_of_strings("alphabet", self.alphabet)

    def print_output_states(self):
        print_list_of_strings("out_states", self.output_states)

    def print_initial_state(self):
        print(f'initial_state = {self.initial_state}')

    def print_transitions(self):
        print("transitions = {")
        for i, transition in enumerate(self.transitions):
            if i != len(self.transitions) - 1:
                print(f'    ({transition.from_state}, {transition.to_state}, {transition.label}),')
            else:
                print(f'    ({transition.from_state}, {transition.to_state}, {transition.label})')
        print("}")

    def check_accepted(self, word):
        current_state = self.initial_state
        for c in word:
            found = False
            for transition in self.transitions:
                if transition.from_state == current_state and transition.label == c:
                    current_state = transition.to_state
                    found = True
                    break
            if not found:
                return False
        return current_state in self.output_states

    def get_next_accepted(self, word):
        current_state = self.initial_state
        accepted_word = ""
        for c in word:
            new_state = None
            for transition in self.transitions:
                if transition.from_state == current_state and transition.label == c:
                    new_state = transition.to_state
                    accepted_word += c
                    break
            if new_state is None:
                if current_state not in self.output_states:
                    return None
                else:
                    return accepted_word
            current_state = new_state
        return accepted_word


class Transition:
    def __init__(self, from_state, to_state, label):
        self.from_state = from_state
        self.to_state = to_state
        self.label = label

    def __str__(self):
        return f'Transition(from_state={self.from_state}, to_state={self.to_state}, label={self.label})'
