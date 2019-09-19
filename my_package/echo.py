import numpy as np

def echo(first = 1, last = 10):
    xs = np.arange(int(first), int(last))
    print(f'hello, world! {xs}')
