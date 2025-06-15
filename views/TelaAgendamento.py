import flet as ft

class Agendamento(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route = "/agendamento_setor"
        self.page = page

        self.setor_selecionado = ft.Ref[ft.RadioGroup]()
        self.horario_selecionado = ft.Ref[ft.RadioGroup]()

        self.setores_simulados = [
            {"id": 1, "nome": "Odontologia"},
            {"id": 2, "nome": "Pediatria"},
            {"id": 3, "nome": "Clínico Geral"},
            {"id": 4, "nome": "Ortopedista"},
            {"id": 5, "nome": "Fisioterapia"},
            {"id": 6, "nome": "Psicologia"},
        ]

        self.horarios_simulados = {
            "1": ["08:00", "10:00", "14:00"],
            "2": ["09:30", "13:00", "15:00"],
            "3": ["07:45", "11:00", "16:30"],
            "4": ["08:15", "12:00"],
            "5": ["10:00", "13:30", "17:00"],
            "6": ["09:00", "11:45", "14:30"],
        }

        # Define primeiro setor como selecionado
        primeiro_setor_id = str(self.setores_simulados[0]["id"])

        # RadioGroup dos setores com valor inicial
        self.radio_group_setores = ft.RadioGroup(
            ref=self.setor_selecionado,
            value=primeiro_setor_id,
            on_change=self.atualizar_horarios,
            content=ft.Column([
                ft.Radio(value=str(setor["id"]), label=setor["nome"], fill_color="teal", active_color="red")
                for setor in self.setores_simulados
            ])
        )

        # RadioGroup dos horários (vai ser preenchido na função)
        self.radio_group_horarios = ft.RadioGroup(
            ref=self.horario_selecionado,
            content=ft.Column([])
        )

        # Define a interface (AppBar, colunas e botão)
        self.controls = [
            ft.AppBar(
                leading=ft.IconButton(ft.icons.ARROW_BACK, icon_color=ft.Colors.BLACK, on_click=lambda _: self.page.go("/home")),
                title=ft.Text("Agendamento", size=28, color="#2a688a", weight=ft.FontWeight.W_700),
                center_title=True,
                bgcolor="#dddddd"
            ),

            # Linha com setores e horários
            ft.Row(
                [
                    ft.Column(
                        [
                            ft.Text("Selecione o setor:", size=18, weight=ft.FontWeight.W_600, color="#2a688a"),
                            self.radio_group_setores,
                        ],
                        spacing=10,
                        width=300
                    ),
                    ft.VerticalDivider(width=1, thickness=1, color=ft.Colors.GREY_400),
                    ft.Column(
                        [
                            ft.Text("Horários disponíveis:", size=18, weight=ft.FontWeight.W_600, color="#2a688a"),
                            self.radio_group_horarios
                        ],
                        spacing=10,
                        width=300
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.START,
                spacing=40
            ),

            # Botão centralizado
            ft.Container(
                content=ft.Row(
                    [
                        ft.ElevatedButton(
                            "Prosseguir",
                            bgcolor="red",
                            color="white",
                            on_click=self.prosseguir_click
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    width=600
                ),
                padding=ft.Padding(20, 30, 20, 0)
            )
        ]

        # Inicializa o valor selecionado
        self.setor_selecionado.current.value = primeiro_setor_id
        self.atualizar_horarios(None)

    def atualizar_horarios(self, e):
        setor_id = self.setor_selecionado.current.value
        horarios = self.horarios_simulados.get(setor_id, [])

        self.radio_group_horarios.content.controls = [
            ft.Radio(value=hora, label=hora, fill_color="blue", active_color="green")
            for hora in horarios
        ]

        if horarios:
            self.horario_selecionado.current.value = horarios[0]

        self.page.update()

    def prosseguir_click(self, e):
        setor_id = self.setor_selecionado.current.value
        horario_escolhido = self.horario_selecionado.current.value

        if not setor_id or not horario_escolhido:
            self.page.snack_bar = ft.SnackBar(ft.Text("Selecione o setor e o horário!", color="white"))
            self.page.snack_bar.open = True
            self.page.update()
            return

        # Simula envio para próxima tela
        self.page.client_storage.set("setor_id", setor_id)
        self.page.client_storage.set("horario_escolhido", horario_escolhido)
        self.page.go("/agendamento_confirmar")
