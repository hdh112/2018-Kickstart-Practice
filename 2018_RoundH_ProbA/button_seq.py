'''Find allowed button sequence'''
# Date: Nov. 18th, 2018

import math

# Read input file
file_in = open("sample.txt", "r")
file_out = open("output.txt", "w")

# Test cases
T = int(file_in.readline().rstrip())
for test_case in range(T):
    # Test case information
    N, P = [int(s) for s in file_in.readline().rstrip().split()]
    print("N:", N)
    print("P:", P)
    winning = math.pow(2, N)
    for p in range(P):
        prefix = file_in.readline().rstrip()
        print("prefix:", prefix)
        # Subtract forbidden sequences
        if winning > 0:
            winning -= math.pow(2, N-len(prefix))

    file_out.write("Case #%d: %d\n" % (test_case+1, winning))

file_in.close()
file_out.close()