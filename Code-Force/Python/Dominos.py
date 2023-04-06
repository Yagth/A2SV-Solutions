# from test import testCase

import sys

def numberOfDominos(row, col):
    squares = row * col
    dominos = squares // 2
    return dominos

# Read input from stdin
input_line = sys.stdin.readline().strip().split()
row, col = int(input_line[0]), int(input_line[1])

# Calculate the number of dominos
dominos = numberOfDominos(row, col)

# Write output to stdout
sys.stdout.write(str(dominos))


# tests = [
#     {
#     'input': {
#         'row': 3,
#         'col': 3
#     }, 
#     'output':4
#     }, 
#     {
#         'input': {
#             'row': 4,
#             'col': 2
#         }, 
#         'output':4
#     },
#     {
#         'input': {
#             'row': 1,
#             'col': 4
#         }, 
#         'output':2
#     }, 
#     {
#         'input': {
#             'row': 6,
#             'col': 1
#         }, 
#         'output':3
#     },
#     {
#         'input': {
#             'row': 2,
#             'col': 4
#         }, 
#         'output':4
#     }
# ]

# testCase(numberOfDominos, tests)