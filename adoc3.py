
'''
>>> f(3)
9
'''

def f(x):
    g(x*2)
    
def g(x):
    print(x+3)
    import pdb; pdb.set_trace()