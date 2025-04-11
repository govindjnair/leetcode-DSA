# in python the built-in algorithm is called Tim Sort.
# Time complexity is O(n log n)


G = [-1, 7, 6, 3, 2, 1, 0]
G.sort()  # In place (constant space)
print(G)

H = [9, -2, 6, 7, 3, 2]
sorted_h = sorted(H)  # Get new sorted array -O(n) space
print(sorted_h)

I = [(7, 2), (3, 5), (2, 6), (1, 8)]  # intervals in leet code

sorted_I = sorted(I, key=lambda t: t[0])  # can do t[1] also
print(sorted_I)

# for sorting backwards
sorted_I_rev = sorted(I, key=lambda t: -t[0])  # can do t[1] also
print(sorted_I_rev)



