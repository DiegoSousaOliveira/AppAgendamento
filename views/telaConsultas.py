import flet as ft


class Consultas(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.route                  = "//consultas"
        self.page                   = page

        self.appbar = ft.AppBar(
            leading=ft.IconButton(ft.icons.ARROW_BACK, on_click=lambda _: self.page.go("//home")),
            title=ft.Text("Consultas", size=28, color="#2a688a", weight=ft.FontWeight.W_700, font_family="League Spartan"),
            center_title=True,
            bgcolor="#dddddd"
        )

        self.controls = [
            self.appbar,
            ft.Column([
                self.card("Hoje", "odontologia", "7hr", "fabiola"),
                self.card("Amanhã", "ortopedia", "15hr", "Antonim"),
                self.card("Dia 17", "exame prostata", "00hr", "Diego Oliveira")
            ], scroll=ft.ScrollMode.AUTO, spacing=20, expand=True)
        ]

    def card(self, titulo, setor, horario, medico):
            return ft.Column([
                ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color="#2a688a"),
                ft.Container(
                    content=ft.Column([
                        ft.Text(f"Setor: {setor}", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Horario: {horario}", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Médico: {medico}", weight=ft.FontWeight.BOLD),
                    ]),
                    bgcolor="white",
                    padding=15,
                    border_radius=5,
                    shadow=ft.BoxShadow(blur_radius=8, color="#aaa")
                ),
                ft.Divider(height=25, color="transparent")
            ])

    def carregar_consultas(self):
        #implementar
        pass
    
    def atualizar_status(self):
        #implementar
        pass
    
    def cancelar_consulta(self, consulta_id):
        #implementar
        pass
