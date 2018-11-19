class variable:
    def __init__(self, var):
        self.var = var
        self.fl = var[0]



    def __add__(self, other):
        if other > 0:
            return variable(self.var + '+' + str(other))
        else:
            return variable(self.var + str(other))

    def __sub__(self, other):
        if other > 0:
            return variable(self.var + '-' + str(other))
        else:
            return variable(self.var + '+' + str(-other))

    def __mul__(self, other):
        return variable(self.var + '*' + str(other))

    def __truediv__(self, other):
        return variable(self.var + '/' + str(other))

    def __gt__(self, other):
        return True

    def __lt__(self, other):
        return False

    def calc(self, value):
        return eval(self.var.replace(self.fl, str(value)))

    def __str__(self):
        return self.var

s = variable('s')
s = s + 5 + s
print(s, s.calc(1))