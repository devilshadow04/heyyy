def combine_skeletons(H1, H2):
    result = []
    i, j = 0, 0
    n1, n2 = len(H1), len(H2)

    while i < n1 and j < n2:
        l1, r1, h1 = H1[i]
        l2, r2, h2 = H2[j]

        # Determine which segment to add based on left endpoints
        if r1 <= l2:
            result.append((l1, r1, h1))
            i += 1
        elif r2 <= l1:
            result.append((l2, r2, h2))
            j += 1
        else:
            # Segments overlap
            if l1 == l2:
                if r1 > r2:
                    result.append((l2, r2, max(h1, h2)))
                    H1[i] = (r2, r1, h1)
                    j += 1
                elif r1 == r2:
                    result.append((l1, r1, max(h1, h2)))  # Fixed parenthesis
                    i += 1
                    j += 1
                else:
                    result.append((l1, r1, max(h1, h2)))
                    H2[j] = (r1, r2, h2)
                    i += 1
            elif l1 < l2:
                if h1 >= h2:
                    if r1 <= r2:
                        result.append((l1, r1, h1))
                        if r1 == r2:
                            i += 1
                            j += 1
                        else:
                            H2[j] = (r1, r2, h2)
                            i += 1
                    else:
                        result.append((l1, r2, h1))  # Fixed endpoint
                        H1[i] = (r2, r1, h1)
                        j += 1
                else:
                    result.append((l1, l2, h1))
                    H1[i] = (l2, r1, h1)
            else:
                if h2 >= h1:
                    if r2 <= r1:
                        result.append((l2, r2, h2))
                        if r2 == r1:
                            i += 1
                            j += 1
                        else:
                            H1[i] = (r2, r1, h1)
                            j += 1
                    else:
                        result.append((l2, r1, h2))  # Fixed endpoint
                        H2[j] = (r1, r2, h2)
                        i += 1
                else:
                    result.append((l2, l1, h2))
                    H2[j] = (l1, r2, h2)

    # Append remaining segments
    while i < n1:
        result.append(H1[i])
        i += 1
    while j < n2:
        result.append(H2[j])
        j += 1

    while i < len(result) - 1:
        l0, r0, h0 = result[i]
        l1, r1, h1 = result[i+1]
        if r0 == l1 and h0 == h1:
            result[i] = l0, r1, h0
            result.pop(i+1)
        else:
            i += 1
    return result


def ComputeTopSkeleton(S):
    if len(S) == 1:
        return S

    mid = len(S) // 2

    S1 = S[:mid]
    S2 = S[mid:]

    H1 = ComputeTopSkeleton(S1)
    H2 = ComputeTopSkeleton(S2)

    return combine_skeletons(H1, H2)

# Test the function
S = [(0, 3, 3), (2, 4, 4), (1, 5, 2), (6, 7, 4), (5, 8, 3), (9, 11, 3), (9, 12, 1)]
print(ComputeTopSkeleton(S))
