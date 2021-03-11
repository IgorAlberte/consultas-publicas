from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def primeira_instancia(chrome, dados_consulta, natureza):
    """Realiza consulta 1ª Instância - Cível. Natureza pode assumir 1 - Cível ou 2 - Criminal"""
    chrome.get(
        "http://rupe.tjmg.jus.br/rupe/justica/publico/certidoes/criarSolicitacaoCertidao.rupe?solicitacaoPublica=true")

    # chrome.maximize_window()

    # Escolhe tipo de instância NORMAL
    escolhe_tipo_instancia(chrome, 1)

    escolhe_instancia(chrome, 1)

    # Escolhe tipo de instância NORMAL
    escolhe_tipo_instancia(chrome, 1)

    # Seleciona a natureza da instancia
    if natureza == 1:
        escolhe_natureza_instancia(chrome, "CIVEL")
    elif natureza == 2:
        escolhe_natureza_instancia(chrome, "CRIMINAL")

    # Seleciona o tipo de pessoa
    escolhe_tipo_pessoa(chrome, int(dados_consulta.tipo_pessoa))

    # Preenche dados da pessoa pesquisada
    preenche_dados_pessoa(chrome, dados_consulta)

    # Escolhe a comarca de Montes Claros
    escolhe_comarca(chrome)

    # Preenche dados do solicitante
    preenche_dados_solicitante(chrome, dados_consulta)


def segunda_instancia(chrome, dados_consulta, natureza):
    """Consulta 2ª instância Cível. Natureza pode assumir 1 - Cível ou 2 - Criminal"""
    chrome.get(
        "http://rupe.tjmg.jus.br/rupe/justica/publico/certidoes/criarSolicitacaoCertidao.rupe?solicitacaoPublica=true")

    # chrome.maximize_window()
    escolhe_instancia(chrome, 2)

    # Escolhe tipo de instância NORMAL
    escolhe_tipo_instancia(chrome, 2)

    # Seleciona a natureza da instancia
    if natureza == 1:
        escolhe_natureza_instancia(chrome, "CIVEL")
    elif natureza == 2:
        escolhe_natureza_instancia(chrome, "CRIMINAL")

    escolhe_instancia(chrome, 2)

    # Seleciona o tipo de pessoa
    escolhe_tipo_pessoa(chrome, int(dados_consulta.tipo_pessoa))

    # Preenche dados da pessoa pesquisada
    preenche_dados_pessoa(chrome, dados_consulta)

    # Preenche dados do solicitante
    preenche_dados_solicitante(chrome, dados_consulta)


def escolhe_instancia(chrome, instancia):
    """Recebe a instância (1 ou 2) que será escolhida para consulta"""
    try:
        # Encontra os radio buttons de Instância
        instancia_certidao_1 = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoInstanciaCertidao:0"))
        )
        # instancia_certidao_1 = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoInstanciaCertidao:0")

        instancia_certidao_2 = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoInstanciaCertidao:1"))
        )
        # instancia_certidao_2 = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoInstanciaCertidao:1")

        if instancia == 1:
            instancia_certidao_1.click()
        elif instancia == 2:
            instancia_certidao_2.click()
        else:
            print("PROBLEMA AO ESCOLHER INSTANCIA DE CONSULTA")
    except:
        raise Exception("Houve um problema ao localizar o item - Instância!")


def escolhe_tipo_instancia(chrome, instancia):
    """Escolhe o tipo de instância como NORMAL"""

    if instancia == 1:
        try:
            algo = WebDriverWait(chrome, 120).until(
                EC.element_to_be_clickable((By.XPATH, "//select[@id='formCriacaoSolicitacaoCertidao:tipoCertidaoCertidao"
                                                      "']//option[@value='VINTENARIA']"))
            )
            # Seleciona o tipo de instancia NORMAL
            tipo_instancia = Select(chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoCertidaoCertidao"))
            tipo_instancia.select_by_value("NORMAL")
        except:
            raise Exception("Houve um problema ao localizar o item - Tipo Instância!")

    else:
        try:
            algo = WebDriverWait(chrome, 120).until(
                EC.element_to_be_clickable((By.XPATH, "//select[@id='formCriacaoSolicitacaoCertidao:tipoCertidaoCertidao"
                                                      "']//option[@value='FINS_ELEITORAIS']"))
            )
            # Seleciona o tipo de instancia NORMAL
            tipo_instancia = Select(chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoCertidaoCertidao"))
            tipo_instancia.select_by_value("NORMAL")
        except:
            raise Exception("Houve um problema ao localizar o item - Tipo Instância!")


def escolhe_natureza_instancia(chrome, natureza):
    """Natureza pode assumir os valores CIVEL ou CRIMINAL. É string."""
    try:
        if natureza == "CIVEL":
            natureza_civel = WebDriverWait(chrome, 120).until(
                EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoNaturezaCertidao:0"))
            )
            # natureza_civel = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoNaturezaCertidao:0")
            print ("LOCALIZOU NATUREZA CÍVEL")
            natureza_civel.click()
        elif natureza == "CRIMINAL":
            natureza_criminal = WebDriverWait(chrome, 120).until(
                EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoNaturezaCertidao:1"))
            )
            # natureza_criminal = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoNaturezaCertidao:1")
            print("LOCALIZOU NATUREZA CRIMINAL")
            natureza_criminal.click()
        else:
            raise Exception("PROBLEMA AO ESCOLHER NATUREZA DA INSTÂNCIA")
    except:
        raise Exception("Houve um problema ao localizar o item - Natureza Instância!")


def escolhe_tipo_pessoa(chrome, tipo):
    """tipo = 1 para PF e tipo = 2 para PJ"""

    try:
        # Encontra os radio buttons de Tipo de Pessoa
        pessoa_fisica = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoDocPesquisado:0"))
        )
        # pessoa_fisica = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoDocPesquisado:0")

        pessoa_juridica = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:tipoDocPesquisado:1"))
        )
        # pessoa_juridica = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:tipoDocPesquisado:1")

        if tipo == 1:
            pessoa_fisica.click()
        elif tipo == 2:
            pessoa_juridica.click()
        else:
            raise Exception("PROBLEMA AO ESCOLHER TIPO DE PESSOA")

    except:
        raise Exception("Houve um problema ao localizar o item - Tipo Pessoa!")


