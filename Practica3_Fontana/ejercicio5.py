def promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else "Error: no se ingresaron números"

print(promedio())