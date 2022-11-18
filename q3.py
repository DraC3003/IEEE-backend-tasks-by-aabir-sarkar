dictionary = {}
for i in range(4):
    subject = str(input(" key : "))  # accepting the user's input
    marks = int(input("value : "))
    dictionary[subject] = marks


print(sorted(dictionary.items()))

value_key_pairs = ((value, key) for (key, value) in dictionary.items())
sorted_value_key_pairs = sorted(value_key_pairs, reverse=True)
sorted_value_key_pairs


{k: v for v, k in sorted_value_key_pairs}
