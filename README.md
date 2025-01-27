# IFaaS
Utilities for the deadpool (Integer Factorization as a Service).

# How to?

First, you will need the ``factorn-cli`` executable that comes bundled with the Fact daemon (https://github.com/FACT0RN/FACT0RN/releases/tag/v5.0.69). Place ``factorn-cli`` in the same folder as the python files found here.

Second, you must load a wallet to be able to fund the transactions, ``./facton-cli loadwallet "wallet_name" ``

Usage:

To set a bounty on an integer, or add coins to an existing bounty, use the following:
```
python create_deadpool_entry.py <bounty_amount> < N integer (Optional) >
```

If you have a solution for an integer with a bounty, announce that you have a solution as follows:

```
python3 announce.py <burn_amount> <address> <N> <N factor>
```


To claim your reward, you need to wait 100 blocks since your announcement and no more than 672 blocks, and you claim as follows:

```
python claim.py .py  <to_address>  <N in decimal> <N factor in decimal value> 
```

If anyone would like to merge all three scripts and use a proper CLI package from python to integrate it into one python script we will accept the PR.

For a brief overview of the new RPC calls for the deadpool see: https://x.com/FACT0RN/status/1874078627421192700
