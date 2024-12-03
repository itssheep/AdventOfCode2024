import re

def Part1():
    pattern = r'mul\((\d+),(\d+)\)' # This is the pattern/template for a valid multiply function
    cleaned = re.findall(pattern, open('AdventOfCode2024\day3.txt').read)
    numbers = [(int(a), int(b)) for a,b in cleaned] # Add all valid entries to a list

    result = 0
    for nums in numbers:
        result += (nums[0]*nums[1]) # Multiply entries of tuples and add them to result

    return result


#Part 2
with open("AdventOfCode2024\day3.txt")as f:print((lambda data,enabled=True:sum([sum([((enabled:=True,0)[1]if data[i:j]=="do()"else((enabled:=False,0)[1]if data[i:j]=="don't()"else(0 if not(enabled and all([(char in "mul(),1234567890")for char in data[i:j]])and(data[i:j].count(",")==1)and(data[i:j].count("(")==1)and(data[i:j].count(")")==1)and(data[i:j].startswith("mul("))and(data[i:j].endswith(")")))else int.__mul__(*list(map(int,data[i+4:j-1].split(",")))))))for j in range(i,min(len(data),i+15))])for i in range(len(data)-15)]))(f.read()))
# THIS IS NOT MY CODE ^^^
# CREDIT TO u/PatattMan on reddit
# https://www.reddit.com/user/PatattMan/
