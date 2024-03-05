def find_index_of_kth_occurrence(sequence, element_to_find, occurrence):

    sequence = list(sequence)
    occurrence = int(occurrence)

    # Create a list of the found elements to explore more easily later
    found_items = []
    for i in range(len(sequence)):
        if sequence[i] == element_to_find:
            found_items.append(i)
    
    # If we're trying to find something out of bounds or not in the list, don't!
    if occurrence > len(found_items):
        return(-1)
    else:
        return(found_items[occurrence-1])

def remove_at(sequence, index_to_remove):
    # Remove item from selected sequence at specified index
    updated_sequence = ""
    removed_element = "none"

    for i in range(len(sequence)):

        if i == int(index_to_remove):
            removed_element = sequence[i]
        else:
            updated_sequence += sequence[i]

    return (updated_sequence, removed_element)

def insert_at(sequence, index, element):
    # Insert element in sequence at specified index
    updated_sequence = ""

    for i in range(len(sequence)):
        if i == int(index):
            updated_sequence += element
        updated_sequence += sequence[i]
    
    # If program wants to add in end of sequence, a for loop does not work
    # so add at the end
    if updated_sequence == sequence:
        updated_sequence += element
    
    return(updated_sequence)

def take_from_pillar(state, pillar):
    # Change given state by taking away from given pillar
    index_of_pillar = find_index_of_kth_occurrence(sequence = state, element_to_find = "|", occurrence = int(pillar))
    # "index_of_pillar - 1" to remove the last item on said pillar
    return(remove_at(sequence = state, index_to_remove = index_of_pillar-1))

def put_on_pillar(state, disc, pillar):
    # Change given state by putting given disc on given pillar
    index_of_pillar = find_index_of_kth_occurrence(sequence = state, element_to_find ="|", occurrence = pillar)
    return (insert_at(sequence=state, index=index_of_pillar, element=disc))

def move_one(away, to, state):
    newState, element = take_from_pillar(state, away)
    return(put_on_pillar(newState, element, to))

def move_many(discs, from_pillar, to_pillar, state):
    discs = int(discs)
    if discs == 0:
        return state
    else:
        other_pillar = 6 - int(from_pillar) - int(to_pillar)
        state = move_many(discs - 1, from_pillar, other_pillar, state)

        state = move_one(from_pillar, to_pillar, state)
        print(state)

        state = move_many(discs - 1, other_pillar, to_pillar, state)    
        return(state)