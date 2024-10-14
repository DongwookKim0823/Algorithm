def solution(n, costs):
    
    def find_parent(parent, node):
        if parent[node] != node:
            parent[node] = find_parent(parent, parent[node])
        return parent[node]
    
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a > b:
            parent[a] = b
        else:
            parent[b] = a
    
    costs.sort(key=lambda x: x[2])
    parent = {i: i for i in range(n)}
    acc_value = 0
    
    for cost in costs:
        a, b, value = cost
        
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            acc_value += value
            
    return acc_value
