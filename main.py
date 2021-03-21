from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import common as Common
import consulta_protesto as consulta_protesto
import tribunal_justica_mg as tribunal_justica_mg
import dados_consulta
import consulta_sec_municipal
import policia_federal
import policia_civil
from selenium.webdriver.remote.command import Command
from webdriver_manager.chrome import ChromeDriverManager

import os

# Função que abre o Google Chrome


def abre_navegador():

    # chrome = webdriver.Chrome()
    chrome = webdriver.Chrome(ChromeDriverManager().install())

    return chrome


def apresenta_menu(dados_entrada):
    os.system('cls')
    print("\n******************************************")
    print("ESCOLHA A CONSULTA A SER REALIZADA:")
    print("1 - Consulta Protesto - Cartório de Protesto")
    print("2 - Justiça Estadual - 1ª Instância - Cível")
    print("3 - Justiça Estadual - 1ª Instância - Criminal")
    print("4 - Justiça Estadual - 2ª Instância - Cível")
    print("5 - Justiça Estadual - 2ª Instância - Criminal")
    print("6 - Secretaria Municipal - Certidão negativa")

    if dados_entrada.tipo_pessoa == "1":
        print("7 - Polícia Federal - Antecedentes criminais")
        print("8 - Polícia Civil - Atestado de Antecedentes")

    print("9 - Informar dados de consulta")
    print("0 - Encerrar programa")
    print("******************************************")

    try:
        opcao = int(input("Escolha sua opção: "))
        return opcao
    except:
        raise Exception("Opção inválida!")


def escolhe_opcao(opcao, dados_entrada):

    if opcao == 1:
        try:
            chrome = abre_navegador()
            consulta_protesto.consulta_protesto(chrome, dados_entrada)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 2:
        try:
            chrome = abre_navegador()
            tribunal_justica_mg.primeira_instancia(chrome, dados_entrada, 1)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 3:
        try:
            chrome = abre_navegador()
            tribunal_justica_mg.primeira_instancia(chrome, dados_entrada, 2)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 4:
        try:
            chrome = abre_navegador()
            tribunal_justica_mg.segunda_instancia(chrome, dados_entrada, 1)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 5:
        try:
            chrome = abre_navegador()
            tribunal_justica_mg.segunda_instancia(chrome, dados_entrada, 2)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 6:
        try:
            chrome = abre_navegador()
            consulta_sec_municipal.consulta_secretaria_municipal(chrome, dados_entrada)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 7 and dados_entrada.tipo_pessoa == "1":
        try:
            chrome = abre_navegador()
            policia_federal.consulta_policia_federal(chrome, dados_entrada)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 8 and dados_entrada.tipo_pessoa == "1":
        try:
            chrome = abre_navegador()
            policia_civil.consulta_policia_civil(chrome, dados_entrada)
        except Exception as e:
            print(e)
            print("HOUVE UM PROBLEMA NA CONSULTA!")
            os.system("pause")
    elif opcao == 9:
        return opcao
    elif opcao == 0:
        return
    else:
        raise Exception("Opção inválida!")

    os.system('cls')
    print("\n\nACOMPANHE A JANELA ABERTA PARA VERIFICAR SE É NECESSÁRIA ALGUMA INTERVENÇÃO HUMANA!")
    print("\n\nFECHE A JANELA ABERTA PARA FAZER NOVAS CONSULTAS")

    # Aguarda até que a janela seja fechada
    while chrome.window_handles:
        pass


if __name__ == "__main__":
    # Recebe dados de entrada do usuário
    os.system('cls')
    dados_entrada = dados_consulta.DadosConsulta()
    # print("Tipo da pessoa: ", dados_entrada.tipo_pessoa, " \nNome da pessoa: ", dados_entrada.nome_pessoa)

    opcao = 1
    while opcao != 0:
        try:
            opcao = apresenta_menu(dados_entrada)
            if opcao == 0:
                break
            opcao = escolhe_opcao(opcao, dados_entrada)
            if opcao == 9:
                os.system("cls")
                dados_entrada = dados_consulta.DadosConsulta()
            else:
                print("JANELAS FECHADAS!")
                input("Pressione ENTER para finalizar...")
        except:
            print("Tente novamente!")

