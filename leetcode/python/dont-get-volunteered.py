def answer(start, destination):
    steps = 0
    if start == destination:
        return steps
    queue = [start]
    visited = set()

    while queue:
        size = len(queue)
        steps += 1
        while size:
            size -= 1
            current = queue[0]
            queue = queue[1:]
            if current in visited:
                continue
            visited.add(current)

            line = int(current / 8)
            h_start, h_end = line * 8, (line + 1) * 8 - 1
            for d in (-2, +2):
                if current + d < h_start or current + d > h_end:
                    continue
                for k in (-8, +8):
                    next = current + d + k
                    if next in visited or next < 0 or next > 63:
                        continue
                    if next == destination:
                        return steps
                    queue.append(next)

            for d in (-16, +16):
                if current + d < 0 or current + d > 63:
                    continue
                for k in (-1, +1):
                    next = current + d + k
                    if next in visited or current + k < h_start or current + k > h_end:
                        continue
                    if next == destination:
                        return steps
                    queue.append(next)

    return steps


print(answer(0, 1))
print(answer(19, 36))
print(answer(0, 0))
