class DadosConsulta:

    def __init__(self):
        print("\nINFORME OS DADOS PARA CONSULTA")

        self.tipo_pessoa = "0"
        self.tipo_pessoa = input("Digite 1 para Pessoa Física ou 2 para Pessoa Jurídica: ")

        while self.tipo_pessoa != "1" and self.tipo_pessoa != "2":
            self.tipo_pessoa = input("Dado incorreto! Digite 1 para Pessoa Física ou 2 para Pessoa Jurídica: ")

        self.nome_pessoa = input("Informe o nome da pessoa a ser consultada: ")

        if self.tipo_pessoa == "1":
            self.numeros_identidade = input("Informe APENAS OS NÚMEROS da identidade da pessoa consultada: ")
            self.cpf = input("Informe APENAS OS NÚMEROS do CPF da pessoa consultada: ")
            self.nascimento = input("Informe a data de nascimento da forma DD/MM/AAAA, incluindo as barras: ")
            self.nome_mae = input("Informe o nome da mãe da pessoa consultada: ")
            self.nome_pai = input("Informe o nome do pai da pessoa consultada: ")
        else:
            self.cnpj = input("Informe APENAS OS NÚMEROS do CNPJ da pessoa consultada: ")

        print("-------------------")
        input("VAMOS AOS DADOS DO SOLICITANTE DA CONSULTA. \nPressione ENTER para continuar...")

        self.nome_solicitante = input("Informe o nome do solicitante da consulta: ")
        self.cpf_solicitante = input("Informe APENAS OS NÚMEROS DO CPF do solicitante da consulta: ")
        self.email_solicitante = input("Informe o e-mail do solicitante da consulta: ")
