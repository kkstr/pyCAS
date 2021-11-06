# preamble
from sympy.core.function import Function, UndefinedFunction
import sympy
import os
from sympy import *
from sympy.functions.elementary.piecewise import Undefined
from sympy.printing.latex import LatexPrinter
from itertools import zip_longest
import numpy as np

temp = 'WIP'

x, y, z, t, = symbols('x y z t')

# core functions and classes

class Polynomial:
    def __init__(self, *coefficients):
        """ input: coefficients are in the form a_n, ...a_1, a_0 
        """
        self.coefficients = list(coefficients) # tuple to list
    def __repr__(self):
        """
        method to return the canonical string representation 
        of a polynomial.
   
        """
        return "Polynomial" + str(self.coefficients)
    def __call__(self, x):    
        res = 0
        for coeff in self.coefficients:
            res = res * x + coeff
        return res 
    def degree(self):
        return len(self.coefficients)   
    def __add__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [sum(t) for t in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    def __sub__(self, other):
        c1 = self.coefficients[::-1]
        c2 = other.coefficients[::-1]
        res = [t1-t2 for t1, t2 in zip_longest(c1, c2, fillvalue=0)]
        return Polynomial(*res)
    def derivative(self):
        derived_coeffs = []
        exponent = len(self.coefficients) - 1
        for i in range(len(self.coefficients)-1):
            derived_coeffs.append(self.coefficients[i] * exponent)
            exponent -= 1
        return Polynomial(*derived_coeffs)
    def __str__(self):
        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^"+str(degree)
            return res
        degree = len(self.coefficients) - 1
        res = ""
        for i in range(0, degree+1):
            coeff = self.coefficients[i]
            # remove 0 coeff
            if abs(coeff) == 1 and i < degree:
                #get rid of useless 1x
                res += f"{'+' if coeff>0 else '-'}{x_expr(degree-i)}"  
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree-i)}" 
        return res.lstrip('+')    # remove the +

class latex_printer(LatexPrinter):
    def _print_Derivative(self, expr):
        function, *variables = expr.args
        if not isinstance (type(function), UndefinedFunction) or \
            not all(isinstance(i, Symbol) for i in variables):
            return super()._print_Derivative(expr)

class pyCAS:
    def __init__(self, version):
        pyCAS.version = version

def exit():
    print('Goodbye!')
    exit
    clearConsole()
    return exit()

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')
    command = 'cls'
    os.system(command)

pyCASv = pyCAS('v.0.1')

def main():
    clearConsole()
    print('Welcome to pyCAS! Version: ' + pyCAS.version)
    print('Please select a topic:')
    print('1. Polynomials')
    print('2. Calculus')
    print('3. Solve')
    print('4. Advanced')
    print('5. Matrices')
    print('6. Geometry')
    print('7. Statistics')
    print('8. Physics')
    print('9. Cryptography')
    print('10. Knowledge')
    print('11. Exit')
    selection = input('Please enter a number: ')
    if selection == '1':
        polynomials()
    elif selection == '2':
        calculus()
    elif selection == '3':
        algebra()
    elif selection == '4':
        advanced()
    elif selection == '5':
        matrices()
    elif selection == '6':
        geometry()
    elif selection == '7':
        statistics_main()
    elif selection == '8':
        physics()
    elif selection == '9':
        cryptography()
    elif selection == '10':
        knowledge()
    elif selection == '11':
        exit()
    else:
        print('Invalid input!')
        main()

# menus/framework

def polynomials():
    clearConsole()
    print('Polynomial Function')
    print('Please select a mode:')
    print('1. Arithmetic')
    print('2. Factorization')
    print('3. Expansion')
    print('4. Solving')
    print('5. Back')
    selection = input('Please enter a number: ') # needs to be printed in latex
    if selection == '1':
        clearConsole()
        p = Polynomial(3, 2, 12, 1, 6)
        p2 = Polynomial(1, 2, 3)
        p_der = p.derivative()
        X = np.linspace(-2, 3, 50, endpoint=True)
        print("Polynomial 1:", p)
        print("Polynomial 2:", p2)
        print("Derivative of Polynomial 1:", p_der)
        p3 = p + p2
        print("Sum of Polynomial 1 + Polynomial 2:", p3)
        rerun = input("\n Rerun to Polynomials? (Y/N)")
        if rerun == 'y' or rerun == 'Y':
            polynomials()
        else:
            main()
    elif selection == '2':
        factor(input("Factor Polynomial: "))
    elif selection == '3':
        sympy.expand(input("Expand Polynomial: "))
    elif selection == '4':
        sympy.solve(x**3 + 2*x + 3, x)
    elif selection == '5':
        return main()
    else:
        print('Invalid input!')
        polynomials()


def calculus():
    clearConsole()
    print('Calculus Function')
    print('Please select a mode: ')
    print('1. Derivative')
    print('2. Integration')
    print('3. Taylor (Laurent) series')
    print('4. Differential Equations Solver')
    print('5. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Derivative Function')
    elif selection == '2':
        print('Integration Function')
    elif selection == '3':
        print('Taylor (Laurent) series Function')
    elif selection == '4':
        print('Differential Equation Solver')
    elif selection == '5':
        return main()
    else:
        print('Invalid input!')
        calculus()


