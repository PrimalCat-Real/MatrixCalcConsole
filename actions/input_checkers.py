from colorama import *


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