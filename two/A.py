def combinations_with_repetition(head, choose_k):        
    return combinations(head, choose_k, repetitions=True)

def combinations(head, choose_k, repetitions=False):
    combos = []
    if not choose_k: #base case
        return [()]
    for i in range(len(head)):
        if repetitions: 
            tails = combinations(head[i:], choose_k-1, repetitions) #includes current element and every element after
        else:      
            tails = combinations(head[i+1:], choose_k-1, repetitions) #includes elements after current
        for tail in tails:
            combos.append((head[i],)+tail)
    return combos

###

def permutations(head):
    return variations(head, len(head))

def permutations_with_repetition(head):
    return variations(head, len(head), repetitions=True)

def variations_with_repetition(head, choose_k):        
    return combinations(head, choose_k, repetitions=True)

def variations(head, choose_k, repetitions=False):
    variats = []
    if not choose_k: #base case
        return [()]
    for i in range(len(head)):
        if repetitions: 
            tails = variations(head, choose_k-1, repetitions)
        else:      
            tails = variations(head[:i]+head[i+1:], choose_k-1, repetitions)
        for tail in tails:
            variats.append((head[i],)+tail)
    return variats