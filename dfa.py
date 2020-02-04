class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, end_states):
        " DFA class constructor "
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.end_states = end_states

        self.current_state = start_state
        return

    def check_word(self, given_word):
        """ a function that, given a word, checks the state transitions from the transfer function and
        returns if it reached a final state or not, meaning if the word is valid or not """
        self.current_state = self.start_state  # begin at the start state

        """ for each character in a word, check if the pair of the character and the current state is
        defined in the transfer function. if it is then change the current state to the next state
        from the transfer function. if it isn't then set the current state to 'None' """
        for current_character in given_word:
            if (self.current_state, current_character) not in self.transition_function.keys():
                self.current_state = None
            else:
                self.current_state = self.transition_function[(self.current_state, current_character)]

        # return 'True' if the last current state was in the defined final states
        return self.current_state in self.end_states
