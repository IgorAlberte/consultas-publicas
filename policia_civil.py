from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def consulta_policia_civil(chrome, dados_consulta):
    """Realiza consulta à base da Polícia Civil de MG. Consulta APENAS PARA PF"""

    chrome.get("https://wwws.pc.mg.gov.br/atestado/solicitarsel.do?evento=x&amp;fwPlc=s")

    chrome.maximize_window()

    chrome.maximize_window()
    # Preenche dados para consulta
    campo_rg = chrome.find_element_by_id("rgAux_Arg")
    campo_rg.click()
    campo_rg.send_keys(dados_consulta.numeros_identidade)

    nome = chrome.find_element_by_id("nomeAux_Arg")
    nome.click()
    nome.send_keys(dados_consulta.nome_pessoa)

    nascimento = chrome.find_element_by_name("dtNascimentoAux_Arg")
    nascimento.click()
    nascimento.send_keys(dados_consulta.nascimento)