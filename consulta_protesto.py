from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def consulta_protesto(chrome, dados_consulta):
    """Para essa consulta, é necessário informar o CPF/CNPJ a ser consultado"""
    chrome.get(
        "https://site.cenprotnacional.org.br/")

    chrome.maximize_window()

    # cpf_cnpj = chrome.find_element_by_id("cpf_cnpj")
    cpf_cnpj = WebDriverWait(chrome, 120).until(
        EC.element_to_be_clickable((By.ID, "cpf_cnpj"))
    )

    if dados_consulta.tipo_pessoa == "1":
        cpf_cnpj.send_keys(dados_consulta.cpf)
    else:
        cpf_cnpj.send_keys(dados_consulta.cnpj)

    botao_consulta = chrome.find_element_by_id("bt-consultar")
    botao_consulta.click()

    # Pode ser necessário reconhecer que é humano após apertar o botão da consulta
