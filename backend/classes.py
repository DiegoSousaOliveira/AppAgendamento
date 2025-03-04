from typing import List
from abc import ABC
from datetime import date, time

class Pessoa(ABC):
    def __init__(self, nome: str, cpf: str, email: str, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone


class Paciente(Pessoa):
    def __init__(self, cpf: str, nome: str, email: str, senha: str, telefone: str):
        super().__init__(nome, cpf, email, telefone)
        self.senha = senha
    
    def atualizar_dados(self, cpf: str, nome: str, email: str, senha: str, telefone): pass


class Medico(Pessoa):
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, especialidade: str):
        super().__init__(nome, cpf, email, telefone)
        self.especialidade = especialidade


class Endereco:
    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, complemento: str,cep: str):
        self.rua:str        = rua
        self.numero:str     = numero
        self.bairro:str     = bairro
        self.cidade:str     = cidade
        self.estado:str     = estado
        self.complemeto:str = complemento
        self.cep:str        = cep

    def atualizar_dados(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, cep: str): pass


class Consulta:
    def __init__(self, data: date, hora: time, medico: Medico, paciente: Paciente):
        self.data = data
        self.hora = hora
        self.medico = medico
        self.paciente = paciente


class Hospital:
    def __init__(self, nome: str, endereco: Endereco, telefone: str):
        self.nome:str               = nome
        self.telefone:str           = telefone
        self.endereco:Endereco      = endereco
        self.medicos: List[Medico]      = []
        self.consultas: List[Consulta]  = []
        self.pacientes: List[Paciente]  = []

    def cadastrar_medico(self, medico: Medico):pass

    def cadastrar_paciente(self, paciente: Paciente):pass

    def remover_medico(self, medico: Medico):pass

    def remover_paciente(self, paciente: Paciente):pass
    
    def listar_medicos(self):pass

    def listar_pacientes(self):pass

    def listar_consultas(self):pass

    def buscar_medico_por_especialidade(self, especialidade: str):pass

    def buscar_medico_por_cpf(self, cpf: str):pass

    def buscar_paciente_por_cpf(self, cpf: str):pass

    def marcar_consulta(self, consulta: Consulta):pass
    
    def cancelar_consulta(self, cpf: str):pass

    def buscar_consulta_por_horario(self, data: date, hora: time):pass

    def buscar_consultas_por_paciente(cpf):pass
