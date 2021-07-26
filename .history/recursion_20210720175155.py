def dictCreation(keys, vals):

    if len(keys) == 0 and len(vals) == 0:
        return {}
    else:
        key = keys[0]
        val = vals[0]

        remainingKeys = keys[1:]
        remainingVals = vals[1:]

        result = dictCreation(remainingKeys, remainingVals)

        result[key] = val
        





keys = ['a', 'b', 'c']
vals = [1,2,3]

print(dictCreation(keys, vals))