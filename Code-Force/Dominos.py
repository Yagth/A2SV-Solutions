from test import testCase

def numberOfDominos(row, col):
    squares = row * col
    dominos = squares // 2
    return dominos

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
#     }
# ]

# testCase(numberOfDominos, tests)