from Navigator import Navigator

city_map_list = [
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1]
]

courier_location = (2, 2)
order_locations = [(4, 0), (0, 2), (4, 3)]

navigator = Navigator(city_map_list)

if __name__ == '__main__':
    navigator.find_the_whole_route(courier_location, order_locations)
