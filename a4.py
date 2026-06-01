def sum(n):
    if n <=0:
        return 0
    return n+sum(n-1)

print("Recursive sum(n-4):",sum(4))

#time complexity=O(4)