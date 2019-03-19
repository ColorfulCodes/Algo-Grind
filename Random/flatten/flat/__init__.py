def flat(a):
    result = {}
    # check if value is 

    for i in a:
        if a[i] not in result:
            result[i]




hold = {
        "key1":1,
        "key2": {
            'a': 2,
            'b': 3,
            'c': {
                'd': 3,
                'e': '1'
        }
    }
}

flat(hold)
