def read_input(file_path: str) -> list:
    with open(file_path) as file:
        input = [int(line.strip()) for line in file]
    
    return input

def part1(input: list) -> int:
    counter = 0
    
    for i in range(len(input)):
        try:
            if input[i+1] > input[i]:
                counter += 1
        except:
            return counter

def part2(input: list) -> int:
    counter = 0
    
    for i in range(len(input)):
        try:
            if input[i+1] + input[i+2] + input[i+3] > input[i] + input[i+1] + input[i+2]:
                counter += 1
        except:
            return counter    
    
    return counter    
    
if __name__ == "__main__":
    input = read_input('input.txt')
    
    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')