def algebra():
    clearConsole()
    print('Algebra Function')
    print('Please select a mode:')
    print('1. Linear Algebra')
    print('2. System of Equations')
    print('3. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Linear Algebra Function')
    elif selection == '2':
        print('System of Equations Function')
    elif selection == '3':
        print('Differential Equation Solver')
    elif selection == '4':
        return main()
    else: 
        print('Invalid input!')
        algebra()


def advanced():
    clearConsole()
    print('Advanced Mathematics')
    print('Please select a mode:')
    print('1. Permutations')
    print('2. Combinations')
    print('3. Partitions')
    print('4. Subsets')
    print('5. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Permutations Function')
    elif selection == '2':
        print('Combinations Function')
    elif selection == '3':
        print('Partitions Function')
    elif selection == '4':
        print('Subsets Function')
    elif selection == '5':
        return main()
    else:
        print('Invalid input!')
        advanced()
    print(temp)


def matrices():
    clearConsole()
    print('Matrices Function')
    print('Please select a mode:')
    print('1. Arithmetic')
    print('2. Eigenvalues/Eigenvectors')
    print('3. Determinants')
    print('4. Inversion')
    print('5. Solving')
    print('6. Abstractions')
    print('7. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Arithmetic Function')
    elif selection == '2':
        print('Eigenvalues/Eigenvectors Function')
    elif selection == '3':
        print('Determinants Function')
    elif selection == '4':
        print('Inversion Function')
    elif selection == '5':
        print('Solving Function')
    elif selection == '6':
        print('Abstractions Function')
    elif selection == '7':
        return main()
    else:
        print('Invalid input!')
        matrices()
    print(temp)


def geometry():
    clearConsole()
    print('Geometrical Function')
    print('Please select a mode:')
    print('1. Intersections')
    print('2. Tangency')
    print('3. Similarity')
    print('4. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Intersections Function')
    elif selection == '2':
        print('Tangency Function')
    elif selection == '3':
        print('Similarity Function')
    elif selection == '4':
        return main()
    else:
        print('Invalid input!')
    print(temp)


def statistics_main():
    clearConsole()
    print('Statistics Function')
    print('Please select a mode:')
    print('1. Random variable types')
    print('2. Probability')
    print('3. Expected value and variance')
    print('4. Probability density')
    print('5. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Random variable types Function')
    elif selection == '2':
        print('Probability Function')
    elif selection == '3':
        print('Expected value and variance Function')
    elif selection == '4':
        print('Probability density Function')
    elif selection == '5':
        return main()
    else:
        print('Invalid input!')
        statistics_main()


def statistics_sub():
    clearConsole()
    print('Random Variables Function')
    print('Please select a mode:')
    print('1. Binomial Distributions')
    print('2. Uniform Distributions')
    print('3. Normal Distributions')
    print('4. Poisson Distributions')
    print('5. Hypergeometric Distributions')
    print('6. Bernoulli Distributions')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Binomial Distributions Function')
    elif selection == '2':
        print('Uniform Distributions Function')
    elif selection == '3':
        print('Normal Distributions Function')
    elif selection == '4':
        print('Poisson Distributions Function')
    elif selection == '5':
        print('Hypergeometric Distributions Function')
    elif selection == '6':
        print('Bernoulli Distributions Function')
    elif selection == '7':
        return statistics_main()
    else:
        print('Invalid input!')
        statistics_sub()


def physics():
    clearConsole()
    print('Physics Function')
    print('Please select a mode:')
    print('1. Mechanics')
    print('2. Quantum Mechanics')
    print('3. Pauli Algebra')
    print('4. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Mechanics Function')
    elif selection == '2':
        print('Quantum Mechanics Function')
    elif selection == '3':
        print('Pauli Algebra Function')
    elif selection == '4':
        return main()
    else:
        print('Invalid input!')
        physics()


def cryptography():
    clearConsole()
    print('Cryptography Function')
    print('Please select a mode:')
    print('1. RSA')
    print('2. Shift cipher')
    print('3. Affine cipher')
    print('4. Linear feedback shift ciphers')
    print('5. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('RSA Function')
    elif selection == '2':
        print('Shift cipher Function')
    elif selection == '3':
        print('Affine cipher Function')
    elif selection == '4':
        print('Linear feedback shift ciphers Function')
    elif selection == '5':
        return main()
    else:
        print('Invalid input!')
        cryptography()

def knowledge():
    print('Information')
    print('Please select a category:')
    print('1. Arithmetical Laws')
    print('2. Calculus Rules')
    print('3. Common Physics Constants')
    print('4. Common Chemistry Constants/Periodic Table')
    print('5. Fundamental Thereom of Algebra')
    print('6. Fundamental Thereom of Calculus')
    print('7. Back')
    selection = input('Please enter a number: ')
    if selection == '1':
        print('Arithmetical Laws Function')
    if selection == '2':
        print('Calculus Rules Function')
    if selection == '3':
        print('Common Physics Constants Function')
    if selection == '4':
        print('Common Chemistry Constants/Periodic Table Function')
    if selection == '5':
        print('Fundamental Thereom of Algebra Function')
    if selection == '6':
        print('Fundamental Thereom of Calculus Function')
    if selection == '7':
        return main()
    else:
        print('Invalid input!')
        knowledge()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3