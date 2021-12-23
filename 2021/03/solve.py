def read_input(file_path: str) -> list:
    with open(file_path) as file:
        input = [line.strip() for line in file]
    
    return input

def part1(input: list) -> int:
    # think of input as a two dimensional array, because numbers have fixed length
    # row = number, column = bit in number
    
    # initialize a list of 0s, one for each column
    counter_row: list[int] = [0] * len(input[0])
    
    # count 1s per row
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '1': 
                counter_row[j] += 1

    gamma_rate: str = ""
    epsilon_rate: str = ""
    
    for counter in counter_row:
        if counter/len(input) > 0.5:
            gamma_rate += '1'
            epsilon_rate += '0'
        else: 
            gamma_rate += '0'
            epsilon_rate += '1'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

def part2(input: list) -> int:
    # get ratings recursively
    oxygen_generator_rating: int = get_oxygen_generator_rating(input)
    co2_scrubber_rating: int = get_co2_scrubber_rating(input)

    return oxygen_generator_rating * co2_scrubber_rating

def get_oxygen_generator_rating(input: list, row: int = 0) -> int:   
    # count 1s in row
    counter: int = sum(i[row] == '1' for i in input)

    # calculate if 1 or 0 is more frequent
    if counter/len(input) > 0.5:
        most_frequent_bit = '1'
    elif counter/len(input) == 0.5:
        most_frequent_bit = '1'
    else: 
        most_frequent_bit = '0'
        
    # remove numbers starting with frequent bit
    input = [x for x in input if x[row] == most_frequent_bit]
    
    if len(input) == 1:
        return int(input[0], 2)
    else: # next row
        return get_oxygen_generator_rating(input, row+1)

def get_co2_scrubber_rating(input: list, row: int = 0) -> int:   
    # count 1s in first row
    counter: int = sum(i[row] == '1' for i in input)
    
    # calculate if 1 or 0 is less frequent
    if counter/len(input) > 0.5:
        least_frequent_bit = '0'
    elif counter/len(input) == 0.5:
        least_frequent_bit = '0'
    else: 
        least_frequent_bit = '1'

    # remove numbers starting with least frequent bit
    input = [x for x in input if x[row] == least_frequent_bit]

    if len(input) == 1:
        return int(input[0], 2)
    else: # next row
        return get_co2_scrubber_rating(input, row+1)   

if __name__ == "__main__":
    input = read_input('input.txt')

    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')