# Table Filling Method

from DeterministicFiniteAutomata import DFA
from copy import copy


dfa = DFA()
newDFA = DFA()
marked = {}
finalEq = []

# EXAMPLE TEST CASES

# test1

# dfa.states = ['A', 'B', 'C', 'D', 'E']
# dfa.alphabet = ['0', '1']
# dfa.final_states = ['E']
# dfa.initial = 'A'
# dfa.transitions = {'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'B', '1': 'D'}, 'C': {
#     '0': 'B', '1': 'C'}, 'D': {'0': 'B', '1': 'E'}, 'E': {'0': 'B', '1': 'C'}}

# test2

# dfa.states = ['A', 'B', 'C', 'D', 'E', 'F']
# dfa.alphabet = ['0', '1']
# dfa.final_states = ['C', 'D', 'E']
# dfa.initial = 'A'
# dfa.transitions = {'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'A', '1': 'D'}, 'C': {
#     '0': 'E', '1': 'F'}, 'D': {'0': 'E', '1': 'F'}, 'E': {'0': 'E', '1': 'F'}, 'F': {'0': 'F', '1': 'F'}}

# test 3

dfa.states = ['A', 'B', 'C', 'D', 'E', 'G']
dfa.alphabet = ['0', '1']
dfa.final_states = ['B', 'C', 'G']
dfa.initial = 'A'
dfa.transitions = {'A': {'0': 'B', '1': 'C'}, 'B': {'0': 'D', '1': 'E'}, 'C': {
    '0': 'E', '1': 'D'}, 'D': {'0': 'G', '1': 'G'}, 'E': {'0': 'G', '1': 'G'}, 'G': {'0': 'G', '1': 'G'}}

print("Example initialised with the following DFA:")
dfa.display()


def printMarked():
    for hmm in marked:
        print(f'{hmm} {marked[hmm]}')


def prepMarked():
    for id1, state1 in enumerate(dfa.states):
        marked[state1] = {}
        for id2, state2 in enumerate(dfa.states):
            # if id1 < id2:
            marked[state1][state2] = False


def zeroEq():
    for id1, state1 in enumerate(dfa.states):
        for id2, state2 in enumerate(dfa.states):
            if (state1 in dfa.final_states) and (state2 not in dfa.final_states):
                marked[state1][state2] = True
            elif (state1 not in dfa.final_states) and (state2 in dfa.final_states):
                marked[state1][state2] = True


def isMarkedMirror(id1, id2):
    return marked[dfa.states[id2]][dfa.states[id1]]


def minimize():
    while True:
        change = False
        for id1, state1 in enumerate(dfa.states):
            for id2, state2 in enumerate(dfa.states):
                if(id1 != id2):
                    if not marked[state1][state2]:
                        for letter in dfa.alphabet:
                            t1 = dfa.transitions[state1][letter]
                            t2 = dfa.transitions[state2][letter]
                            if dfa.states.index(t1) != dfa.states.index(t2):
                                if marked[t1][t2]:
                                    marked[state1][state2] = True
                                    change = True
        if not change:
            break


def finalEquivalence():
    for id1, state1 in enumerate(dfa.states):
        for id2, state2 in enumerate(dfa.states):
            if(id1 < id2):
                if not marked[state1][state2]:
                    inserted = False
                    for newState in finalEq:
                        if (state1 in newState) and (state2 not in newState):
                            newState.append(state2)
                            inserted = True
                            break
                        elif (state1 not in newState) and (state2 in newState):
                            newState.append(state1)
                            inserted = True
                            break
                        elif (state1 in newState) and (state2 in newState):
                            inserted = True
                            break
                    if not inserted:
                        newState = [state1, state2]
                        finalEq.append(newState)
                        inserted = True

    for id1, state1 in enumerate(dfa.states):
        allmarked = True
        for id2, state2 in enumerate(dfa.states):
            if(id1 < id2):
                if not marked[state1][state2]:
                    allmarked = False
        if allmarked:
            inGrp = False
            for grp in finalEq:
                if state1 in grp:
                    inGrp = True
            if not inGrp:
                newState = [state1]
                finalEq.append(newState)


def constructNewDFA():
    newDFA.alphabet = copy(dfa.alphabet)
    stateRelations = {}
    for group in finalEq:
        newState = ''.join(group)
        for state in group:
            stateRelations[copy(state)] = newState

    newDFA.initial = stateRelations[dfa.initial]
    for state in dfa.final_states:
        if stateRelations[state] not in newDFA.final_states:
            newDFA.final_states.append(copy(stateRelations[state]))
    for state in dfa.states:
        if stateRelations[state] not in newDFA.states:
            newDFA.states.append(copy(stateRelations[state]))

    doneTransition = {}
    for state in newDFA.states:
        doneTransition[state] = False

    for state in dfa.states:
        newState = stateRelations[state]
        if not doneTransition[newState]:
            newDFA.transitions[newState] = {}
            for letter in newDFA.alphabet:
                newDFA.transitions[newState][letter] = stateRelations[dfa.transitions[state][letter]]
            doneTransition[newState] = True


def output():
    print(
        f'\nFollowing is the Minimum Equivalence State Partition:\n\t{finalEq}\n')
    print('Following is the Minimum State Transition Table:')
    newDFA.showTransitions()

# dfa.takeInput()
prepMarked()
zeroEq()
minimize()
finalEquivalence()
constructNewDFA()
output()
