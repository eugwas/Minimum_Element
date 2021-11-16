""" Printing minimum element of the values enetered in the console"""


def print_minimum_element():
    while True:
        try:
            elements = int(input('How many elements will be entered? >>> '))
            list_elements = []
            for element in range(elements):
                entered_elements = input(f'Enter {element + 1}. number >>> ')
                for i in entered_elements:
                    list_elements.append(i)
            print('Minimum value = ' + min(list_elements))
            break
        except ValueError:
            print('Wrong value. Please enter integer number. ')
            
print_minimum_element()