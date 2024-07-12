def d(graph, start):
    visit = set()
    
    def dfs(node):
        if node in visit:
            return
        visit.add(node)
        for neighbor in graph[node]:

            dfs(neighbor)
    
    dfs(start)
    return visit

# Graph representation
graph = {

    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['A', 'B'],  # Cycle A -> B -> C -> A
}


# Start DFS from node 'A'
visited_nodes = d(graph, 'A')
print(visited_nodes)