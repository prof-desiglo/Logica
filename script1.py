import sys

def soma(x, y):
    return x+y

if len(sys.argv) <= 2: # neceesário 2 argumentos
    print('Menos de 2 argumentos')
    sys.exit()
    
print(sys.argv[0])

x = sys.argv[1] 
y = sys.argv[2]

x = int(x)
y = int(y)

print(soma(x,y))
