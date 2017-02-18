import numpy as np
import sys
import math
import time

def branin(seed,x, y):

  result = np.square(y - (5.1/(4*np.square(math.pi)))*np.square(x) + 
       (5/math.pi)*x - 6) + 10*(1-(1./(8*math.pi)))*np.cos(x) + 10

  result = float(result)

  #if np.random.rand > 0.75:
  #  raise Exception('Blah!')

  print 'Result = %f' % result
  time.sleep(np.random.randint(30))
  return {'branin'+str(seed) : result}

# Write a function like this called 'main'
def main(seed, params):
  print params
  return branin(seed,params['x'], params['y'])
