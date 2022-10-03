# Problem Set 4A
# Name: Madhura Baxi


def get_permutations(sequence):
    """ 
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    """
    res = []

    # Base case
    if len(sequence) == 1:
        return [sequence]

    for i in range(len(sequence)):
        char = sequence[0]
        sequence = sequence[1:]
        perms = get_permutations(sequence)

        for j in range(len(perms)):
            perms[j] = perms[j] + char
        res.extend(perms)
        sequence = sequence + char

    return res


if __name__ == '__main__':

    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
