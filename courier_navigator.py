def find_way(graph, start, end):
    visited = set()
    queue = [start]
    parents = {}
    route = [end]
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            break
        neibours = [(vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1), (vertex[0] - 1, vertex[1]),
                    (vertex[0] + 1, vertex[1])]
        for neibour in neibours:
            if 0 <= neibour[0] < len(graph) and 0 <= neibour[1] < len(graph):
                if neibour not in visited and graph[neibour[1]][neibour[0]] != 0:
                    queue.append(neibour)
                    visited.add(neibour)
                    parents[neibour] = vertex
    while start not in route:
        route.append(parents[end])
        end = parents[end]
    route.remove(start)
    return route[::-1]


city_map_list = [
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

courier_location = (2, 2)
orders_location = [(4, 0), (0, 2), (4, 3)]

route = []
for order_location in orders_location:
    result_of_function = find_way(city_map_list, courier_location, order_location)
    for i in result_of_function:
        route.append(i)
    courier_location = order_location

print(route)
