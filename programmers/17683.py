def time_str_to_int(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute


sheet_map = {
    'C': '0',
    'C#': '1',
    'D': '2',
    'D#': '3',
    'E': '4',
    'E#': 'c',
    'F': '5',
    'F#': '6',
    'G': '7',
    'G#': '8',
    'A': '9',
    'A#': 'a',
    'B': 'b'
}


def convert_sheet(sheet):
    index = 0
    result = ''
    while index < len(sheet):
        note = sheet[index]
        index += 1
        if index < len(sheet) and sheet[index] == '#':
            note += '#'
            index += 1
        result += sheet_map[note]
    return result

def solution(m, musicinfos):
    matched_musics = []
    m = convert_sheet(m)
    for musicinfo in musicinfos:
        start_time, end_time, title, sheet = musicinfo.split(',')
        start_time = time_str_to_int(start_time)
        end_time = time_str_to_int(end_time)
        play_time = end_time - start_time
        sheet = convert_sheet(sheet)
        played_music = ''
        played_music += sheet * (play_time // len(sheet))
        left_note = play_time % len(sheet)
        for note in sheet:
            played_music += note
            if note != '#':
                left_note -= 1
            if left_note == 0:
                break
        if m in played_music:
            matched_musics.append((play_time, title))
    if len(matched_musics) == 0:
        return "(None)"

    result = "(None)"
    max_play_time = -1
    for matched_music in matched_musics:
        if matched_music[0] > max_play_time:
            max_play_time = matched_music[0]
            result = matched_music[1]
    return result

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
