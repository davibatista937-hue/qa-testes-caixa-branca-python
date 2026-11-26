def saque(valor, saldo, limite_credito):
    status = False

    if valor <= saldo:
        saldo = saldo - valor
        status = True

    elif valor <= limite_credito:
        limite_credito = limite_credito - valor
        status = True

    return status, saldo, limite_credito


# Casos de teste
casos = [
    ("Caso 1 - Saque pelo saldo", 800, 1000, 500, (True, 200, 500)),
    ("Caso 2 - Saque pelo credito", 1200, 1000, 1500, (True, 1000, 300)),
    ("Caso 3 - Saldo e credito insuficientes", 1600, 1000, 500, (False, 1000, 500))
]

for nome, valor, saldo_inicial, limite_inicial, esperado in casos:
    resultado = saque(valor, saldo_inicial, limite_inicial)

    print(nome)
    print("Valor do saque:", valor)
    print("Resultado obtido:", resultado)
    print("Resultado esperado:", esperado)

    if resultado == esperado:
        print("Status do teste: APROVADO")
    else:
        print("Status do teste: REPROVADO")

    print("-" * 40)
