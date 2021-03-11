from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def consulta_policia_federal(chrome, dados_consulta):
    """Realiza consulta à base da Polícia Federal. Consulta APENAS PARA PF"""
    chrome.get(
        "https://servicos.dpf.gov.br/antecedentes-criminais/certidao")

    chrome.maximize_window()

    # Preenche dados para emissão
    nome = chrome.find_element_by_id("inputNome_input")
    nome.click()
    nome.send_keys(dados_consulta.nome_pessoa)

    nome_pai = chrome.find_element_by_id("inputNomePai_input")
    nome_pai.click()
    nome_pai.send_keys(dados_consulta.nome_pai)

    nome_mae = chrome.find_element_by_id("inputNomeMae_input")
    nome_mae.click()
    nome_mae.send_keys(dados_consulta.nome_mae)

    nascimento = chrome.find_element_by_id("inputDataNascimento_input")
    nascimento.click()
    nascimento.send_keys(dados_consulta.nascimento)

    cpf = chrome.find_element_by_id("inputCpf_input")
    cpf.click()
    cpf.send_keys(dados_consulta.cpf)


