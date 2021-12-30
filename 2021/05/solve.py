import math

def read_input(file_path: str) -> list:
    with open(file_path) as file:
        input = [line[:-1].split(" -> ") for line in file]

    for i in range(len(input)):
            input[i] = [list(map(int, value.split(","))) for value in input[i]]
        
    return input

def num_digits(n) -> int:
    if n == 0:
        return 1
    else:
        return int(math.log10(n)+1)

def max_matrix(input: list) -> int:
    max_val: int = 0
    
    for line in input:
        for coordinates in line:
            if max(coordinates) > max_val:
                max_val = int(max(coordinates))
    
    return max_val     

def part1(input: list) -> int:
    # initialize diagram
    max_range: int = 10**num_digits(max_matrix(input))
    diagram: list = [[0 for i in range(max_range)] for j in range(max_range)]
    
    # fill out diagram
    for line in input:
        if line[0][0] == line[1][0] and line[0][1] == line[1][1]: 
            break
        elif line[0][0] == line[1][0]: # x1 = x2
            if line[0][1] < line[1][1]:
                for y in range(line[0][1], line[1][1] + 1):
                    diagram[y][line[0][0]] += 1
            elif line[0][1] > line[1][1]: 
                for y in range(line[0][1], line[1][1] - 1, -1):
                    diagram[y][line[0][0]] += 1
        elif line[0][1] == line[1][1]: # y1 = y2
            if line[0][0] < line[1][0]:
                for x in range(line[0][0], line[1][0] + 1):
                    diagram[line[0][1]][x] += 1
            elif line[0][0] > line[1][0]:
                for x in range(line[0][0], line[1][0] - 1, -1):
                    diagram[line[0][1]][x] += 1

    # count overlaps
    overlap_count: int = 0
    
    for row in diagram:
        for value in row:
            if value >= 2:
                overlap_count += 1
                    
    return overlap_count

def part2(input: list) -> int: 
    # initialize diagram
    max_range: int = 10**num_digits(max_matrix(input))
    diagram: list = [[0 for i in range(max_range)] for j in range(max_range)]
    
    # fill out diagram
    for line in input:
        # x1 == x2 && y1 == y2
        if line[0][0] == line[1][0] and line[0][1] == line[1][1]: 
            break
        
        if line[0][0] == line[1][0]: # x1 = x2
            if line[0][1] < line[1][1]: # y1 < y2
                for y in range(line[0][1], line[1][1] + 1):
                    diagram[y][line[0][0]] += 1
            elif line[0][1] > line[1][1]: # y1 > y2
                for y in range(line[0][1], line[1][1] - 1, -1):
                    diagram[y][line[0][0]] += 1
        elif line[0][1] == line[1][1]: # y1 = y2
            if line[0][0] < line[1][0]: # x1 < x2
                for x in range(line[0][0], line[1][0] + 1):
                    diagram[line[0][1]][x] += 1
            elif line[0][0] > line[1][0]: # x1 > x2
                for x in range(line[0][0], line[1][0] - 1, -1):
                    diagram[line[0][1]][x] += 1
        else: # diagonal
            if line[0][0] < line[1][0]: # x1 < x2
                if line[0][1] < line[1][1]: # y1 < y2
                    for x, y in zip(range(line[0][0], line[1][0] + 1), range(line[0][1], line[1][1] + 1)):
                        diagram[y][x] += 1
                elif line[0][1] > line[1][1]: # y1 > y2
                    for x, y in zip(range(line[0][0], line[1][0] + 1), range(line[0][1], line[1][1] - 1, -1)):                    
                        diagram[y][x] += 1
            elif line[0][0] > line[1][0]: # x1 > x2
                if line[0][1] < line[1][1]: # y1 < y2
                    for x, y in zip(range(line[0][0], line[1][0] - 1, -1), range(line[0][1], line[1][1] + 1)):
                        diagram[y][x] += 1
                elif line[0][1] > line[1][1]: # y1 > y2
                    for x, y in zip(range(line[0][0], line[1][0] -1, -1), range(line[0][1], line[1][1] - 1, -1)):                    
                        diagram[y][x] += 1

    # count overlaps
    overlap_count: int = 0
    
    for row in diagram:
        for value in row:
            if value >= 2:
                overlap_count += 1
                    
    return overlap_count
    
    
if __name__ == "__main__":
    input: list = read_input('input.txt')
    #print(input)

    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')