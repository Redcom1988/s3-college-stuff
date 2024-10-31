def dfa_l1():
    # L1: All strings that start with '10' and end with '01'
    transitions = {
        ('Q0', '1'): 'Q2',
        ('Q0', '0'): 'Q1',
        ('Q1', '0'): 'Q1',
        ('Q1', '1'): 'Q1',
        ('Q2', '0'): 'Q3',
        ('Q2', '1'): 'Q1',
        ('Q3', '0'): 'Q4',
        ('Q3', '1'): 'Q5',
        ('Q4', '0'): 'Q4',
        ('Q4', '1'): 'Q5',
        ('Q5', '0'): 'Q4',
        ('Q5', '1'): 'Q3'
    }
    start_state = 'Q0'
    accept_states = {'Q5'}
    return transitions, start_state, accept_states

def dfa_l2():
    # L2: All strings that contain '000' and end with '1'
    transitions = {
        ('Q0', '0'): 'Q1',
        ('Q0', '1'): 'Q0',
        ('Q1', '0'): 'Q2',
        ('Q1', '1'): 'Q0',
        ('Q2', '0'): 'Q3',
        ('Q2', '1'): 'Q0',
        ('Q3', '0'): 'Q3',
        ('Q3', '1'): 'Q4',
        ('Q4', '0'): 'Q3',
        ('Q4', '1'): 'Q4'
    }
    start_state = 'Q0'
    accept_states = {'Q4'}
    return transitions, start_state, accept_states

def dfa_l3():
    # L3: All strings that start and end with a different symbol
    transitions = {
        ('Q0', '0'): 'Q1',
        ('Q0', '1'): 'Q3',
        ('Q1', '0'): 'Q1',
        ('Q1', '1'): 'Q2',
        ('Q2', '0'): 'Q1',
        ('Q2', '1'): 'Q2',
        ('Q3', '0'): 'Q4',
        ('Q3', '1'): 'Q3',
        ('Q4', '0'): 'Q4',
        ('Q4', '1'): 'Q3'
    }
    start_state = 'Q0'
    accept_states = {'Q2', 'Q4'}
    return transitions, start_state, accept_states

def dfa_l4():
    # L4: All strings that start and end with an identical symbol and contain '101'
    transitions = {
        ('Q0', '0'): 'Q1', 
        ('Q0', '1'): 'Q7',
        ('Q1', '0'): 'Q1',
        ('Q1', '1'): 'Q2',
        ('Q2', '0'): 'Q3',
        ('Q2', '1'): 'Q2',
        ('Q3', '0'): 'Q1',
        ('Q3', '1'): 'Q4',
        ('Q4', '0'): 'Q5',
        ('Q4', '1'): 'Q4',
        ('Q5', '0'): 'Q5',
        ('Q5', '1'): 'Q4',
        ('Q6', '0'): 'Q6',
        ('Q6', '1'): 'Q7',
        ('Q7', '0'): 'Q8',
        ('Q7', '1'): 'Q7',
        ('Q8', '0'): 'Q6',
        ('Q8', '1'): 'Q9',
        ('Q9', '0'): 'Q8',
        ('Q9', '1'): 'Q9',
    }
    start_state = 'Q0'
    accept_states = {'Q5', 'Q9'}
    return transitions, start_state, accept_states

def delta_dfa(state, symbol, transitions):
    return transitions.get((state, symbol))

def hat_delta_dfa(state, input_string, transitions):
    if len(input_string) == 0:
        return state
    else:
        a, x = input_string[-1], input_string[:-1]
        next_state = hat_delta_dfa(state, x, transitions)
        result = delta_dfa(next_state, a, transitions)
        return result

def print_process(state, input_string, transitions):
    if not input_string:
        print(f"δ^({state}, ε)")
        print(f"= {state}")
        return state

    print(f"δ^({state}, {input_string})")
    
    curr_string = input_string
    while curr_string:
        deltas = 'δ(' * (len(input_string) - len(curr_string) + 1)
        remaining = curr_string[:-1] if len(curr_string) > 1 else 'ε'
        print(f"= {deltas}δ^({state}, {remaining})", end='')
        for symbol in input_string[len(curr_string)-1:]:
            print(f", {symbol}", end='')
        print(")")
        curr_string = curr_string[:-1]
    
    current_state = state
    states = []
    for i, symbol in enumerate(input_string):
        deltas = 'δ(' * (len(input_string) - i)
        current_state = transitions.get((current_state, symbol), current_state)
        states.append(current_state)
        print(f"= {deltas}{current_state}", end='')
        for symbol in input_string[i+1:]:
            print(f", {symbol}", end='')
        print(")")

    print(f"= {current_state}")
    return current_state

def main(): 
    # L1: All strings that start with '10' and end with '01'
    # L2: All strings that contain '000' and end with '1'
    # L3: All strings that start and end with a different symbol
    # L4: All strings that start and end with an identical symbol and contain '101'

    # l1 accept
    transitions, start_state, accept_states = dfa_l1()
    input_string = '101101101'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l1()
    input_string = '101001101'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    #l1 reject
    transitions, start_state, accept_states = dfa_l1()
    input_string = '01000010'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")
    
    transitions, start_state, accept_states = dfa_l1()
    input_string = '101000010'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")


    #l2 accept
    transitions, start_state, accept_states = dfa_l2()
    input_string = '110001001'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l2()
    input_string = '110000011'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    #l2 reject
    transitions, start_state, accept_states = dfa_l2()
    input_string = '11000100'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l2()
    input_string = '11001101'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")


    #l3 accept
    transitions, start_state, accept_states = dfa_l3()
    input_string = '10101010'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l3()
    input_string = '01110111'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    #l3 reject
    transitions, start_state, accept_states = dfa_l3()
    input_string = '11010111'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l3()
    input_string = '01010110'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")


    #l4 accept
    transitions, start_state, accept_states = dfa_l4()
    input_string = '110101101'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l4()
    input_string = '010101010'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    #l4 reject
    transitions, start_state, accept_states = dfa_l4()
    input_string = '111010110'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

    transitions, start_state, accept_states = dfa_l4()
    input_string = '110011001'
    print_process(start_state, input_string, transitions)
    result = hat_delta_dfa(start_state, input_string, transitions)
    print(f"Result: {'Accepted' if result in accept_states else 'Rejected'}\n")

if __name__ == "__main__":
    main()