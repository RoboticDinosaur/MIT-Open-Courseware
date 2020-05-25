# Problem Set 4A
# Name: Robert Forbes
# Collaborators: None
# Time Spent:  Too long.

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

    # Base case
    if len(sequence) == 1:
        return sequence

    # Recursive case
    else:
        result = []
        # for each item in get_permutations(remove first char)
        # "abc"
        head = sequence[0]  # a
        tail = sequence[1:] # bc   <-- By recursion, we permute this
        # permutions of "abc" are the permutations of "bc" with 'a' inserted in all 3 locations
        #
        # get_permutations is provided by others and works.
        # perms = ['bc', 'cb']
        for perms in get_permutations(tail):
            for insert_location in range(len(perms) + 1):
                # Swap the first and last items
                result.append(perms[:insert_location] + head + perms[insert_location:])

        return list(set(result))

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print('----------')

    example_input = 'aaa'
    print('Input:', example_input)
    print('Expected Output:', ['aaa'])
    print('Actual Output:', get_permutations(example_input))
    print('----------')

