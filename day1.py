import csv


# Part 1
def Part1(lst1, lst2):
    # Clone lists so we do not change "master" lists in functions.
    clone1 = lst1[:]
    clone2 = lst2[:]
    
    result = [] 
    clone1.sort() 
    clone2.sort() # Best time complexity possible, O(nlogn)

    for i in range(len(clone1)): # Find distance between each minimum in list
        result.append(abs(clone1[i] - clone2[i])) 

    return result

# Part 2
def Part2(lst1, lst2):
    d = {key: 0 for key in lst1} # Dictionary with each element of list 2 as key with 0 as value, acting like counter
    result = []

    for i in lst2:
        if i in d.keys(): # If the value of list 2 is in keys, add to counter in d
            val = d.get(i)
            d.update({i:val+1})
    
    for i in lst1: # Multiply the elements of the dictionary with the number of times they occur
        result.append(i*d.get(i))

    return result # I know this is bad time complexity, but im not sure how to optimize it.

list1 = []
list2 = []

# Read CSV with input so I dont have to paste 1,000 line list here
with open('AdventOfCode2024\day1.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        list1.append(int(row[0]))
        list2.append(int(row[1]))


print(sum(Part1(list1,list2))) # Print sum of resultant lists
print(sum(Part2(list1,list2)))