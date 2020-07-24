#!/usr/bin/python3

'''
Ends in a 4 or 9 -> IV or IX
40 or 90 -> XL or XC
400 or 900 -> CD or CM

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''

big_array = [ 
        [ 1000, 'M'],
        [ 900, 'CM'],
        [ 500, 'D'],
        [ 400, 'CD'],
        [ 100, 'C'],
        [ 90, 'XC'],
        [ 50, 'L'],
        [ 40, 'XL'],
        [ 10, 'X'],
        [ 9, 'IX'],
        [ 5, 'V'],
        [ 4, 'IV'],
        [ 1, 'I']
]

big_dict = { 
        'MM': 2000,
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'CC': 200,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'XX': 20,
        'X' : 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'II': 2,
        'I': 1
}

def num_to_nume(num):
    nume = ''
    arr_ptr = 0
    while num != 0:
        if num - big_array[arr_ptr][0] >= 0:
            nume += big_array[arr_ptr][1]
            num -= big_array[arr_ptr][0]
        else:
            arr_ptr += 1
    return nume

def nume_to_num(nume):
    num = 0
    while len(nume) > 1:
        if nume[:2] in big_dict:
            num += big_dict[nume[:2]]
            nume = nume[2:]
        else:
            num += big_dict[nume[0]]
            nume = nume[1:]
    if len(nume) == 1:
        num += big_dict[nume]
    return num

overall = 0
with open('p089_roman.txt') as f:
    for line in f:
        #print ('###################')
        line = line.strip()
        length = len(line)
        #print(line, " and has ", length, " characters.")
        num = nume_to_num(line)
        #print("It actually is a value of: ", num)
        nume = num_to_nume(num)
        nume_length = len(nume)
        #print("Converted it is: ", nume, " and of length ", nume_length)
        #print("We saved ", length - nume_length, "characters")
        saved = length - nume_length
        overall += saved
print(overall)
