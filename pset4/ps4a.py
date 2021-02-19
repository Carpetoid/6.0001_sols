# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    lst_sequence = list(sequence)
    
    if len(sequence) == 1:
        return lst_sequence
    
    return_list = []
    for i in range(len(lst_sequence)):
        copy_seq = lst_sequence.copy()
        current = copy_seq.pop(i)
        perm_table_for_rest = get_permutations(''.join(copy_seq))
        for element in perm_table_for_rest:
            return_list.append(current + element)
            
    return return_list   
        
        
    

if __name__ == '__main__':

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input))
    
    
    example_input = 'olc'
    print('Input:', example_input)
    print('Expected Output:', ['olc', 'ocl', 'loc', 'lco', 'col', 'clo'])
    print('Actual Output:', get_permutations(example_input))
    
    example_input = 'hal'
    print('Input:', example_input)
    print('Expected Output:', ['hal', 'hla', 'ahl', 'alh', 'lha', 'lah'])
    print('Actual Output:', get_permutations(example_input))
    

