
OP_ = {
    (0, 0): 0,
    (1, 1): 1,
    (2, 2): 2,
    (1, 2): 0,
    (1, 0): 2,
    (2, 1): 0,
    (2, 0): 1,
    (0, 1): 2,
    (0, 2): 1,
}

def op(x, y):
    return OP_[(x, y)]



class Card:

    def __init__(self, *attrs):
        self.attrs = attrs

    def __add__(self, other):
        if other == self:
            return E
        elif other == E:
            return self
        elif self == E:
            return other
        else:
            return Card(*(op(a, b) for a, b in zip(self.attrs, other.attrs)))
            
    def __repr__(self):
        return "Card" + str(self.attrs) 

    def __str__(self):
        return str(self.attrs)

    def __eq__(self, other):
        return self.attrs == other.attrs

    def __neg__(self):
        return self

    def __sub__(self, other):
        return self + (-other)


E = Card(-1)


if __name__ == "__main__":

    A, B, C = Card(0,0), Card(0, 1), Card(0, 2)
    D, F, G = Card(1,0), Card(1, 1), Card(1, 2)
    H, I, J = Card(2,0), Card(2, 1), Card(2, 2)

    # it's not associative
    assert (A + D) + G != A + (D + G)

    # it's order 2
    assert A + A == E
    assert B + B == E

    # it's abelian
    assert A + B == B + A

