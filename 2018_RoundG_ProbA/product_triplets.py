'''Find the number of triplets'''

# Read input file
file_in = open("A-small-practice.in", "r")
file_out = open("A-small-practice.out", "w")

# Test cases
T = int(file_in.readline().rstrip())
for test_case in range(T):
    # Array information
    N = int(file_in.readline().rstrip())
    A = [int(s) for s in file_in.readline().rstrip().split(" ")]

    # Sort array
    A.sort()

    Ax_prev = None; Ay_prev = None; Az_prev = None
    triplets = []
    for x in range(N-2):
        if A[x] == Ax_prev:
            continue
        for y in range(x+1, N-1):
            if A[y] == Ay_prev:
                continue
            for z in range(y+1, N):
                if A[z] == Az_prev:
                    continue
                if A[z] == A[x]*A[y] and not (A[x], A[y], A[z]) in triplets:
                    triplets.append((A[x], A[y], A[z]))
                z_prev = A[z]
            y_prev = A[y]
        x_prev = A[x]
    file_out.write("Case #" + str(test_case+1) + ": " + str(len(triplets)) + "\n")