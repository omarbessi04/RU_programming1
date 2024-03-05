# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5
# Ómar Bessi Ómarsson

# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    # if the relation is reflexive, the following must be true:
    # for every item a in defined_set there will be a vertex (a, a) in relation_on_set
    for item in defined_set:
        # check if an item has it's reflection in the set
        if (item, item) in relation_on_set:
            reflexive_relation = True
        else:
            reflexive_relation = False
            # if there's an item that doesn't have a reflection in the relation, \
            # the relation cannot be reflexive, so break here 
            break

    return reflexive_relation

# Problem 1b)
def is_symmetric(relation_on_set):
    # if the relation is symmetric, the following must be true:
    # it is true for all (a, b) pairs in relation_on_set that another pair, (b, a) also exists in relation_on_set
    for a, b in relation_on_set:
        # check if a pair follows the symmetry rule
        if (b, a) in relation_on_set:
            symmetric = True
        else:
            # if there's a pair that breaks this rule in the relation, the relation cannot be reflexive, so break here 
            symmetric = False
            break
    return symmetric

# Problem 1c)
def is_antisymmetric(relation_on_set):
    # if the relation is antisymmetric, the following must be true:
    # for every (a, b) pair in relation_on_set where there also exists another pair (b, a), the relation is \
    # antisymmetric if and only if a==b
    for a, b in relation_on_set:
        # check if the pair is symmetric
        if (b, a) in relation_on_set:
            if a == b:
                antisymmetric = True
            else:
                # the only instance where a relation is antisymmetric is when there exists two symmetric pairs \
                # (a,b) and (b,a) and b does not equal a. Exactly that has happened if the current a,b pair has \
                # failed the if statement above ("a == b") so the relation can not be antisymmetric
                antisymmetric = False
                return antisymmetric
        else:
            # if an (a,b) pair exists in the relation without a corresponding (b,a) pair, that means nothing 
            # this line is here mostly for empty sets, since they are also antisymmetric
            antisymmetric = True

    return antisymmetric

# Problem 1d)
def is_transitive(relation_on_set):
    # for every (a, b) pair, if (b, c) exists in the list, for the relation to be transative the pair (a, c) must also exist in the relation
    transative = True
    for a, b in relation_on_set:
        # This line will grab the second half of each pair if the first item in that pair is b
        possible_c = [pair[1] for pair in relation_on_set if pair[0] == b]

        # it has no effect on whether a relation is transative if an (a, b) pair exists with no corresponding (b, c) pair
        if len(possible_c) == 0:
            transative = True
        else:
            for possibility in possible_c:
                # if an (a, b) pair has a corresponding (b, c) pair which has a corresponding (a, c) pair, \
                # that means the relation (for now) can be transative
                if (a, possibility) in relation_on_set:
                    transative = True
                    break
                else:
                    # if an (a, b) pair has a corresponding (b, c) pair but no (a, c) pair exists, the set cannot be transative
                    transative = False
                    # here we return transative instead of breaking because we are inside a nested for-loop
                    return transative
    
    return transative

# Problem 2
def is_equivalence_relation(defined_set, relation_on_set):
    # for a relation of a set to be equivalent, it must be reflexive, symmetric and transative

    # check if the relation is reflexive
    is_relation_reflexive = is_reflexive(defined_set, relation_on_set)
    # check if the relation is symmetric
    is_relation_symmetric = is_symmetric(relation_on_set)
    # check if the relation is transative
    is_relation_transitive = is_transitive(relation_on_set)

    # if the relation is all three, then it is equivalent
    if is_relation_reflexive and is_relation_symmetric and is_relation_transitive:
        relation_is_equivalent = True
    else:
        relation_is_equivalent = False

    return relation_is_equivalent

# Problem 3
def composite_relations(relation1, relation2):
    # let's say A is a set of teachers, B is a set of college courses, and C is a set of students
    # let's also presume that a relation R exists between A and B where (a, b) is a part of R (which teacher is teaching which course)
    # let's also presume that a relation S exists between B and C where (b, c) is a part of S (what course is which student taking)
    # the composite of those relations would say which teacher is teaching which student, or (a, c)

    # we start with an empty list where our composites will go
    composite = []
    for a, b1 in relation1:
        for b2, c in relation2:
            # check if the last item in the first pair is the same as the first item in the current pair
            # in the example, this would be checking if the courses match
            if b1 == b2:
                if (a,c) not in composite:
                    # in this problem, we care about the order of the compsite
                    # so we use a list here instead of a set and just check if the (a, c) pair is already in the list
                    composite.append((a, c))
    return composite

# Problem 4a)
def aces_in_relation_a(A):
    # the relation R will only ever include the integer 0, so there will never be aces in the matrix of this relation
    return 0

# Problem 4b)
def aces_in_relation_b(A): 
    # first create the given relation, then count the number of items in that relation
    relation = []
    for item in A:
        # for every item in A, create a tuple (a, b) where a = b + 1, \
        # then add it to the larger list of these tuples
        new_relation = (item, item+1)
        relation.append(new_relation)

    # in this problem, the number of aces will always be the same as the number of items in the tuple list - 1
    return len(relation)-1

# Problem 4c)
def aces_in_relation_c(A):
    # in this problem we can simply return the sum of set A
    # if we go through the set, it starts at 1 and goes up to n, so count up from 1
    # how many numbers in the set is 1 bigger than on equal to? there's only one number, 1, it is equal to itself and larger than nothing
    # the next number is 2, which is bigger than 1 and equal to itself, so a total of two numbers are smaller or equal to 2
    # the next is 3 which is bigger than 2 and 1 and equal to itself...
    # this continues until we reach n, which will be larger than all other numbers, and equal to itself
    # therefore, each number in the set will add a number of (a, b) pairs equal to itself, so we can simply get the sum of the set itself
    return sum(A)

# Problem 4d)
def aces_in_relation_d(A):
    # first create the given relation, then count the number of items in that relation
    relation = []
    for item in A:
        # for each item in the set A, we can check if a pair exists for that item by subtracting 1000 by that item
        # the item plus the nex item should be equal to 1000
        # since the list goes from 1 to n with no duplicates, there will always just be one number that the item can be added to \
        # so there's no need to do anything special here
        if 1000-item in A:
            relation.append((item, 1000-item))
    
    return len(relation)

# Problem 4 e)
def aces_in_relation_e(A):
    # first create the given relation, then count the number of items in that relation
    relation = []
    for item1 in A:
        for item2 in A[::-1]:
            # go both forwards (item1) and backwards (item2) through the given set A

            if item1 + item2 >= 1001:
                # if the addition of the numbers is bigger than or equal to 1001, add it to the list
                # also, check if we've previously added this pair to the relation list, \
                # (586 + 685) is larger than 1001, but so is (685 + 586), we only want to count this pair once
                if not((item1, item2) in A or (item2, item1) in A):
                    relation.append((item1, item2))
            else:
                # if item1 + item2 is ever less than 1001, \
                # the next value associated with item2 will be x-1 where x is the current value of item2
                # this new value of item2 will be smaller than the current value of item2
                # so that item1 + item2 will also be smaller than 1001
                # this program is already in O(n**2) so we can cut down on a little time by breaking here
                break

    return len(relation)