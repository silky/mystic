#!/usr/bin/env python

"""
Example:
    - Minimize Rosenbrock's Function with Powell's method.

Demonstrates:
    - standard models
    - minimal solver interface
    - parameter constraints solver and constraints factory
    - statistical parameter constraints
    - customized monitors
"""

# Powell's Directonal solver
from mystic.solvers import fmin_powell

# Rosenbrock function
from mystic.models import rosen

# tools
from mystic.monitors import VerboseMonitor
from mystic.math.measures import mean, impose_mean
from mystic.math import almostEqual


if __name__ == '__main__':

    print "Powell's Method"
    print "==============="

    # initial guess
    x0 = [0.8,1.2,0.7]

    # define constraints factory function
    def constraints_factory(target):
        # define constraints function
        def constraints(x):
            # constrain the last x_i to be the same value as the first x_i
            x[-1] = x[0]
            # constrain x such that mean(x) == target
            if not almostEqual(mean(x), target):
                x = impose_mean(target, x)
            return x
        return constraints

    # configure constraints function
    constraints = constraints_factory(1.0)

    # configure monitor
    stepmon = VerboseMonitor(1)

    # use Powell's method to minimize the Rosenbrock function
    solution = fmin_powell(rosen,x0,constraints=constraints,itermon=stepmon)
    print solution
 
# end of file
