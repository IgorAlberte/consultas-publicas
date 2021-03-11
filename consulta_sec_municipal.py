from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def consulta_secretaria_municipal(chrome, dados_consulta):
    """Realiza consulta à secretaria municipal"""
    chrome.get(
        "http://sis.montesclaros.mg.gov.br:8080/cidadao/servlet/br.com.cetil.ar.jvlle.hatendimento")

    chrome.maximize_window()

    # Aciona botão de baixar certidão negativa
    botao_certidao_negativa(chrome)

    # Preenche campo de CPF/CNPJ
    chrome.switch_to_frame("iframe") # acessa frame da janela de inserção de dados
    preenche_dados_consulta(chrome, dados_consulta)
    ' volta para conteúdo principal: driver.switch_to_default_content()'


def botao_certidao_negativa(chrome):
    """Aciona botão de consultar certidão negativa"""
    try:
        certidao_negativa = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Certidão Negativa de Débitos"))
        )
        # certidao_negativa = chrome.find_element_by_link_text("Certidão Negativa de Débitos")
        certidao_negativa.click()
    except:
        print("Houve um problema ao localizar o item!")


def preenche_dados_consulta(chrome, dados_consulta):
    """Preenche dados para consulta"""
    # preenche CPF/CNPJ
    try:
        cpf_cnpj = WebDriverWait(chrome, 30).until(
            EC.element_to_be_clickable((By.NAME, "_CONTRIBUINTE"))
        )
        # cpf_cnpj = chrome.find_element_by_id("_CONTRIBUINTE")
        cpf_cnpj.click()

        if dados_consulta.tipo_pessoa == "1":
            cpf_cnpj.send_keys(dados_consulta.cpf)
        else:
            cpf_cnpj.send_keys(dados_consulta.cnpj)

        # seleciona a finalidade
        finalidade = Select(chrome.find_element_by_name("_FINALIDADE"))
        finalidade.select_by_value("5")  # Seleciona opção  FINS DE DIREITO

        cpf_cnpj.click()  # clica para aparecer próximo campo

        # preenche dados do requerente
        nome_requerente = WebDriverWait(chrome, 30).until(
            EC.element_to_be_clickable((By.ID, "_NOMEREQUERENTE"))
        )

        # nome_requerente = chrome.find_element_by_id("_NOMEREQUERENTE")
        nome_requerente.click()
        nome_requerente.send_keys(dados_consulta.nome_solicitante)

        # Apertar botão de consulta
        botao = chrome.find_element_by_name("BTN_CONFIRMAR")
        botao.click()

    except:
        print("Houve um problema ao localizar o item!")
