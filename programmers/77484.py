def solution(lottos, win_nums):
    lottos = sorted(filter(lambda x: x != 0, lottos))
    chance = 6 - len(lottos)
    win_nums.sort()

    lottos_index = 0
    win_nums_index = 0

    matched_count = 0
    while lottos_index < len(lottos) and win_nums_index < len(win_nums):
        if lottos[lottos_index] == win_nums[win_nums_index]:
            matched_count += 1
            lottos_index += 1
            win_nums_index += 1
        elif lottos[lottos_index] > win_nums[win_nums_index]:
            win_nums_index += 1
        else:
            lottos_index += 1
            
    min_matched_rank = 7 - matched_count if matched_count > 1 else 6
    max_matched_count = 7 - (matched_count + chance) if matched_count + chance > 1 else 6
    return [max_matched_count, min_matched_rank]