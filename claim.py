import numpy as np
import sympy as sp
import sys
import binascii as bs
import os
from subprocess import PIPE, run
import json

if len(sys.argv) < 4:
    print("Usage: python3 claim.py .py  <to_address>  <N in decimal> <N factor in decimal value> ") 
    sys.exit()

#######
address     = sys.argv[1]
n           = sys.argv[2] 
p           = sys.argv[3] 


#get some data needed to build the transaction
n_poolid = run( "./factorn-cli getdeadpoolid "    + str(n) , stdout=PIPE, universal_newlines=True, shell=True ).stdout
dp_entry = run( "./factorn-cli getdeadpoolentry " + n_poolid , stdout=PIPE, universal_newlines=True, shell=True ).stdout
dp_entry = json.loads(dp_entry)["entries"]

print()
print("Claim deadpool entry txn.")
command1 = "./factorn-cli claimdeadpooltxs '" + dp_entry.__str__().replace("'","\"") + "' " + "  ".join( [ address, p ] )  
print(command1)
result = run(  command1   , stdout=PIPE, universal_newlines=True, shell=True)
print(result.stdout)

command2 = "./factorn-cli sendrawtransaction " + result.stdout

print("Send Transaction.")
result = run(  command2 , stderr=PIPE,  stdout=PIPE, universal_newlines=True, shell=True )

print()
print( result.stdout )
print( result.stderr )

print()
print(command1)
print(command2)
