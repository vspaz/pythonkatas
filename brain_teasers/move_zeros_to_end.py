lyst = [0, 0, 10, 0, 1, 0, 20, 30, 0, 0]
lyst_length = len(lyst)
lyst = [i for i in lyst if i != 0]
new_lyst_length = len(lyst)
lyst += [0] * (lyst_length - new_lyst_length)
print(lyst)
