def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def main():
    alunos = {}

    while True:
        try:
            qtd = int(input("Informe a quantidade de alunos (entre 2 e 7): "))
            if 2<=qtd<=7:
                break
            else:
                print("Quantidade invalida. Insira um valor entre 2 e 7.")
        except ValueError:
            print("Entrada invalida. Insira um numero inteiro.")

    for i in range(qtd):
        nome = input(f"\nInforme o nome do aluno {i+1}: ").strip()
        while True:
            try:
                nota1 = float(input(f"Nota 1 de {nome}: "))
                nota2 = float(input(f"Nota 2 de {nome}: "))
                if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
                    media = calcular_media(nota1, nota2)
                    alunos[nome] = media
                    break
                else:
                    print("As notas devem estar entre 0.0 e 10.0.")
            except ValueError:
                print("Entrada invalida. Use apenas números.")

    medias = list(alunos.values())
    media_turma = sum(medias) / qtd
    maior_media = max(medias)
    menor_media = min(medias)

    aluno_maior = [nome for nome, media in alunos.items() if media == maior_media][0]
    aluno_menor = [nome for nome, media in alunos.items() if media == menor_media][0]

    print("\nResultado final:")
    print(f"A média da turma é: {media_turma:.2f}")
    print(f"A turma tem {qtd} alunos.")
    print(f"O aluno com a maior média foi {aluno_maior} com {maior_media:.2f}.")
    print(f"O aluno com a menor média foi {aluno_menor} com {menor_media:.2f}.")

if __name__ == "__main__":
    main()