def dictCreation(keys, vals):

    if len(keys) == 0 and len(vals) == 0:
        return {}
    else:
        key = keys[0]
        val = vals[0]

        remainingKeys = keys[1:]
        remainingVals = vals[1:]

        result = dictCreation(remainingKeys, remainingVals)
        print(result)

        result[key] = val

        return result





keys = ['a', 'b', 'c']
vals = [1,2,3]

print(dictCreation(keys, vals))

from copy import copy

class P:
  def __init__(self, theName):
    self.name = theName

  def __eq__(self, other):
    return (self.name == other.name)

a = P("Caleb")
b = copy(a)
c = a

print(a==b, a is b, a==c, a is c)


class A:
    def __init__(self, theName):
    self.name = theName

class B:
  def __init__(self, stuff):
     self.data = stuff

x = A("Caleb")
y = B(x)
