import argparse

# Parser de argumentos em linha de comando
parser = argparse.ArgumentParser()

# Adicionando Argumento Output
parser.add_argument("-o", "--Output", help = "Mostra Output")

# Adicionando Argumento Output
parser.add_argument("-R", "--Read", help = "Le o valor", action='store_true')

# Le os argumentos
args = parser.parse_args()

if args.Output:
    print("Mostrando o parametro Output as: % s" % args.Output)
    if args.Read:
        s = input()
        print("Lido:")
        print(s)
