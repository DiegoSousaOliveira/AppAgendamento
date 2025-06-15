import flet as ft
import requests


class Consultas(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "//consultas"
        self.page = page
        self.bgcolor = "#e0e0e0"

        self.appbar = ft.AppBar(
            leading=ft.IconButton(
                ft.icons.ARROW_BACK,
                icon_color=ft.Colors.BLACK,
                on_click=lambda _: self.page.go("//home")
            ),
            title=ft.Text("Consultas", size=28, color="#2a688a", weight=ft.FontWeight.W_700),
            center_title=True,
            bgcolor="#dddddd"
        )

        self.controls = [
            self.appbar,
            ft.Container(
                content=ft.Column(
                    [
                        self.card("Hoje", "Odontologia", "07:00", "Dra. Fabiola"),
                        self.card("Amanhã", "Ortopedia", "15:00", "Dr. Antonim"),
                        self.card("17/06", "Exame Próstata", "00:00", "Dr. Diego Oliveira")
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    spacing=20,
                    expand=True,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                padding=ft.Padding(20, 20, 20, 20)
            )
        ]

    def card(self, data, setor, horario, medico):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(f"📅 {data}", size=20, weight=ft.FontWeight.BOLD, color="#2a688a"),
                    ft.Row(
                        [
                            ft.Column(
                                [
                                    ft.Text(f"🩺 Setor:", color="#2a688a", weight=ft.FontWeight.W_600),
                                    ft.Text(f"⏰ Horário:", color="#2a688a", weight=ft.FontWeight.W_600),
                                    ft.Text(f"👨‍⚕️ Médico:", color="#2a688a", weight=ft.FontWeight.W_600)
                                ],
                                spacing=8,
                                width=120
                            ),
                            ft.Column(
                                [
                                    ft.Text(setor, color=ft.colors.BLACK, weight=ft.FontWeight.W_600),
                                    ft.Text(horario, color=ft.colors.BLACK, weight=ft.FontWeight.W_600),
                                    ft.Text(medico, color=ft.colors.BLACK, weight=ft.FontWeight.W_600)
                                ],
                                spacing=8
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=20
                    )
                ],
                spacing=12
            ),
            bgcolor=ft.colors.WHITE,
            border_radius=10,
            padding=20,
            width=500,
            shadow=ft.BoxShadow(blur_radius=6, color="#aaa")
        )


class CancelarConsultaView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/cancelar_consulta"
        self.page = page
        self.bgcolor = "#e0e0e0"  # Cor de fundo igual à tela de consultas
        self.consultas_checkboxes = []

        self.consultas_simuladas = [
            {
                "id": 1,
                "data": "15/06/2025",
                "hora": "08:00",
                "setor": "Odontologia",
                "medico_nome": "Dra. Ana",
                "status": "agendada"
            },
            {
                "id": 2,
                "data": "16/06/2025",
                "hora": "14:30",
                "setor": "Pediatria",
                "medico_nome": "Dr. Carlos",
                "status": "agendada"
            },
            {
                "id": 3,
                "data": "17/06/2025",
                "hora": "10:00",
                "setor": "Ortopedia",
                "medico_nome": "Dr. Pedro",
                "status": "agendada"
            }
        ]

        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK, icon_color=ft.Colors.BLACK, on_click=lambda _: self.page.go("//home")),
            title=ft.Text("Cancelar Consultas", size=28, color="#2a688a", weight=ft.FontWeight.W_700),
            center_title=True,
            bgcolor="#dddddd"
        )

        self.botao_cancelar = ft.ElevatedButton(
            text="Cancelar Selecionadas",
            bgcolor="red",
            color="white",
            on_click=self.cancelar_consultas_selecionadas
        )

        self.lista_consultas = ft.Column(
            spacing=20,
            scroll=ft.ScrollMode.AUTO,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        self.controls = [
            self.appbar,
            ft.Container(
                content=self.lista_consultas,
                padding=ft.Padding(20, 20, 20, 20),
                expand=True
            ),
            ft.Container(
                content=ft.Row(
                    [self.botao_cancelar],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                padding=ft.Padding(0, 0, 0, 20)
            )
        ]

        self.carregar_consultas_simuladas()

    def carregar_consultas_simuladas(self):
        self.consultas_checkboxes.clear()
        self.lista_consultas.controls.clear()

        consultas_agendadas = [c for c in self.consultas_simuladas if c["status"] == "agendada"]

        if not consultas_agendadas:
            self.lista_consultas.controls.append(
                ft.Text("Nenhuma consulta agendada encontrada.", size=18, color="gray")
            )
        else:
            for consulta in consultas_agendadas:
                checkbox = ft.Checkbox(label="", value=False)
                self.consultas_checkboxes.append((consulta["id"], checkbox))

                card = ft.Container(
                    content=ft.Row(
                        [
                            checkbox,
                            ft.Column(
                                [
                                    ft.Text(f"📅 Data: {consulta['data']}", weight=ft.FontWeight.W_600, color="#2a688a"),
                                    ft.Text(f"⏰ Horário: {consulta['hora']}", weight=ft.FontWeight.W_500, color=ft.colors.BLACK),
                                    ft.Text(f"🩺 Setor: {consulta['setor']}", weight=ft.FontWeight.W_500, color=ft.colors.BLACK),
                                    ft.Text(f"👨‍⚕️ Médico: {consulta['medico_nome']}", weight=ft.FontWeight.W_500, color=ft.colors.BLACK),
                                ],
                                spacing=5
                            )
                        ],
                        alignment=ft.MainAxisAlignment.START,
                        spacing=15
                    ),
                    bgcolor=ft.colors.WHITE,
                    padding=15,
                    border_radius=10,
                    shadow=ft.BoxShadow(blur_radius=6, color="#aaa"),
                    width=500
                )

                self.lista_consultas.controls.append(card)

        self.page.update()

    def cancelar_consultas_selecionadas(self, e):
        consultas_para_cancelar = [cid for cid, chk in self.consultas_checkboxes if chk.value]

        if not consultas_para_cancelar:
            self.page.snack_bar = ft.SnackBar(ft.Text("Nenhuma consulta selecionada para cancelamento.", color="white"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        # Simula cancelamento
        for consulta in self.consultas_simuladas:
            if consulta["id"] in consultas_para_cancelar:
                consulta["status"] = "cancelada"

        self.page.snack_bar = ft.SnackBar(ft.Text("Consultas canceladas com sucesso!", color="white"))
        self.page.snack_bar.open = True
        self.page.update()
        self.carregar_consultas_simuladas()
