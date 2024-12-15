# QUESTÃO 05
# Crie um programa em Python para gerenciar uma lista de tarefas. O programa deve
# oferecer as seguintes opções:
# 1. Adicionar tarefa: O usuário pode adicionar uma tarefa com um título e uma
# descrição. (adicionar no Json) --> OK
# 2. Listar tarefas: Exibir todas as tarefas cadastradas no Json --> OK
# 3. Remover tarefa: Permitir ao usuário selecionar uma tarefa pela sua abreviação para
# removê-la da lista que está armazenada no Json. --> OK
# 4. Sair: Encerrar o programa. --> OK
# Cada funcionalidade deve ser implementada em uma função separada e o programa
# deve rodar até que o usuário opte por sair.

import os
import json

arquivo = os.path.join(os.path.dirname(__file__), "tarefas.json")


def carregar_tarefas():
    if not os.path.exists(arquivo):
        with open(arquivo, "w") as p:
            json.dump([], p, indent=4)

    with open(arquivo, "r") as p:
        return json.load(p)


def limpar_terminal():
    os.system("cls")


def titulo():
    print("\033[1;35m========== LISTA DE TAREFAS ==========\033[m\n")


def exibir_subtitulo(texto):
    limpar_terminal()
    linha = f'{"*" * 80: ^75}'
    print(linha)
    print(texto)
    print(linha)
    print("")


def add_tarefa(titulo, abreviacao, descricao):
    tarefas = carregar_tarefas()
    tarefas.append({"titulo": titulo, "abreviacao": abreviacao, "descricao": descricao})

    with open(arquivo, "w") as p:
        json.dump(tarefas, p, indent=4, ensure_ascii=False)

    print("\n\033[1;32m✅ NOVA TAREFA ADICIONADA!\033[m")


def listar_tarefas():
    tarefas = carregar_tarefas()
    if not tarefas:
        print("\033[1;33m⚠️ Nenhuma tarefa encontrada.\033[m")
    else:
        for tarefa in tarefas:
            print(f"TAREFA: {tarefa['titulo']} | SIGLA: {tarefa['abreviacao']} | DESCRIÇÃO: {tarefa['descricao']}")


def remover_tarefa(abv):
    tarefas = carregar_tarefas()
    encontrado = False

    for tarefa in tarefas:
        if tarefa["abreviacao"] == abv:
            tarefas.remove(tarefa)
            encontrado = True
            print("\n\033[1;32m✅ TAREFA EXCLUÍDA! \033[m")
            break

    if not encontrado:
        print("\n\033[1;31m❌ TAREFA NÃO ENCONTRADA.\033[m")

    with open(arquivo, "w") as p:
        json.dump(tarefas, p, indent=4, ensure_ascii=False)


def exibir_menu_tarefas():
    titulo()
    print("1 - Adicionar nova tarefa")
    print("2 - Exibir lista de tarefas")
    print("3 - Remover tarefa")
    print("4 - Encerrar programa")


def opcoes_menu_tarefa():
    while True:
        try:
            op = int(input("\n\033[0;34m➤ Escolha uma opção:\033[m "))
            if op == 1:
                exibir_subtitulo(f'\033[1;35m{"Nova tarefa":^75}\033[m')
                titulo = input("▸ Informe o TÍTULO da nova tarefa: ")
                abreviacao = input("▸ Informe a SIGLA (abreviação) do título da tarefa: ")
                descricao = input("▸ Escreva uma curta descrição da tarefa: ")
                add_tarefa(titulo, abreviacao, descricao)
                voltar_menu()

            elif op == 2:
                exibir_subtitulo(f'\033[1;35m{"Lista de tarefas":^75}\033[m')
                listar_tarefas()
                voltar_menu()

            elif op == 3:
                exibir_subtitulo(f'\033[1;35m{"Remover tarefa":^75}\033[m')
                abv = input("▸ Informe a SIGLA (abreviação) do título da tarefa que você deseja excluir: ")
                remover_tarefa(abv)
                voltar_menu()
            elif op == 4:
                print("\n\033[1;36mPrograma encerrado!\033[m")
                return False
            
            else:
                print("\n\033[1;33m⚠️ OPÇÃO INVÁLIDA!\033[m")
        except ValueError as e:
            print(f"\n\033[1;31m⚠️ ERRO: Entrada inválida. Detalhes: {e}\033[m")
        except Exception as e:
            print(f"\n\033[1;31m⚠️ ERRO INESPERADO: {e}\033[m")

def voltar_menu():
    input("\n\033[0;34m➤  Digite qualquer tecla para voltar ao menu anterior:\033[m ")
    main()

def main():
    while True:
        limpar_terminal()
        exibir_menu_tarefas()
        if not opcoes_menu_tarefa():
            break


if __name__ == "__main__":
    main()


