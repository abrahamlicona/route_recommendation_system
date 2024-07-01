import time
from help_functions import *
from prob_functions import *
from trajectories import trajectories
from trajectories import length_n
from trajectories import valid_nodes


class Menus:
    def __init__(self):
        self.trajectories = trajectories
        self.valid_nodes = valid_nodes
        self.route_length = length_n
    
    def route_menu(self):
        """
        Creates Route Menu.
        """
        while True:
            try:
                input_route = input('Please enter the route separated by commas or write "exit" to exit: ')
                if input_route.lower() == 'exit':
                    time.sleep(2)
                    help_functions.clear_screen()
                    break
                else:
                    route = input_route.split(",")
                    if len(route) >= self.route_length:
                        print(f'Error: Input length needs to be smaller than {self.route_length}')
                        time.sleep(2)
                        help_functions.clear_screen()
                    else:
                        for node in route:
                            if node  not in self.valid_nodes:
                                print('Error: There is one or more elements that are not on the valid nodes.')
                                time.sleep(2)
                                help_functions.clear_screen()
                                return None
                        print(probability_functions.find_recommendation(route))
                        while True:
                            add_option = input('Would you like to enter another node to the route? [Y/N]: ')
                            if add_option.upper() == 'Y':
                                try:
                                    new_node = input('Enter the new node: ')
                                    if new_node not in self.valid_nodes:
                                        print("The new node is not on the valid nodes.")
                                        time.sleep(2)
                                        help_functions.clear_screen()
                                        break
                                    else:
                                        route.append(new_node)
                                        if len(route) > self.route_length:
                                            print(f'Route length needs to be smaller than {self.route_length}')
                                            time.sleep(2)
                                            help_functions.clear_screen()
                                            break
                                        else:
                                            print(probability_functions.find_recommendation(route))
                                except:
                                    print('ERROR...')

                            elif add_option.upper() == 'N':
                                help_functions.clear_screen()
                                break
                            else:
                                print("Invalid option.")
            except:
                print("ERROR...")   

    def main_menu(self):
        """
        Creates Main Menu. 
        """
        while True:
            selected_option, exit_option = help_functions.menu("Main menu", "Please select one of the following options", 1, ['Enter a route'])
            if selected_option == exit_option:
                help_functions.clear_screen()
                break
            elif selected_option == 1:
                help_functions.clear_screen()
                self.route_menu()
            else:
                print("ERROR, invalid input...")


if __name__ == "__main__":
    menus = Menus()
    main_menu = menus.main_menu()                       

                            
