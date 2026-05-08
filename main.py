import sys
import os

x = None
if x == None:
    print("x is None")

unused_variable = "never used"

def greet(name):
    greeting = "Hello, " + name + "! Welcome to DSC 190, Tools of the Trade, Spring 2026."
    return greeting

print(greet("World"))
