class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

    def evaluate(self, x_value):
        return x_value


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)

    def evaluate(self, x_value):
        return self.i


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) + self.p2.evaluate(x_value)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) * self.p2.evaluate(x_value)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, (Add, Sub)) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, (Add, Sub)) else repr(self.p2)
        return f"{p1_repr} / {p2_repr}"

    def evaluate(self, x_value):
        denominator = self.p2.evaluate(x_value)
        if denominator == 0:
            raise ValueError("division by zero!")
        return self.p1.evaluate(x_value) / denominator


class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        p1_repr = f"( {repr(self.p1)} )" if isinstance(self.p1, Add) else repr(self.p1)
        p2_repr = f"( {repr(self.p2)} )" if isinstance(self.p2, Add) else repr(self.p2)
        return f"{p1_repr} - {p2_repr}"

    def evaluate(self, x_value):
        return self.p1.evaluate(x_value) - self.p2.evaluate(x_value)

# cs 506 exercise part a
poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)

# cs 506 exercise part b
poly2 = Sub(Div(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly2)

# cs 506 exercise part c
poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))

