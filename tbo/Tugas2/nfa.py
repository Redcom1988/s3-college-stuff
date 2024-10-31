def nfa_l1():
    # L1: All strings that start with '10' and end with '01'
    transitions = {
        ('Q0', '0'): {}, 
        ('Q0', '1'): {'Q1'},
        ('Q1', '0'): {'Q2'},
        ('Q1', '1'): {},
        ('Q2', '0'): {'Q2', 'Q3'},
        ('Q2', '1'): {'Q2', 'Q4'},
        ('Q3', '0'): {},
        ('Q3', '1'): {'Q4'},
        ('Q4', '0'): {},
        ('Q4', '1'): {},
    }
    start_state = 'Q0'
    accept_states = {'Q4'}
    return transitions, start_state, accept_states

def nfa_l2():
    # L2: All strings that contain '000' and end with '1'
    transitions = {
        ('Q0', '0'): {'Q0', 'Q1'}, 
        ('Q0', '1'): {'Q0'},
        ('Q1', '0'): {'Q2'},
        ('Q1', '1'): {},
        ('Q2', '0'): {'Q3'},
        ('Q2', '1'): {},
        ('Q3', '0'): {'Q3'},
        ('Q3', '1'): {'Q3', 'Q4'},
        ('Q4', '0'): {},
        ('Q4', '1'): {},
    }
    start_state = 'Q0'
    accept_states = {'Q4'}
    return transitions, start_state, accept_states

def nfa_l3():
    # L3: All strings that start and end with a different symbol
    transitions = {
        ('Q0', '0'): {'Q1'}, 
        ('Q0', '1'): {'Q2'},
        ('Q1', '0'): {'Q1'},
        ('Q1', '1'): {'Q1', 'Q3'},
        ('Q2', '0'): {'Q2', 'Q3'},
        ('Q2', '1'): {'Q2'},
        ('Q3', '0'): {},
        ('Q3', '1'): {},
    }
    start_state = 'Q0'
    accept_states = {'Q3'}
    return transitions, start_state, accept_states

def nfa_l4():
    # L4: All strings that start and end with an identical symbol and contain '101'
    transitions = {
        ('Q0', '0'): {'Q1'}, 
        ('Q0', '1'): {'Q2', 'Q4'},
        ('Q1', '0'): {'Q1'},
        ('Q1', '1'): {'Q1', 'Q3'},
        ('Q2', '0'): {'Q2'},
        ('Q2', '1'): {'Q2', 'Q4'},
        ('Q3', '0'): {'Q5'},
        ('Q3', '1'): {},
        ('Q4', '0'): {'Q6'},
        ('Q4', '1'): {},
        ('Q5', '0'): {},
        ('Q5', '1'): {'Q7'},
        ('Q6', '0'): {},
        ('Q6', '1'): {'Q8', 'Q9'},
        ('Q7', '0'): {'Q7', 'Q9'},
        ('Q7', '1'): {'Q7'},
        ('Q8', '0'): {'Q8'},
        ('Q8', '1'): {'Q8', 'Q9'},
        ('Q9', '0'): {},
        ('Q9', '1'): {},
    }
    start_state = 'Q0'
    accept_states = {'Q9'}
    return transitions, start_state, accept_states

def delta_nfa(state, symbol, transitions):
    return transitions.get((state, symbol), set())

def hat_delta_nfa(states, input_string, transitions):
    current_states = {states}
    for symbol in input_string:
        next_states = set()
        for state in current_states:
            next_states.update(delta_nfa(state, symbol, transitions))
        current_states = next_states
    return sorted(current_states)


def print_process(start_state, input_string, transitions):
    current_states = {start_state}
    print(f"δ^({start_state}, ε) = {{{start_state}}}")
    
    for i, symbol in enumerate(input_string):
        prefix = input_string[:i+1]
        next_states = set()
        
        for state in current_states:
            next_states.update(delta_nfa(state, symbol, transitions))
        
        transitions_text = " ∪ ".join(f"δ({state}, {symbol})" for state in current_states)
        states_text = " ∪ ".join('{' + ', '.join(sorted(delta_nfa(state, symbol, transitions))) + '}' 
                                for state in current_states)
        result_text = '{' + ', '.join(sorted(next_states)) + '}'
        print(f"δ^({start_state}, {prefix}) = {transitions_text} = {states_text} = {result_text}")
        
        if not next_states:
            print("Proses berhenti karena tidak ada transisi valid.")
            break
            
        current_states = next_states

def main(): 
    # L1: All strings that start with '10' and end with '01'
    # L2: All strings that contain '000' and end with '1'
    # L3: All strings that start and end with a different symbol
    # L4: All strings that start and end with an identical symbol and contain '101'

    # l1 accept
    transitions, start_state, accept_states = nfa_l1()
    input_string = '101101101'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l1()
    input_string = '101001101'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    #l1 reject
    transitions, start_state, accept_states = nfa_l1()
    input_string = '01000010'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")
    
    transitions, start_state, accept_states = nfa_l1()
    input_string = '101000010'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")


    #l2 accept
    transitions, start_state, accept_states = nfa_l2()
    input_string = '110001001'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l2()
    input_string = '110000011'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    #l2 reject
    transitions, start_state, accept_states = nfa_l2()
    input_string = '11000100'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l2()
    input_string = '11001101'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")


    #l3 accept
    transitions, start_state, accept_states = nfa_l3()
    input_string = '10101010'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l3()
    input_string = '01110111'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    #l3 reject
    transitions, start_state, accept_states = nfa_l3()
    input_string = '11010111'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l3()
    input_string = '01010110'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")


    #l4 accept
    transitions, start_state, accept_states = nfa_l4()
    input_string = '110101101'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l4()
    input_string = '010101010'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    #l4 reject
    transitions, start_state, accept_states = nfa_l4()
    input_string = '111010110'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

    transitions, start_state, accept_states = nfa_l4()
    input_string = '110011001'
    print(f"Input string: {input_string}")
    print_process(start_state, input_string, transitions)
    results = hat_delta_nfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if any(state in accept_states for state in results) else 'Rejected'}\n")

if __name__ == "__main__":
    main()