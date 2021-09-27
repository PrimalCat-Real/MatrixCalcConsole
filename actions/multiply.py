import numpy as np
import sys
sys.path.append(".")
from actions import create_matrix as cremx
import inquirer
from colorama import *


multiply_more = [
    inquirer.List('multiply_more',
                  message='Do You want multiply more?',
                  choices=['yes', 'no'],
                  default='no'),
]

def start_multiply_matrix():
    A = cremx.FulledMatrix()
    # print(A.create_fulled_matrix())
    matrix_A = A.create_fulled_matrix()
    B = cremx.FulledMatrix() 
    # print(B.count_lines)
    matrix_B = B.create_fulled_matrix()
    # TODO! create class for future use
    if A.count_lines == B.count_columns or A.count_columns == B.count_lines:
        print("work")
        result_matrix = multiply_matrix(matrix_A, matrix_B)
        choosed_more_or_not = inquirer.prompt(multiply_more)
        # TODO! create class for future use
        if choosed_more_or_not["multiply_more"] == "yes":
            multiply_new_matrix = cremx.FulledMatrix()
            multiply_matrix(result_matrix, multiply_new_matrix.create_fulled_matrix())
        else:
            # TODO! Back to choose action func
            pass
    else:
        print(Fore.RED, "not work")
    # print(B.create_fulled_matrix())
    # A.create_fulled_matrix()
    # result_matrix = multiply_matrix(A.create_fulled_matrix(), B.create_fulled_matrix())
    
    
    # B.create_fulled_matrix()
    # if  A.count_lines == B.count_columns:
        
    # else:
    #     print("You cannot")
    
    
def multiply_matrix(A, B):
    result_matrix = A.dot(B) 
    print("It is result")
    print(result_matrix)
    return result_matrix
    