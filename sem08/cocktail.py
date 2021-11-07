"""
Cocktail shaker sort
input:
  seq: a list of sortable items
output:
  nothing, this function modifies the given list
repeat
  # First loop
  for each element e in seq except the last
      if e is greater than the element after e then
          swap e and the next element
      end if
  end for
  if we did not swap in the loop above then
      break outer loop
  end if

  # Second loop
  for each element e in seq except the last, going backwards
      if e is greater than the element after e then
          swap e and the next element
      end if
  end for
until no swaps took place in the second loop
"""

def cocktail(seq):
    while True:
        swapped = False
        for i in range(len(seq) - 1):
            if seq[i] > seq[i + 1]:
                swapped = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        if not swapped:
            break

        swapped = False
        for i in reversed(range(len(seq) - 1)):
            if seq[i] > seq[i + 1]:
                swapped = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        if not swapped:
            break

l = [5, 4, 3]
cocktail(l)
