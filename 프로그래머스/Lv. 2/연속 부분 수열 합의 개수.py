def solution(elements):
    candidate = set()
    connected_elements = elements * 2
    for length in range(1, len(elements) + 1):
        for start in range(len(elements)):
            partial_sum = sum(connected_elements[start:start+length])
            candidate.add(partial_sum)

    return len(candidate)
