from colorama import *
import sys
from termcolor import colored
from pprint import pprint
import inquirer
sys.path.append(".")
from actions import create_matrix as cremx
from actions import sum_up
from actions import multiply


def main():
    pprint("Welcome to MatrixConsoleCalc")
    
    # while not matrix_is_done:
    #     temp_input_matrix = input("Enter matrix line: ")
    #     input_matrix_done[0][0] = temp_input_matrix
    init(autoreset=True) 
    choosing_action = [
        inquirer.List('action',
                    message="What action do you need?",
                    choices=['Determine', 'Sum Up', 'Multiply', 'Find Minor'],
                ),
    ]
    global choosed_action
    choosed_action = inquirer.prompt(choosing_action)
    check_choosed_action()
    # print(colored(choosed_action, 'green'))
   

# распределение действий от выбора
def check_choosed_action():
    if choosed_action['action'] == "Determine":
        print(colored(choosed_action, 'green'))
        # multiply.start_multiply_matrix()
    elif choosed_action['action'] == "Sum Up":
        print(colored(choosed_action, 'green'))
        sum_up.start_sumup_matrix()
    elif choosed_action['action'] == "Multiply":
        multiply.start_multiply_matrix()
        print(colored(choosed_action, 'green'))
    elif choosed_action['action'] == "Find Minor":
        print(colored(choosed_action, 'green'))
    else:
        print('wtf')
    


if __name__ == '__main__':
    main()
    
    
