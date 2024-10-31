def nfatransition(state, input_symbol):
    transitions = {
        ('q0', '0'): {'q1', 'q2'},
        ('q0', '1'): {},
        ('q1', '0'): {},
        ('q1', '1'): {'q3', 'q4'},
        ('q2', '0'): {},
        ('q2', '1'): {'q1'},
        ('q3', '0'): {},
        ('q3', '1'): {'q1'},
        ('q4', '0'): {},
        ('q4', '1'): {'q5'},
        ('q5', '0'): {},
        ('q5', '1'): {},
    }
    start_state = 'q0'
    accept_states = {'q5', 'q3'}
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
    input_string = '01', '011', '0111', '010', '0110', '01110'
    transitions, start_state, accept_states = nfatransition('q0', '0')
    for string in input_string:
        print_process(start_state, string, transitions)
        result = hat_delta_nfa(start_state, string, transitions)
        if any(state in accept_states for state in result):
            print(f"String {string} diterima.")
        else:
            print(f"String {string} tidak diterima.")
        print()    

if __name__ == "__main__":
    main()