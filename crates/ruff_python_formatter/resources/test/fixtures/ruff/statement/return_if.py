def foo():
    if 1 == 2:
        return
    if 1 == 2: # trailing comment
        return
    if 1 == 3: return True
    if aaaaaaaaaaaaaaaaaaaaa() and bbbbbbbbbbbbbbbbbb() and ccccccccccccccccccccccccccccccccc(): return
    for i in range(1000): return
    if foo:
        return
    else:
        return
    if bar:
        return
    elif foo:
        return
