""" 
def bar(pos1, pos2, *args, par1='par1', par2='par2'):
    print(pos1, pos2, args, par1, par2)

bar(1,2, par2='nuevo par2')
 """
 
def foo(p1, p2, *args, n1="uno", n2 = "dos", **kwargs):
    print(p1, p2, args, n1, n2, kwargs)

foo(1, 'dddd', 11,22,33,n3="enetres", n4="enecuatro", n2="nuevo n2")
