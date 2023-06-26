import sys

import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].lstrip('-').isdigit():
            number = int(sys.argv[1])
            if number % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            print("AssertionError: argument is not an integer")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")








#!other way

# if __name__ == "__main__":
    
    
#     if len(sys.argv) == 2:
        
#         number = int(sys.argv[1])
#         assert isinstance(sys.argv[1], int), "Argument is not an integer"
#         try:
#             if number % 2 == 0:
#                 print("I'm Even.")
#             else:
#                 print("I'm Odd.")
#         except ValueError:
#             print("AssertionError: argument is not an integer")
#     elif len(sys.argv) > 2:
#         print("AssertionError: more than one argument is provided")
