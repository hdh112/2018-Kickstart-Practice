'''Combine classes'''

# Read input file
file_in = open("B-small-practice.in", "r")
file_out = open("B-small-practice-out.txt", "w")

# Test cases
T = int(file_in.readline().rstrip())
for test_case in range(T):
    [N, Q] = [int(s) for s in file_in.readline().rstrip().split(" ")]
    [X_1, X_2, A_1, B_1, C_1, M_1] = [int(s) for s in file_in.readline().rstrip().split(" ")]
    [Y_1, Y_2, A_2, B_2, C_2, M_2] = [int(s) for s in file_in.readline().rstrip().split(" ")]
    [Z_1, Z_2, A_3, B_3, C_3, M_3] = [int(s) for s in file_in.readline().rstrip().split(" ")]

    # X_i, Y_i, Z_i
    X = []; Y = []; Z = []
    X.append(X_1); Y.append(Y_1)
    if N>=2:
        X.append(X_2); Y.append(Y_2)
    if N>=3:
        for i in range(2, N):
            X.append((A_1 * X[i-1] + B_1 * X[i-2] + C_1) % M_1)
            Y.append((A_2 * Y[i-1] + B_2 * Y[i-2] + C_2) % M_2)

    Z.append(Z_1)
    if Q>=2:
        Z.append(Z_2)
    if Q>=3:
        for i in range(2, Q):
            Z.append((A_3 * Z[i-1] + B_3 * Z[i-2] + C_3) % M_3)

    # L_i, R_i, K_i
    L = []; R = []; K = []
    for i in range(N):
        L.append(min(X[i], Y[i])+1)
        R.append(max(X[i], Y[i])+1)
    for i in range(Q):
        K.append(Z[i])

    # Align scores
    scores = []
    for i in range(N):
        scores.extend(range(L[i], R[i]+1))
    scores.sort(reverse=True)

    # Sum of answers
    answers = 0
    for i in range(Q):
        if K[i] < len(scores):
            answer = scores[K[i]]
        else:
            answer = 0
        answers += answer * i

    # Write into file
    file_out.write("Case #" + str(test_case+1) + ": " + str(answers))

file_in.close()
file_out.close()
