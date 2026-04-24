# problem-1
# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique
d ={}
for i in range(4):
    name = input(f"Enter a frind name {i+1}:")
    lang = input(f"Enter a language name {i+1}: ")
    # when i write at a two time enter keys so data will show in one time but values will be in two times   
    if name in d:
        d[name].append(lang)
    else:
        d[name] = [lang]
print(d)

# Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "samarth", [1,2]}
    # No, you cannot include a list inside a set in Python.
    # Sets only allow hashable (immutable) items.
    # Lists are mutable → hence, not hashable → so you can’t put a list inside a set.