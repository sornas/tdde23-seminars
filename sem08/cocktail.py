def cocktail(seq):
    # repeat
    while True:
        swapped = False
        # for each element e in seq except the last
        for i in range(len(seq) - 1):
            # if e is greater than the element after e then
            if seq[i] > seq[i + 1]:
                # swap e and the next element
                swapped = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
            # end if
        # end for
        # if we did not swap in the loop above then
        if not swapped:
            # break outer loop
            break
        # end if

        swapped = False
        # for each element e in seq except the last, going backwards
        for i in reversed(range(len(seq) - 1)):
            # if e is greater than the element after e then
            if seq[i] > seq[i + 1]:
                # swap e and the next element
                swapped = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
            # end if
        # end for
        # until no swaps took place in the second loop
        if not swapped:
            break

l = [5, 4, 3]
cocktail(l)
print(l)
