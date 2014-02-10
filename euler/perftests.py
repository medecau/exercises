import mathkit
try:
    import cProfile as profile
except:
    import profile

def test1():
    mathkit.next_prime(100000000)
    

profile.run('mathkit.next_prime(100000000000000)')
    
