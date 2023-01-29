def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        print('in the while loop vertex: {0} - path: {1}'.format(vertex,path))
        for next in graph[vertex]:
            if next == goal:
            	tmp=path+[next]
            	return path + [next]
            else:
                stack.append((next, path + [next]))
                print('else branch print {}'.format(stack))


# graph
g = { "a" : set(["c","b"]),
      "b" : set(["d","f"]),
      "c" : set(["e"]),
      "d" : set([]),
      "e" : set([]),
      "f" : set([])
    }

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}   

print(dfs_paths(g,'a','d'))