

def delta(q, a, transitions):
    return transitions.get((q, a))

def delta_hat(q, w, transitions):
    if not w:  # Empty string (ε)
        return q
    else:
        return delta(delta_hat(q, w[:-1], transitions), w[-1], transitions)

# def process_input(dfa, input_string):
#     transitions, q0, F = dfa
#     final_state = delta_hat(q0, input_string, transitions)
    
#     # Construct the output string
#     output = f"δ̂({q0}, {input_string}) \n= "
    
#     # Add intermediate steps
#     for i in range(len(input_string)):
#         output += f"δ(δ̂({q0}, {input_string[:i]}), {input_string[i]}) \n= "
    
#     # Add final state
#     output += f"δ({final_state}, ε) = {final_state}"
    
#     print(output)
#     return final_state in F

def process_input(dfa, input_string):
    transitions, q0, F = dfa
    
    output = [f"δ̂({q0}, {input_string})"]
    current_state = q0
    
    for i in range(len(input_string) - 1, -1, -1):
        next_state = delta(delta_hat(q0, input_string[:i], transitions), input_string[i], transitions)
        output.append(f"δ(δ̂({q0}, {input_string[:i]}), {input_string[i]}) = {next_state}")
    
    if input_string:
        output.append(f"δ(δ̂({q0}, ε), {input_string[0]}) = {delta(q0, input_string[0], transitions)}")
    output.append(f"δ̂({q0}, ε) = {q0}")
    
    print("\n= ".join(reversed(output)))
    
    final_state = delta_hat(q0, input_string, transitions)
    return final_state in F

def dfa_l1():
    # L1: q0ll strings that start with '10' and end with '01'
    transitions = {
        ('q0', 'ε'): 'q0',
        ('q0', '1'): 'q3',
        ('q0', '0'): 'q1',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q1',
        ('q3', '0'): 'q4',
        ('q3', '1'): 'q1',
        ('q4', '0'): 'q5',
        ('q4', '1'): 'q6',
        ('q5', '0'): 'q5',
        ('q5', '1'): 'q6',
        ('q6', '0'): 'q5',
        ('q6', '1'): 'q4'
    }
    start_state = 'q0'
    accept_states = {'q6'}
    return transitions, start_state, accept_states

def dfa_l2():
    # L2: q0ll strings that contain '000' and end with '1'
    transitions = {
        ('q0', 'ε'): 'q0',
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q0',
        ('q1', '0'): 'q3',
        ('q1', '1'): 'q0',
        ('q3', '0'): 'q4',
        ('q3', '1'): 'q0',
        ('q4', '0'): 'q4',
        ('q4', '1'): 'q5',
        ('q5', '0'): 'q4',
        ('q5', '1'): 'q5'
    }
    start_state = 'q0'
    accept_states = {'q5'}
    return transitions, start_state, accept_states

def dfa_l3():
    # L3: q0ll strings that start and end with a different symbol
    transitions = {
        ('q0', 'ε'): 'q0',
        ('q0', '0'): 'q1',
        ('q0', '1'): 'q4',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q3',
        ('q3', '0'): 'q1',
        ('q3', '1'): 'q3',
        ('q4', '0'): 'q5',
        ('q4', '1'): 'q4',
        ('q5', '0'): 'q5',
        ('q5', '1'): 'q4'
    }
    start_state = 'q0'
    accept_states = {'q3', 'q5'}
    return transitions, start_state, accept_states

def dfa_l4():
    # L4: q0ll strings that start and end with an identical symbol and contain '101'
    transitions = {
        ('q0', 'ε'): 'q0',
        ('q0', '0'): 'q1', 
        ('q0', '1'): 'q8',
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q3',
        ('q3', '0'): 'q4',
        ('q3', '1'): 'q3',
        ('q4', '0'): 'q1',
        ('q4', '1'): 'q5',
        ('q5', '0'): 'q6',
        ('q5', '1'): 'q5',
        ('q6', '0'): 'q6',
        ('q6', '1'): 'q5',
        ('q7', '0'): 'q7',
        ('q7', '1'): 'q8',
        ('q8', '0'): 'q9',
        ('q8', '1'): 'q8',
        ('q9', '0'): 'q7',
        ('q9', '1'): 'q10',
        ('q10', '0'): 'q9',
        ('q10', '1'): 'q10',
    }
    start_state = 'q0'
    accept_states = {'q6', 'q10'}
    return transitions, start_state, accept_states

def nfa_l1():
    # L1: All strings that start with '10' and end with '01'
    transitions = {
        ('q0', '1'): {'q1'},
        ('q1', '0'): {'q2'},
        ('q2', '0'): {'q2'},
        ('q2', '0'): {'q2', 'q3'},
        ('q3', '1'): {'q4'},
    }
    start_state = 'q0'
    accept_states = {'q4'}
    return transitions, start_state, accept_states

def nfa_l2():
    # L2: All strings that contain '000' and end with '1'
    transitions = {
        ('q0', '0'): {'q0', 'q1'},
        ('q0', '1'): {'q0'},
        ('q1', '0'): {'q2'},
        ('q2', '0'): {'q3'},
        ('q3', '0'): {'q3'},
        ('q3', '1'): {'q3', 'q4'},
    }
    start_state = 'q0'
    accept_states = {'q4'}
    return transitions, start_state, accept_states

def nfa_l3():
    # L3: All strings that start and end with a different symbol
    transitions = {
        ('q0', '0'): {'q1'},
        ('q0', '1'): {'q2'},
        ('q1', '0'): {'q1'},
        ('q1', '1'): {'q1', 'q3'},
        ('q2', '0'): {'q2', 'q4'},
        ('q2', '1'): {'q2'},
    }
    start_state = 'q0'
    accept_states = {'q3', 'q4'}
    return transitions, start_state, accept_states

def nfa_l4():
    # L4: All strings that start and end with an identical symbol and contain '101'
    transitions = {
        ('q0', '0'): {'q1'},
        ('q0', '1'): {'q2'},
        ('q1', '0'): {'q1'},
        ('q1', '1'): {'q1', 'q3'},
        ('q3', '0'): {'q5'},
        ('q5', '1'): {'q7'},
        ('q7', '0'): {'q7', 'q9'},
        ('q7', '1'): {'q7'},
        ('q6', '1'): {'q9'},
        ('q7', '1'): {'q10'},
        ('q8', '0'): {'q8'},
        ('q9', '1'): {'q9'},
        ('q2', '0'): {'q4'},
        ('q2', '1'): {'q2'},
        ('q4', '1'): {'q4', 'q8'},
        ('q4', '0'): {'q4'},
        ('q6', '1'): {'q6'},
        ('q8', '0'): {'q6'},
        ('q8', '1'): {'q8'},
        ('q10', '1'): {'q10'},
    }
    start_state = 'q0'
    accept_states = {'q8', 'q9'}
    return transitions, start_state, accept_states

def main():
    dfas = [dfa_l1(), dfa_l2(), dfa_l3(), dfa_l4()]
    dfa_names = ["L1", "L2", "L3", "L4"]

    while True:
        input_string = input("Enter a string of 1's and 0's to check (or 'q' to quit): ")
        if input_string.lower() == 'q':
            break

        for i, dfa in enumerate(dfas):
            print(f"\nChecking {dfa_names[i]}:")
            is_accepted = process_input(dfa, input_string)
            if is_accepted:
                print(f"String is accepted by {dfa_names[i]}")
            else:
                print(f"String is not accepted by {dfa_names[i]}")


if __name__ == "__main__":
    main()
