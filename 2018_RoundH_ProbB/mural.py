'''Find maximum beauty points'''
# Date: Nov. 18th, 2018
# Running time: O(n)

# Read input file
file_in = open("B-large.in", "r")
file_out = open("output.txt", "w")

# Test cases
T = int(file_in.readline().rstrip())
for test_case in range(T):
    # Test case information
    N = int(file_in.readline().rstrip())
    S = file_in.readline().rstrip()

    # Indices that indicate start & end position of string sequence
    start = 0
    length = int((N+1)/2)
    diffs = 0

    # Search within the string sequence, half its length
    for i in range(int(N/2)):
        # compare start and end values
        diffs += int(S[i+length])
        diffs -= int(S[i])
        if diffs>0: # change start and end
            start = i+1
            diffs = 0

    sum = 0
    # Sum up the beauty points
    for i in range(start, start+length):
        sum += int(S[i])
    file_out.write("Case #%d: %d\n" % (test_case+1, sum))

file_in.close()
file_out.close()