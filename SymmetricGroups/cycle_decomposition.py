'''
Will write a program to implement an algorithm to find the cycle decompostion
of a permumtation in a Symmetric group S_n
----------------------------------------------------------------------------
| Method:                                           Example:               |
|1) to start a new cycle pick the smallest elt of   (1                     |                                               
|{1,2,..,n} which hasn't appeared in a prev cycle                          |                                                 
|call it a write (a to start.                                              |
|                                                                          |             
|--------------------------------------------------------------------------|                                                                  
|2) Read off o(a) call it b if b == a close the cycle Example:             |
|with parantheses then return to step 1: if b != a    o(1) = 12 != 1       |
|then write b next to a: (a b                         (1 12                |                                              
|                                                                          |         
|--------------------------------------------------------------------------|                                                         
|3) Read off o(b) call it c if c == a close the cycle Example:             |
|go back to step 1) else write c next to b: (a b c     o(12) = 8 != 1      |           
|repeat this step using c as the new b (i.e read o(c)                      |                                                                 
|do this until the cycle closes                       (1 12 8 ..)          |                                                              
|                                                                          |                         
----------------------------------------------------------------------------    
Reference: Abstract Algebra, Dummit and Foote Third Edition
'''
def is_valid_perm(N, S):
    if len(N) != len(S):
        return False
    elif sorted(N) != sorted(S):
        return False
    else:
        return True

def cycle_it(perm):
    '''
    given a permuation S on the set n
    find the cycle decompostion
    note for n_i in N o(n_i) = S_i
    where indices match.
    Note you can use the permuation library from python this is just for fun
    '''
    # check validity
    if not is_valid_perm(perm[0], perm[1]):
        raise ValueError('Input perm not valid')
    maps = { a: b for a, b in zip(*perm) }
    cycles = []
    for a in perm[0]:
        b = maps.pop(a, None)
        if b is None:
            continue # `a` has already been handled
        cycle = [a]
        while a != b:
            cycle.append(b)
            b = maps.pop(b)
        cycles.append(cycle)
    return cycles

if __name__ == "__main__":
    print("This is the permutations before it's decomposed\n")
    perm = [[1, 2, 3, 4, 5], [3,4,5,2,1]]
    for row in perm:
        print('(', *perm[0], ')')
    print('\n')
    cycles = cycle_it([[1, 2, 3, 4, 5], [3,4,5,2,1]])
    print("This is the permutations before written as a product of disjoint cycles\n")
    for row in cycles:
        print("(", *row, ")", end="")
    print('\n')



