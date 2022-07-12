import heapq
from collections import defaultdict


def solution(cacheSize, cities):
    cache = set()
    use_logs = []
    use_log_counts = defaultdict(int)
    answer = 0
    for i, city in enumerate(cities):
        city = city.lower()
        if city in cache:
            answer += 1
            heapq.heappush(use_logs, (i, city))
            use_log_counts[city] += 1
        else:
            answer += 5
            cache.add(city)
            heapq.heappush(use_logs, (i, city))
            use_log_counts[city] += 1
            while len(cache) > cacheSize:
                time, city_to_remove = heapq.heappop(use_logs)
                use_log_counts[city_to_remove] -= 1
                if use_log_counts[city_to_remove] == 0:
                    cache.remove(city_to_remove)
    return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
