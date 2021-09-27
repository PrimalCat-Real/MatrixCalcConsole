from colorama import *
import sys
import numpy as np
sys.path.append(".")
from actions import create_matrix as cremx


def start_sumup_matrix():
    A = cremx.FulledMatrix()
    matrix_A = A.create_fulled_matrix()
    B = cremx.FulledMatrix() 
    matrix_B = B.create_fulled_matrix()
    sumup_matrix(matrix_A, matrix_B)
    
def sumup_matrix(matrix_A, matrix_B):
    result_matrix = matrix_A + matrix_B
    print("It is result")
    print(result_matrix)
    return result_matrix