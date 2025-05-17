class Navigator:
    def __init__(self, city_map: list[list[int]]):
        self.city_map = city_map

    def find_route(
            self,
            courier_location: tuple[int, int],
            order_location: tuple[int, int],
    ) -> list[tuple[int, int]]:
        """
        route - ordered list of point coordinates from start to end

        :param courier_location: start point coordinates
        :param order_location: end point coordinates
        :return: the route from the start to the end point
        """
        visited = set()
        queue = [courier_location]
        parents = {}

        route = [order_location]
        while queue:
            vertex = queue.pop(0)
            if vertex == order_location:
                break
            neighbours = [(vertex[0], vertex[1] + 1), (vertex[0], vertex[1] - 1), (vertex[0] - 1, vertex[1]),
                          (vertex[0] + 1, vertex[1])]
            for neighbour in neighbours:
                if 0 <= neighbour[0] < len(self.city_map) and 0 <= neighbour[1] < len(self.city_map):
                    if neighbour not in visited and self.city_map[neighbour[1]][neighbour[0]] != 0:
                        queue.append(neighbour)
                        visited.add(neighbour)
                        parents[neighbour] = vertex
        while courier_location not in route:
            route.append(parents[order_location])
            order_location = parents[order_location]
        route.remove(courier_location)
        return route[::-1]

    def find_the_whole_route(
            self,
            courier_location: tuple[int, int],
            order_locations: list[tuple[int, int]],
    ):
        """
        route - ordered list of point coordinates from start to end

        :param courier_location: start point coordinates
        :param order_locations: list of intermediate points coordinates
        :return: the route from start to finish including intermediate points
        """
        route = []
        for order_location in order_locations:
            intermediate_route = self.find_route(courier_location, order_location)
            for point in intermediate_route:
                route.append(point)
            courier_location = order_location
        print(route)
