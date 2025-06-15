import flet as ft
from datetime import datetime

class AgendamentoSetor(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route          = "//agendamento_setor"
        self.page           = page
        self.setor_selecionado = ft.Ref[ft.RadioGroup]()

        setores = [
            "Odontologia", "Pediatra", "Clinico Geral", 
            "Ortopedista", "Fisioterapia", "Psicologia"
        ]

        self.controls = [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, icon_color=ft.Colors.BLACK, on_click=lambda _: self.page.go("/home")),
                title=ft.Text("Agendamento", size=28, color="#2a688a", weight=ft.FontWeight.W_700),
                center_title=True,
                bgcolor="#dddddd"
            ),
            ft.Column([
                ft.TextField(label="informe seu cpf", text_align=ft.TextAlign.CENTER),
                ft.Text("Selecione o setor:", size=18, weight=ft.FontWeight.W_600, color="#2a688a"),
                ft.RadioGroup(
                    ref=self.setor_selecionado,
                    content=ft.Column([
                        ft.Radio(value=s, label=s, fill_color="teal", active_color="red") for s in setores
                    ])
                ),
                ft.ElevatedButton(
                    "Prosseguir",
                    bgcolor="red",
                    color="white",
                    on_click=self.prosseguir_click
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
            )
        ]

    def prosseguir_click(self, e):
        self.page.go("/agendamento_disponibilidade")


class AgendamentoDisponibilidade(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/agendamento_disponibilidade"
        self.page = page

        
        self.controls = [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, icon_color=ft.Colors.BLACK, on_click=lambda _: self.page.go("/agendamento_setor")),
                title=ft.Text("Agendamento", size=28, color="#2a688a", weight=ft.FontWeight.W_700),
                center_title=True,
                bgcolor="#dddddd"
            ),
            ft.Column([
                ft.Text("Disponibilidade (odontologia)", size=20, weight=ft.FontWeight.BOLD, color="#2a688a"),
                self.card("fabiola", "16/02 às 15hr"),
                self.card("Juliano", "2/02 às 7hr")
            ], spacing=20)
        ]

    def card(self, medico, data_hora):
            return ft.Row(
                 controls=[
                    ft.Container(
                        content=ft.Column([
                            ft.Text(f"Medico:{medico}", size=18, color="#2a688a", weight=ft.FontWeight.BOLD),
                            ft.Text(f"Data: {data_hora}", size=16),
                            ft.ElevatedButton("Marcar", bgcolor="red", color="white")
                        ]),
                        padding=15,
                        bgcolor="white",
                        border_radius=5,
                        shadow=ft.BoxShadow(blur_radius=8, color="#aaa"),
                        expand=True,
                    )
                 ],
                 expand=True
            )
    