def escolhe_comarca(chrome):
    """A comarca só é escolhida quando a consulta é de 1ª instância; Comarca de Montes Claros"""
    try:
        algo = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='formCriacaoSolicitacaoCertidao:comarcaCertidao2"
                                                  "']//option[@value='164']"))
        )
        # Encontra o combobox a marcar a comarca
        comarca = Select(chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:comarcaCertidao2"))
        # comarca.select_by_value("164")  # Value da Comarca de Montes Claros
        comarca.select_by_visible_text("MONTES CLAROS")
    except:
        raise Exception("Houve um problema ao localizar o item - Comarca!")


def preenche_dados_pf(chrome, dados_consulta):
    """Preenche campos dos dados da Pessoa Física Consultada"""

    try:
        # Campo de CPF
        cpf = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:cpfPesquisa"))
        )
        # cpf = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:cpfPesquisa")

        cpf.click()
        cpf.send_keys(dados_consulta.cpf)

        # Campo de nome
        nome = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:nomePesquisado")
        nome.send_keys(dados_consulta.nome_pessoa)

        # Identidade (apenas números)
        identidade = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:identidadePesquisado")
        identidade.send_keys(dados_consulta.numeros_identidade)

        # Nome da mãe
        nome_mae = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:nomeMaePesquisado")
        nome_mae.send_keys(dados_consulta.nome_mae)

        # Nome do pai
        nome_pai = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:nomePaiPesquisado")
        nome_pai.send_keys(dados_consulta.nome_pai)

    except:
        raise Exception("Houve um problema ao localizar o item - Dados PF!")


def preenche_dados_pj(chrome, dados_consulta):
    """Preenche campos da Pessoa Jurídica consultada"""

    try:
        # CNPJ da empresa consultada
        cnpj = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:cnpjPesquisa"))
        )
        # cnpj = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:cnpjPesquisa")

        cnpj.click()
        cnpj.send_keys(dados_consulta.cnpj)

        # Nome da empresa consultada
        nome = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:nomePesquisado")
        nome.send_keys(dados_consulta.nome_pessoa)
    except:
        raise Exception("Houve um problema ao localizar o item - Dados PJ!")


def preenche_dados_pessoa(chrome, dados_consulta):
    """Escolhe a função adequada para a pessoa recebida, de acordo com o tipo - PF ou PJ"""
    if dados_consulta.tipo_pessoa == '1':
        preenche_dados_pf(chrome, dados_consulta)
    else:
        preenche_dados_pj(chrome, dados_consulta)


def preenche_dados_solicitante(chrome, dados_consulta):
    """Preenche dados do solicitante da consulta"""

    # Localiza campos
    nome_solicitante = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:nomeSolicitante")
    cpf_solicitante = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:cpfSolicitante")
    email_solicitante = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:email")
    confirm_email_solicitante = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:confirmacaoEmail")

    # botão de gerar código
    # gerar_codigo = chrome.find_element_by_id("formCriacaoSolicitacaoCertidao:btnGerarCodigo")
    gerar_codigo = chrome.find_element_by_name("formCriacaoSolicitacaoCertidao:btnGerarCodigo")

    # Preenche campos
    nome_solicitante.send_keys(dados_consulta.nome_solicitante)
    cpf_solicitante.click()
    cpf_solicitante.send_keys(dados_consulta.cpf_solicitante)
    email_solicitante.send_keys(dados_consulta.email_solicitante)
    confirm_email_solicitante.send_keys(dados_consulta.email_solicitante)

    # Solicita a geração do código
    chrome.maximize_window()
    gerar_codigo.click()

    try:
        confirmacao_codigo = WebDriverWait(chrome, 120).until(
            EC.element_to_be_clickable((By.ID, "formCriacaoSolicitacaoCertidao:formEmailCodigoVerificacao:gerarCodigoVerificacaoCertidao"))
        )
        # confirmacao_codigo.click()
    except:
        raise Exception("Houve um problema ao localizar o item - Dados solicitante!")

