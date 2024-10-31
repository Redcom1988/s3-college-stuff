def delta_dfa(state, symbol, transitions):
    return transitions.get((state, symbol))

def hat_delta_dfa(state, string, transitions):
    current_state = state
    print(f"Starting state: {current_state}")
    for symbol in string:
        next_state = delta_dfa(current_state, symbol, transitions)
        # if next_state is None:
        #     print(f"No transition for state {current_state} with symbol {symbol}")
        #     return None
        print(f"Transition: {current_state} --{symbol}--> {next_state}")
        current_state = next_state
    print(f"Final state: {current_state}")
    return current_state

def dfa_l1():
    # L1: All strings that start with '10' and end with '01'
    transitions = {
        ('A', '1'): 'C',
        ('A', '0'): 'B',
        ('B', '0'): 'B',
        ('B', '1'): 'B',
        ('C', '0'): 'D',
        ('C', '1'): 'B',
        ('D', '0'): 'E',
        ('D', '1'): 'F',
        ('E', '0'): 'E',
        ('E', '1'): 'F',
        ('F', '0'): 'E',
        ('F', '1'): 'D'
    }
    start_state = 'A'
    accept_states = {'F'}
    return transitions, start_state, accept_states

def dfa_l2():
    # L2: All strings that contain '000' and end with '1'
    transitions = {
        ('A', '0'): 'B',
        ('A', '1'): 'A',
        ('B', '0'): 'C',
        ('B', '1'): 'A',
        ('C', '0'): 'D',
        ('C', '1'): 'A',
        ('D', '0'): 'D',
        ('D', '1'): 'E',
        ('E', '0'): 'D',
        ('E', '1'): 'E'
    }
    start_state = 'A'
    accept_states = {'E'}
    return transitions, start_state, accept_states

def dfa_l3():
    # L3: All strings that start and end with a different symbol
    transitions = {
        ('A', '0'): 'B',
        ('A', '1'): 'D',
        ('B', '0'): 'B',
        ('B', '1'): 'C',
        ('C', '0'): 'B',
        ('C', '1'): 'C',
        ('D', '0'): 'E',
        ('D', '1'): 'D',
        ('E', '0'): 'E',
        ('E', '1'): 'D'
    }
    start_state = 'A'
    accept_states = {'C', 'E'}
    return transitions, start_state, accept_states

def dfa_l4():
    # L4: All strings that start and end with an identical symbol and contain '101'
    transitions = {
        ('A', '0'): 'B', 
        ('A', '1'): 'H',
        ('B', '0'): 'B',
        ('B', '1'): 'C',
        ('C', '0'): 'D',
        ('C', '1'): 'C',
        ('D', '0'): 'B',
        ('D', '1'): 'E',
        ('E', '0'): 'F',
        ('E', '1'): 'E',
        ('F', '0'): 'F',
        ('F', '1'): 'E',
        ('G', '0'): 'G',
        ('G', '1'): 'H',
        ('H', '0'): 'I',
        ('H', '1'): 'H',
        ('I', '0'): 'G',
        ('I', '1'): 'J',
        ('J', '0'): 'I',
        ('J', '1'): 'J',
    }
    start_state = 'A'
    accept_states = {'F', 'J'}
    return transitions, start_state, accept_states

def main():
    dfas = [dfa_l1(), dfa_l2(), dfa_l3(), dfa_l4()]
    dfa_names = ["L1", "L2", "L3", "L4"]

    while True:
        input_string = input("Enter a string of 1's and 0's to check (or 'q' to quit): ")
        if input_string.lower() == 'q':
            break

        for i, (transitions, start_state, accept_states) in enumerate(dfas):
            print(f"\nChecking {dfa_names[i]}:")
            final_state = hat_delta_dfa(start_state, input_string, transitions)
            if final_state in accept_states:
                print(f"String is accepted by {dfa_names[i]}")
            else:
                print(f"String is not accepted by {dfa_names[i]}")

if __name__ == "__main__":
    main()
