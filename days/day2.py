def parse_grab(grab):
    cubes = dict()
    for items in grab.split(','):
        cnt, color = items.split()
        cubes[color] = int(cnt)
    return cubes

def parse(inp):
    games = []
    for line in inp.splitlines():
        game_id, grabs = line.split(':')
        game_id = int(game_id.split()[1])
        grabs = [parse_grab(grab) for grab in grabs.split(';')]
        games.append((game_id, grabs))
    return games

def check_grab(target, grab):
    for color, cnt in grab.items():
        if target[color] < cnt:
            return False
    return True

def part1(games):
    game_id_sum = 0
    target = {'red': 12, 'green': 13, 'blue': 14}

    for game_id, grabs in games:
        if all(check_grab(target, g) for g in grabs):
            game_id_sum += game_id

    return game_id_sum

def bag_power(grabs):
    bag = {'red': 0, 'green': 0, 'blue': 0}
    for grab in grabs:
        for color, cnt in grab.items():
            bag[color] = max(bag[color], cnt)
    return bag['red'] * bag['green'] * bag['blue']

def part2(games):
    power_sum = 0
    for _, grabs in games:
        power_sum += bag_power(grabs)
    return power_sum

