"""
Author: chiu cam minh
Date: 03/09/2021
Program: exersice_01_page_194.py
Problem:
    Where are module variables, parameters, and temporary variables introduced and
    initialized in a program?
Solution:
    Module variables :
        Introduced: A module-level variable is declared for a particular module. 
                    It is available to all procedures within that module but not to the rest of the application. 
                    Module-level variables remain in existence for 
                    the lifetime of the application and preserve their values.
        Initialized: module variable gets initialized where they are declared inside the module.
                    it is initialized to 0 by default.

    Parameters:
        Introduced: parameters are declared inside the parenthesis of the function definition
        Initialized: parameters can be initialized where they are declared or 
                    can be declared in the parenthesis of the function call

    Temporary variables :
        Introduced: inside a block, they have very short lifetime and
                    hold data that can be discarded or is later stored in a permanent variable
        Initialized: temporary variables can be initialized anywhere inside the block where they are declared.

"""
