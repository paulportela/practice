

def insertion_sort(a):
    for i in range(1, len(a)):
        current = a[i] # Get element to be sorted
        start = i - 1  # Start by looking here
        while start >= 0 and a[start] > current: # check if 
            a[start+1] = a[start]
            start = start - 1
        a[start + 1] = current
    print a

elements = [5, 3, 2, 4, 10, 8]
insertion_sort(elements)
