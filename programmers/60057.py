def compress(s, chunk_size):
    compressed_s = ""
    combo = 0
    latest_chunk = ""
    for i in range(0, len(s), chunk_size):
        chunk = s[i:i + chunk_size]
        if len(chunk) != chunk_size:
            compressed_s += chunk
        elif latest_chunk == chunk:
            combo += 1
        else:
            if combo > 1:
                compressed_s += str(combo) + latest_chunk
            elif combo == 1:
                compressed_s += latest_chunk
            latest_chunk = chunk
            combo = 1
    if combo > 1:
        compressed_s += str(combo) + latest_chunk
    elif combo == 1:
        compressed_s += latest_chunk
    return compressed_s


def solution(s):
    result = len(s)
    for i in range(1, len(s) + 1):
        result = min(result, len(compress(s, i)))
    return result

