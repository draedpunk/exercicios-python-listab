# QUESTÃO 06
# Desenvolva um programa em Python para gerenciar notas de alunos em uma disciplina,
# utilizando arquivos JSON para armazenamento dos dados.
# O programa deve realizar as seguintes operações:
# 1. Cadastrar aluno: Permitir o cadastro de alunos inserindo o nome e inicializando
# a lista de notas como vazia. Os dados devem ser armazenados em um arquivo
# JSON. --> OK
# 2. Adicionar notas: Permitir ao usuário adicionar pelo menos três notas a um aluno
# já cadastrado. As notas devem ser armazenadas no arquivo JSON. --> OK
# 3. Exibir médias: Calcular e exibir a média de cada aluno. Informar se ele está
# aprovado (média ≥ 7) ou reprovado (média < 7). --> OK
# 4. Sair: Encerrar o programa.

import os
import json

# Definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), "notas.json")


def carregar_notas_json():
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as p:
            json.dump([], p, indent=4)

    with open(arquivo, "r") as p:
        return json.load(p)


def limpar_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def titulo():
    print("\033[1;35m========== RELAÇÃO NOTAS-ALUNOS ==========\033[m\n")


def exibir_subtitulo(texto):
    limpar_terminal()
    linha = f'{"*" * 80: ^75}'
    print(linha)
    print(texto)
    print(linha)
    print("")


def cadastrar_aluno(aluno):
    alunos = carregar_notas_json()
    # Adicionando o novo aluno com campos de nota como None
    alunos.append({"aluno": aluno, "num": None, "ndois": None, "ntres": None})

    # Salvando novamente o JSON com o aluno atualizado
    with open(arquivo, "w") as p:
        json.dump(alunos, p, indent=4, ensure_ascii=False)
    print("\n\033[1;32m✅ ALUNO ADICIONADO COM SUCESSO!\033[m")


def add_notas_aluno(nome_aluno, nota_um, nota_dois, nota_tres):
    alunos = carregar_notas_json()

    for aluno in alunos:
        if aluno["aluno"].lower() == nome_aluno.lower():
            aluno["num"] = nota_um
            aluno["ndois"] = nota_dois
            aluno["ntres"] = nota_tres
            break
    else:
        print("\n\033[1;31m❌ ALUNO NÃO ENCONTRADO!\033[m")
        return

    with open(arquivo, "w") as p:
        json.dump(alunos, p, indent=4, ensure_ascii=False)
    print("\n\033[1;32m✅ NOTAS ADICIONADAS COM SUCESSO!\033[m")


def calcular_medias():
    alunos = carregar_notas_json()

    for aluno in alunos:
        if None in (aluno["num"], aluno["ndois"], aluno["ntres"]):
            print(f"\n\033[1;33m⚠️  O aluno {aluno['aluno']} ainda não possui todas as notas cadastradas.\033[m")
            continue

        # Calculando e exibindo a média:
        notas = [aluno["num"], aluno["ndois"], aluno["ntres"]]
        media = sum(notas) / 3
        situacao = "Aprovado" if media >= 7 else "Reprovado"

        print(f"\nALUNO: {aluno['aluno']}")
        print(f"NOTAS: {notas}")
        print(f"MÉDIA: {media:.2f} - SITUAÇÃO: {situacao}")


def exibir_menu_aluno():
    limpar_terminal()
    titulo()
    print("1 - Cadastrar novo aluno")
    print("2 - Adicionar notas")
    print("3 - Exibir médias")
    print("4 - Encerrar programa")


def voltar_menu():
    input("\n\033[0;34m➤  Digite qualquer tecla para voltar ao menu anterior:\033[m ")
    main()


def opcoes_menu():
    while True:
        try:
            op = int(input("\n\033[0;34m➤  Escolha uma opcao:\033[m "))

            if op == 1:
                exibir_subtitulo(f'\033[1;35m{"Novo Cadastro":^75}\033[m')
                aluno = input("▸ Informe o nome do novo ALUNO: ").strip()
                cadastrar_aluno(aluno)
                voltar_menu()

            elif op == 2:
                exibir_subtitulo(f'\033[1;35m{"Adicionar Notas":^75}\033[m')
                nome_aluno = input("▸ Informe o nome do aluno que receberá as notas: ").strip()
                nota_um = float(input("▸ Informe a primeira nota: "))
                nota_dois = float(input("▸ Informe a segunda nota: "))
                nota_tres = float(input("▸ Informe a terceira nota: "))
                add_notas_aluno(nome_aluno, nota_um, nota_dois, nota_tres)
                voltar_menu()

            elif op == 3:
                exibir_subtitulo(f'\033[1;35m{"Médias":^75}\033[m')
                calcular_medias()
                voltar_menu()

            elif op == 4:
                print("\n\033[1;36mPrograma encerrado.\033[m")
                break
            else:
                print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")
        except ValueError:
            print("\n\033[1;33m⚠️  Ocorreu um erro.\033[m")


def main():
    while True:
        exibir_menu_aluno()
        if not opcoes_menu():
            break


if __name__ == "__main__":
    main()
