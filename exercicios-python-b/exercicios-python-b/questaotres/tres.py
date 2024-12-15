# QUESTÃO 03
# Como desenvolvedor, você foi solicitado a criar um programa em Python que realize o
# cadastro e a visualização dos alunos de uma faculdade. O programa deve apresentar um
# menu de opções para o usuário com as seguintes funcionalidades:
# 1. Escrever: Adicionar um nome e idade de um aluno ao arquivo JSON.
# 2. Ler: Exibir o conteúdo de um arquivo JSON na tela.
# 3. Sair: Encerrar o programa.
# O programa deve executar em um loop indefinido até que o usuário escolha a opção de
# sair. Ao selecionar uma opção, o programa deve realizar a ação correspondente e retornar
# ao menu.

import json
import os

# definindo o caminho do arquivo no escopo global
arquivo = os.path.join(os.path.dirname(__file__), "alunos.json")

def limpar_terminal():
    os.system("cls")

def carregar_estudantes_json():

    if not os.path.exists(arquivo):
        with open(arquivo, "w") as p:
            json.dump([], p, indent=4)
    with open(arquivo, "r") as p:
        return json.load(p)

def titulo_menu():
    print("\033[1;35m========== SISTEMA DOS ALUNOS ==========\033[m\n")

def exibir_subtitulo(texto):
    os.system("cls")
    linha = f'{"*" * 80: ^75}'
    print(linha)
    print(texto)
    print(linha)
    print("")

def cadastrar_aluno(nome, idade):
    alunos = carregar_estudantes_json()
    alunos.append({"nome": nome, "idade": idade})

    with open(arquivo, "w") as p:
        json.dump(alunos, p, indent=4, ensure_ascii=False)
    print("\n \033[1;32m✅ ALUNO ADICIONADO COM SUCESSO!\033[m")

def exibir_alunos():
    alunos = carregar_estudantes_json()

    if alunos:
        for aluno in alunos:
            print("NOME: " + aluno["nome"].center(10) + " | IDADE: " + str(aluno["idade"]))
    else:
        print("\n\033[1;31m❌ NENHUM ALUNO ENCONTRADO.\033[m")

def exibir_menu_aluno():
    os.system("cls") #limpar terminal
    titulo_menu()
    print("1 - Cadastrar novo aluno")
    print("2 - Exibir alunos")
    print("3 - Encerrar")

def escolher_opcao_menu():
    while True:
        try:
            op = int(input("\n\033[0;34m➤  Escolha uma opcao:\033[m "))

            if (op == 1):
                exibir_subtitulo(f'\033[1;35m{"Novo Cadastro":^75}\033[m')
                nome = input("▸ Informe o NOME do aluno: ")
                idade = int(input("▸ Informe a IDADE do aluno: "))
                cadastrar_aluno(nome, idade)
                voltar_menu()
                break
            elif (op == 2):
                exibir_subtitulo(f'\033[1;35m{"Alunos Cadastrados":^75}\033[m')
                exibir_alunos()
                voltar_menu()
                break
            elif (op == 3):
                print("\n\033[1;36mPrograma encerrado!\033[m")
                return False
            else:
                print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")

        except ValueError:
            print("\n\033[1;33m⚠️  OPÇÃO INVÁLIDA!\033[m")

def voltar_menu():
    input("\n\033[0;34m➤  Digite qualquer tecla para voltar ao menu anterior:\033[m ")
    main()

def main():
    while True:
        os.system("cls")
        exibir_menu_aluno()
        if not escolher_opcao_menu():
            break

if __name__ == "__main__":
    main()

