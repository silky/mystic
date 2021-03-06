#!/usr/bin/env python

"""
Example:
    - Solve 8th-order Chebyshev polynomial coefficients with Powell's method.
    - Plot of fitting to Chebyshev polynomial.

Demonstrates:
    - standard models
    - minimal solver interface
"""

# Powell's Directonal solver
from mystic.solvers import fmin_powell

# Chebyshev polynomial and cost function
from mystic.models.poly import chebyshev8, chebyshev8cost
from mystic.models.poly import chebyshev8coeffs

# tools
from mystic.math import poly1d
from mystic.tools import getch
import pylab
pylab.ion()

# draw the plot
def plot_exact():
    pylab.title("fitting 8th-order Chebyshev polynomial coefficients")
    pylab.xlabel("x")
    pylab.ylabel("f(x)")
    import numpy
    x = numpy.arange(-1.2, 1.2001, 0.01)
    exact = chebyshev8(x)
    pylab.plot(x,exact,'b-')
    pylab.legend(["Exact"])
    pylab.axis([-1.4,1.4,-2,8],'k-')
    return
 
# plot the polynomial
def plot_solution(params):
    import numpy
    x = numpy.arange(-1.2, 1.2001, 0.01)
    f = poly1d(params)
    y = f(x)
    pylab.plot(x,y,'y-')
    pylab.legend(["Exact","Fitted"])
    pylab.axis([-1.4,1.4,-2,8],'k-')
    return


if __name__ == '__main__':

    print "Powell's Method"
    print "==============="

    # initial guess
    import random
    random.seed(123)
    ndim = 9
    x0 = [random.uniform(-100,100) for i in range(ndim)]

    # draw frame and exact coefficients
    plot_exact()

    # use Powell's method to solve 8th-order Chebyshev coefficients
    solution = fmin_powell(chebyshev8cost,x0)

    # use pretty print for polynomials
    print poly1d(solution)

    # compare solution with actual 8th-order Chebyshev coefficients
    print "\nActual Coefficients:\n %s\n" % poly1d(chebyshev8coeffs)

    # plot solution versus exact coefficients
    plot_solution(solution) 
    getch() #XXX: or pylab.show() ?

# end of file
