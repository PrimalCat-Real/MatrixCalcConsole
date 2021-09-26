import numpy as np
from colorama import *


# TODO вынести в новый файл
# Проверяет евляется ли веденое значение int если нет то отправляет пользователя на доработку
class CheckInput():
    def check_action(self, action, input_line):
        if "Determine" or "Sum Up" or "Multiply" == action:
            self.check_input_value(input_line)         
        else:
            pass
    def check_input_value(self, input_line):
        for element in input_line:
            try:
                int(element)
            except:
                print(f'You have write wrong type element "{Fore.RED + element}{Style.RESET_ALL}" please type new one')
                try:
                    input_line[input_line.index(element)] = int((input("Write new one: ")))
                except:
                    self.check_input_value(input_line)


# Создание нулевой матрицы за параметрами от пользователя
def create_zero_matrix():
    corect = False
    while not corect:
        try:
            count_lines = int(input("How many lines in matrix: "))
            count_columns = int(input("How many columns in matrix: "))
            corect = True
        except ValueError:
            print(Fore.RED, "Value must be number, try again", Style.RESET_ALL)
        
       
    starter_matrix = np.zeros((count_lines, count_columns))
    return starter_matrix, count_lines, count_columns



     
# Заменяет нулевую матрицу значениеми пользователя
def create_fulled_matrix():
    starter_matrix, count_lines, count_columns= create_zero_matrix()
    for i in range(0, count_lines):
        try:
            holder_matrix_line = input(f'Write {i+1}th line: ').split(",")
        except ValueError():
            print("error")
        matrix_line_checker = CheckInput()
        matrix_line_checker.check_action("Determine", holder_matrix_line)  
        for a in range(0, count_columns): 
            try:
                starter_matrix[i][a] = holder_matrix_line[a]
            except:
                # TODO возможно дабавить сообщение надо
                pass
        else:
            pass  
    print(starter_matrix)  
    
     






   