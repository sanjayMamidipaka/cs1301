def dictCreation(keys, vals):

    if len(keys) == 0 and len(vals) == 0:
        return
    else:
        key = keys[0]
        val = vals[0]

        remainingKeys = keys[1:]
        remainingVals = vals[1:]

        dict = {}
        dict[key] = val
        




keys = ['a', 'b', 'c']
values = [1,2,3]