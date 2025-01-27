import numpy as np
import sympy as sp
import sys
import binascii as bs
import os
from subprocess import PIPE, run
import json

if len(sys.argv) < 5:
    print("Usage: python3 announce.py <burn_amount> <address> <N> <N factor> ") 
    sys.exit()

#######
burn_amount = sys.argv[1]
address     = sys.argv[2]
n           = sys.argv[3] 
p           = sys.argv[4]

print()
print("Create announcement transaction")
command1 = "./factorn-cli announcedeadpoolclaim " + " ".join( [ burn_amount, address, n, p ] )  
result = run(  command1   , stdout=PIPE, universal_newlines=True, shell=True)
print(result.stdout)

print("Fund transaction.")
command2 =  "./factorn-cli fundrawtransaction " + result.stdout
result = run( command2 , stdout=PIPE, universal_newlines=True, shell=True )
print(result.stdout)

print("Sign transaction.")
command3 =  "./factorn-cli signrawtransactionwithwallet " + json.loads( result.stdout)["hex"]
result = run( command3 , stdout=PIPE, universal_newlines=True, shell=True )
print(result.stdout)

print("Send Transaction.")
command4 = "./factorn-cli sendrawtransaction " + json.loads( result.stdout)["hex"]
result = run(  command4 , stderr=PIPE,  stdout=PIPE, universal_newlines=True, shell=True )

print()
print( result.stdout )
print( result.stderr )
print()
print(command1)
print(command2)
print(command3)
print(command4)

