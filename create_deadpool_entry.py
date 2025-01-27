import numpy as np
import sympy as sp
import sys
import binascii as bs
import os
from subprocess import PIPE, run
import json

if len(sys.argv) < 2:
    print("Usage: python3 create_deadpool_entry.py <bounty_amount> < N integer (Optional) > ") 
    sys.exit()

nbits, p, q, n = 0, 0, 0, 0
bounty         = sys.argv[1]
n = sys.argv[2]


print()
print("Create deadpool entry.")
command1 = "./factorn-cli createdeadpoolentry " + bounty  + " " + str(n)
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
command4 =  "./factorn-cli sendrawtransaction " + json.loads( result.stdout)["hex"]
result = run(  command4 , stderr=PIPE,  stdout=PIPE, universal_newlines=True, shell=True )

print()
print( result.stdout )
print( result.stderr )
print()
print(command1)
print(command2)
print(command3)
print(command4)
