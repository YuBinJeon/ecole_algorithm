from collections import deque, defaultdict


def solution(n, vertex):
    graph = defaultdict(list)
    for u, v in vertex:
        graph[u].append(v)
        graph[v].append(u)  
    distances = [-1] * (n + 1)  
    distances[1] = 0  
    queue = deque([1])
    
    while queue:
        current_node = queue.popleft()
        current_distance = distances[current_node]  
        for neighbor in graph[current_node]:
            if distances[neighbor] == -1:
                distances[neighbor] = current_distance + 1
                queue.append(neighbor)

    max_distance = max(distances) 
    return distances.count(max_distance)
