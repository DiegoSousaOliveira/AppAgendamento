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

    def autenticar(self, email: str, cpf: str, senha: str): pass


class Medico(Pessoa):
    def __init__(self, nome: str, cpf: str, email: str, telefone: str, especialidade: str):
        super().__init__(nome, cpf, email, telefone)
        self.especialidade = especialidade


class Endereco:
    def __init__(self, rua: str, numero: str, bairro: str, cidade: str, estado: str, cep: str):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep


class Hospital:
    def __init__(self, nome: str, endereco: Endereco, telefone: str):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone


class Consulta:
    def __init__(self, data: date, hora: time, medico: Medico, paciente: Paciente):
        self.data = data
        self.hora = hora
        self.medico = medico
        self.paciente = paciente


class AgendamentoService:
    def __init__(self):
        self.medicos: List[Medico]      = []
        self.consultas: List[Consulta]  = []
        self.pacientes: List[Paciente]  = []

    def marcar_consulta(self, consulta: Consulta):pass
    
    def cancelar_consulta(self, usuario_cpf: str):pass

    def listar_consultas(self):pass

    def buscar_consulta_por_horario(self, data: date, hora: time):pass

    def buscar_consultas_por_paciente(usuario_cpf):pass

