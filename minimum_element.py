""" Printing minimum element of the values enetered in the console"""

class Minimum_Element:

    def print_minimum_element(self):
        while True:
            try:
                self.elements = int(input('How many elements will be entered? >>> '))
                self.list_elements = []
                for element in range(self.elements):
                    entered_elements = input(f'Enter {element + 1}. number >>> ')
                    for i in entered_elements:
                        self.list_elements.append(i)
                print('Minimum value = ' + min(self.list_elements))
                break
            except ValueError:
                print('Wrong value. Please enter integer number. ')
            

# %%
minimum_element = Minimum_Element() 
minimum_element.print_minimum_element()       
