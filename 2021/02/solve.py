def part1() -> int:

    input = {'forward': 0, 'depth': 0}
    
    with open("input.txt") as file:
        for line in file:
            (key, val) = line.split()
            if(key == "down"): 
                input['depth'] += int(val)
            elif(key == "up"):
                input['depth'] -= int(val)
            else:
                input['forward'] += int(val)
                
    return input['forward'] * (input['depth'])

def part2() -> int:
    input = {'forward': 0, 'depth': 0, 'aim': 0}
    
    with open("input.txt") as file:
        for line in file:
            (key, val) = line.split()
            if(key == "down"): 
                input['aim'] += int(val)
            elif(key == "up"):
                input['aim'] -= int(val)
            else:
                input['forward'] += int(val)
                input['depth'] += input['aim'] * int(val)
                
    return input['forward'] * (input['depth'])
    
if __name__ == "__main__":
   
    print(f'Part1: {part1()}')
    print(f'Part2: {part2()}')