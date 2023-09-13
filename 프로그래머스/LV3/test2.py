def solution(movie):
    from collections import Counter
    d = Counter(movie)
    d = sorted(d.items(), reverse=False)
    d = sorted(d, key=lambda x: x[1], reverse=True)
    # sorted(d.items(), key=lambda x: x[1])
    # answer = list(d.keys())
    return list(dict(d).keys())
print(solution(["spy", "ray", "spy", "room", "once", "ray", "spy", "once"]))