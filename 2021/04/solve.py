def read_input(file_path: str) -> list:
    with open(file_path) as file:
        input = [line.strip() for line in file]
    
    return input

def parse_boards(input: list) -> list:
    board_index: int = 0
    boards: list = [[]]

    for row in range(2, len(input)):
        if input[row] == '':
            board_index += 1
            boards.append([])
            continue
        else:
            boards[board_index].append([[int(x), False] for x in input[row].split()])

    return boards

def mark_number(board: list, number: int) -> None:
    for row in board:
        for tuple in row:
            if tuple[0] == number:
                tuple[1] = True

def bingo(board: list) -> bool:  
    for i in range(len(board)): # row
        row_counter: int = 0
        column_counter: int = 0

        for j in range(len(board[i])): # tuple
            if board[i][j][1] == True:
                row_counter += 1
            if board[j][i][1] == True:
                column_counter += 1
            if row_counter == 5 or column_counter == 5:
                return True
 
    return False

def get_score(board: list, winning_number: int) -> int:
    score: int = 0
    
    for row in board:
        score += sum(tuple[0] for tuple in row if tuple[1] == False)     
    
    return score * winning_number

def part1(input: list) -> int:
    # parse input
    draw_numbers: list = [int(x) for x in input[0].split(',')]
    boards: list = parse_boards(input)

    for number in draw_numbers:
        for board in boards:
            mark_number(board, number)
            if bingo(board):
                return get_score(board, number)

def part2(input: list) -> int: 
    # parse input    
    draw_numbers: list = [int(x) for x in input[0].split(',')]
    boards: list = parse_boards(input)

    for number in draw_numbers:
        for board in boards:
            mark_number(board, number)
            if bingo(board):
                boards.remove(board)
            if len(boards) == 1:
                return get_score(board, number)
        
if __name__ == "__main__":
    input: list = read_input('input.txt')

    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')