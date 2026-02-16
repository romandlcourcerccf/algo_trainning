from collections import defaultdict, deque


def bfs(graph, start_node, end_node):

    q = deque()
    q.append(start_node)

    visited = set()
    track = []
    visited.add(start_node)
    track.append(start_node)

    while q:
        v = q.pop()

        print("v :", v)

        for u in graph[v]:
            if u not in visited:
                if u == end_node:
                    track.append(u)
                    return track

                q.append(u)
                visited.add(u)
                track.append(u)

        print("track :", track)


def main():

    print("-->")

    stations_count = int(input(""))
    lines_count = int(input(""))

    lines_description = defaultdict(list)
    stations_to_lines = defaultdict(set)
    metro_graph = defaultdict(set)

    for line in range(lines_count):
        stations = list(map(int, input("").split()))
        lines_description[line + 1].append(stations)
        for station in stations:
            stations_to_lines[station].add(line + 1)

        for i in range(len(stations)):
            s = stations[i]
            metro_graph[i + 1].add(s)

    nodes = list(map(int, input("").split()))

    print("stations_count :", stations_count)
    print("lines_count :", lines_count)
    print("lines_description :", lines_description)
    print("stations_to_lines :", stations_to_lines)
    print(metro_graph)

    start_node = nodes[0]
    end_node = nodes[1]

    print("start_node : ", start_node, "end_node : ", end_node)

    print(bfs(metro_graph, start_node, end_node))

    print(0)


if __name__ == "__main__":
    main()
