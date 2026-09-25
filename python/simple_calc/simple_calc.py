# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Simple Calculator
--------------------------------------------------------------------------
License:   
Copyright 2026 - Randy Casas Alvarez

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple calculator that will 
  - Take in two numbers from the user
  - Take in an operator from the user
  - Perform the mathematical operation and provide the number to the user
  - Repeat

Operations:
(Base)
  - "+" : addition
  - "-" : subtraction
  - "*" : multiplication
  - "/" : division
(Additional)
  - ">>": right shift
  - "<<": left shift
  - "%" : modulo
  - "**": exponentiation

Error conditions:
  - Invalid operator --> Program should exit
  - Invalid number   --> Program should exit

--------------------------------------------------------------------------
"""

# NOTE - Add import statements to allow access to Python library functions
#        Hint:  Look at https://docs.python.org/3/library/operator.html
import operator


# ------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------

# NOTE - No constants are needed for this example 

# ------------------------------------------------------------------------
# Global variables
# ------------------------------------------------------------------------

# NOTE - Global variable to map an operator string (e.g. "+") to 
#        the appropriate function.
operators = {
    # Dictionary syntax:  "key" : "value"
    #   i.e. "function" : operator.<function>
    
    # Base operations
    "+" : operator.add,
    "-" : operator.sub,
    "/" : operator.truediv,
    "*" : operator.mul,
    
    # Additional operations
    ">>" : operator.rshift,
    "<<" : operator.lshift,
    "%"  : operator.mod,
    "**" : operator.pow,
    
}

# Python 2 backwards-compatibility
# bind Python 2's "raw_input" function to Python 3's "input"
try:
    input = raw_input
except NameError:
    pass



# ------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------

def get_user_input():
    """ Get input from the user.
        Returns tuple:  (number, number, function) or 
                        (None, None, None) if inputs invalid
    """
    # NOTE - Use "try"/"except" statements to handle errors gracefully.      
    try:
        num1 = float(input("\nEnter 1st number: "))
        num2 = float(input("Enter 2nd number: "))
        op   = input("Enter operation ( + , - , * , / , >> , << , % , ** ): ")
        
        # rshift and lshift do not work on float types
        if (">>" in op) or ("<<" in op):
            num1 = int(num1)
            num2 = int(num2)
            print("Note: User-inputted numbers converted to integers.")
        
        operation = operators[op] # dictionary mapping operator functions
        
        # NOTE - Use "pass" statements to allow code to be run without having to
        #        fill out the contents.  This pass statement should be removed    
        #pass
        
        # User input is generally returned as a string and must be translated.
        return (num1, num2, operation)
        
    except:
        print("Invalid Input")
        return (None, None, None)

# End def



# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------

# NOTE - The python variable "__name__" is provided by the language and can 
#       be used to determine how the file is being executed.  For example,
#       the program is being executed on the command line:
#          python3 simple_calc.py
#       then the "__name__" will be the string:  "__main__".  If the file 
#       is being imported into another python file:
#          import simple_calc
#       the "__name__" will be the module name, i.e. the string "simple_calc"

if __name__ == "__main__":

    # NOTE - Need to add main calculator functionality:
    #          - Use a loop construct to repeat the operation
    #          - Get the input from the user (i.e. use function created above)    
    #          - Check that all inputs are valid (exit the program if invalid)
    #          - Execute the function on the numbers and print the results
    
    while (1):
        
        (n1, n2, op) = get_user_input()
        
        if (n1 is None) or (n2 is None) or (op is None):
            print("ERROR: User Input Invalid: {0} {1} {2}".format(n1, n2, op))
            exit()
        else:
            print(op(n1, n2))
    
    # test method: get_user_input()
    #print(n1)
    #print(n2)
    #print(op)

    # NOTE - Use "pass" statements to allow code to be run without having to 
    #        fill out the contents.  This pass statement should be removed    
    #pass

