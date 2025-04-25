def promedio(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

print(promedio(3,5,7))