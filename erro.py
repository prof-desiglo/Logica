try:
    #2 / 0
    raise RuntimeError("Erro customizado") 
except(ZeroDivisionError):
    print("Divisão por zero")
except RuntimeError as e:
    print(str(e))
except:
    print("erro")
finally:
    print("acontece mesmo com erro")