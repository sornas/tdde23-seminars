def line(a, b, c):
    return a

def triangle(a, b, c):
    return not (a and b and c) and (a or b or c)

def triangle(a, b, c):
    return not a == b == c

def around(seq, i):
    assert len(seq) > 1
    if i == 0:
        return [False, seq[i], seq[i + 1]]
    elif i == len(seq) - 1:
        return [seq[i - 1], seq[i], False]
    else:
        return seq[i-1:i+2]

def next_state(seq, pred):
    new = []
    for i in range(len(seq)):
        left, this, right = around(seq, i)
        new.append(pred(left, this, right))
    return new

def next_state(seq, pred):
    return [pred(*around(seq, i)) for i in range(len(seq))]

def print_state(seq):
    state = ""
    for alive in seq:
        if alive:
            state += "x"
        else:
            state += " "
    print(state)

if __name__ == "__main__":
    seq = [i == 40 for i in range(80)]

    print_state(seq)
    for i in range(39):
        seq = next_state(seq, triangle)
        print_state(seq)
