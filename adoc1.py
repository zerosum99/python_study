
'''
>>> f(3)
19
'''

def f(x):
    g(x*2)
    
def g(x):
    print(x+3)
    import pdb; pdb.set_trace()