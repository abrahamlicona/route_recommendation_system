class Help_Functions:
    def __init__(self):
        pass

    def clear_screen(self, n=100):
        """
        Clears the console for better code readability.
        """
        for _ in range(n):
            print(' ')

    def menu(self, title, context, num_options, text_array, option_message="Option: "):
        """
        Creates a default menu when necessary.
        """
        title_length = len(title)
        context_length = len(context)
        side_length = int((context_length - (title_length + 2)) / 2)
        if side_length % 2 == 0:
            side_char = '-' * side_length
            header = f'{side_char} {title.upper()} {side_char}'
            total_char = '-' * (context_length - 1)
        else:
            side_char = '-' * (side_length + 1)
            header = f'{side_char} {title.upper()} {side_char}'
            total_char = '-' * (context_length + 1)
        print(header)
        print(context)
        for i in range(num_options):
            print(f'{i + 1}) {text_array[i]}')
        exit_option = f'{num_options + 1}) Exit'
        print(exit_option)
        print(total_char)
        try:
            menu_option = int(input(option_message))
            return menu_option, num_options + 1
        except:
            print("ERROR...")
            return None, None
        
# Storing class
help_functions = Help_Functions()