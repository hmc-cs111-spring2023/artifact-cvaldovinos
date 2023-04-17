import numpy_financial as npf;
import numpy as np;

cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]
print(npf.irr(cash_flows))

rate = 0.05/12
nper = 10*12
pmt = -100
pv = -100

# One approach for a design change here could be allowing users to input an 
#   annual rate and/or number of years which in the implementation of the 
#   functions is automatically converted to monthly rate and number of months
print(npf.fv(rate, nper, pmt, pv))


# This creates an array of monthly interest rates when the annual interest rate 
#   is 5%, 6%, and 7% respectively
intRates = np.array((0.05, 0.06, 0.07))/12

# This prints the future value of a $100 payment made monthly for 10 years at 
#   5%, 6%, and 7% interest rates
print(npf.fv(intRates, 10*12, -100, -100))

# This is an example of minor design decision that I would like to make work;
#   (allow users to call function with uppercase letters as that is the standard
#   in Economics)

# print(npf.FV(intRates, 10*12, -100, -100))
 

#  An example of the more interesting and useful design I would like to have 
#   work would be assigning values in the call to the function such as

# print(npf.FV(r = 7%, years = 10, pmt = -100, pv = -100))

print(npf.npv(0.281,[-100, 39, 59, 55, 20]))

print(npf.npv(0.281,[-100, 39, 59, 55, 20]))
