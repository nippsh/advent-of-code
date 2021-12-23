from solve import part1, part2

INPUT = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".split()

def test_part1():
    assert part1(INPUT) == 198

def test_part2():
    assert part2(INPUT) == 230