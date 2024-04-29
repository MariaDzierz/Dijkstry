#python code

import heapq

def dijkstra(graf, start):
    drogi = {wierzcholek: float('infinity') for wierzcholek in graf}
    drogi[start] = 0

    priority_queue = [(0, start)]
    while priority_queue:
        obecny_dystans, obecny_wierzcholek = heapq.heappop(priority_queue)
        if obecny_dystans > drogi[obecny_wierzcholek]:
            continue

        for sasiad, waga in graf[obecny_wierzcholek].items():
            droga = obecny_dystans + waga
            if droga < drogi[sasiad]:
                drogi[sasiad] = droga
                heapq.heappush(priority_queue, (droga, sasiad))

    return drogi

if __name__ == "__main__":
    graf = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
}
najkrotsza_droga = dijkstra(graf, 'A')
print(najkrotsza_droga)
#Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
