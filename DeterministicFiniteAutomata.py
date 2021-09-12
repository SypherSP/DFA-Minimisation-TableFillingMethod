from prettytable import PrettyTable
class DFA:
    states = []
    alphabet = []
    initial = ''
    final_states = []
    transitions = {}

    def __init__(self):
        return

    def takeInput(self):
        self.states = input(
            "Enter the STATES seperated by commas: ").split(",")
        self.alphabet = input(
            "Enter the ALPHABET seperated by commas: ").split(",")
        self.initial = input("Enter the INITIAL STATE: ")
        self.final_states = input(
            "Enter the FINAL STATES seperated by commas: ").split(",")
        self.prepTransitions()

    def prepTransitions(self):
        print("Enter the transitions: ")
        for state in self.states:
            print(f"State {state}")
            self.transitions[state] = {}
            for letter in self.alphabet:
                self.transitions[state][letter] = input(f"\tInput {letter}: ")

    def display(self):
        print("-----------------------------")
        print(f'{self.states} {self.initial} {self.final_states}\n{self.alphabet}\n{self.transitions}')
        print("-----------------------------")

    def showTransitions(self):
        table=PrettyTable()
        fname=[' ']
        for letter in self.alphabet:
            fname.append(letter)
        table.field_names=fname
        for state in self.states:
            newEntry=[state]
            for letter in self.alphabet:
                newEntry.append(self.transitions[state][letter])
            table.add_row(newEntry)
        
        print(table)
            

        