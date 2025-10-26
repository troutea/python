#!/usr/bin/env python3
import sys

def add_command(args):
    #print(args)
    #print(len(sys.argv))
    
    # if len(sys.argv) > 2:
    #      print("Result: ignoring second input")

    #      return

    try:
        # Try to convert the first parameter to an integer
        # if it fails it raises the exception
        int(args)
        n = int(args)
        # Check if the number is in valid range [0..150]
        if 0 <= n <= 150:
            result = n + 1
            print(f"Result: {result}")
            print(result)
            return result
        else: 
            print("Result: Invalid input")
            print("Number out of range")
            return 'Invalid Input'
    except ValueError:
        # Text parameters are unsupported
        print('Invalid Input, Text Characters not supported')      
        return 'Invalid Input Text Characters not supported'
    
    
def main():
        if len(sys.argv) < 2:
            print("Usage: python add3.py <number>") 
            sys.exit(1)
        
        add_command(sys.argv[1])
        
        
        
    
        

# def add_command(args):
#     """
#     Process the 'add' command with the following rules:
#     - Valid inputs are integers in range [0..150]
#     - Returns n+1
#     - Text parameters are unsupported
#     - Additional parameters are ignored
#     - Always produces output without errors
#     """
#     if len(args) < 2:
#         print("Result: Invalid input")
        
    
#     try:
#         # Try to convert the first parameter to an integer
#         n = int(args[1])
        
#         # Check if the number is in valid range [0..150]
#         if 0 <= n <= 150:
#             result = n + 1
#             print(f"Result: {result}")
#             return
#         else:
#             print("Result: Invalid input")
#             return
    
#     except ValueError:
#         # Text parameters are unsupported
#         print("Result: Invalid input")
#         return

# def main():
#     """
#     Main entry point for the script.
#     Expects: python script.py add n
#     """
#     if len(sys.argv) < 2:
#         print("Usage: python script.py add n")
#         return
    
#     command = sys.argv[0] if len(sys.argv) == 1 else sys.argv[1]
    
#     # Check if the command is 'add'
#     if command.lower() == 'add':
#         add_command(sys.argv)
#     else:
#         # If first arg isn't 'add', check if it's in the script name
#         # This handles: python script.py add n
#         add_command(sys.argv)

if __name__ == "__main__":
    
    main()
     
     
         
 
    #total = add_command('a')
     #   print(total)
       
    
     