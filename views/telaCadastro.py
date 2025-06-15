import flet as ft

class Cadastro(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Image, title: str, bgcolor: str):
        super().__init__()
        self.route                  = "\\cadastro"
        self.page                   = page
        self.logo                   = logo
        self.title                  = title
        self.bgcolor                = bgcolor
        
        self.banner = ft.Row(
            controls=[logo, ft.Text(self.title)],
            expand=True,
            alignment=ft.MainAxisAlignment.CENTER
        )

        self.appbar = ft.AppBar(
            title=self.banner,
            center_title=True,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            actions=[ft.IconButton(ft.Icons.WB_SUNNY_OUTLINED)],
        )

        self.text_cadastro = ft.Text(
            "Cadastro",
            color="#2a688a",
            size=25,
            font_family="League Spartan",
            weight=ft.FontWeight.W_600,
        )

        self.login_container = ft.Container(
            content=self.text_cadastro,
            padding=ft.padding.only(bottom=38) 
        )

        self.field_cpf = self.create_field("Cpf", False, "#2a688a")

        self.field_name = self.create_field("Nome", False, "#2a688a")
        
        self.field_email = self.create_field("Email", False, "#2a688a")

        self.field_call = self.create_field("Telefone", False, "#2a688a")

        self.field_senha = self.create_field("Senha", True, "#2a688a")

        self.botao_cadastro = ft.Row(
            [
                ft.ElevatedButton(
                    "Cadastrar",
                    width=160,
                    height=47,
                    bgcolor='red',
                    color='white',
                     on_click=self.entrar_click,
                    style=ft.ButtonStyle(
                        text_style=ft.TextStyle(
                            size=22,
                            font_family="Open Sans",
                            weight=ft.FontWeight.W_700
                        )
                    )
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    
        self.body = ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        content=self.text_cadastro,
                        alignment=ft.alignment.center,
                    ),
                    self.field_cpf,
                    self.field_name,
                    self.field_email,
                    self.field_call,
                    self.field_senha,
                    ft.Row([self.botao_cadastro], alignment=ft.MainAxisAlignment.CENTER)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            ),
            expand=True,
        )

        self.controls = [
            self.body
        ]


    def create_field(self, nome: str, password: bool, cor: str, size: int = 20):
        return ft.TextField(
            label=nome,
            password=password,
            can_reveal_password=True,
            label_style=ft.TextStyle(
                color=cor,
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=size
            ),
            color='black',
            border_color="#b8b9bb",
            cursor_color="red",
            bgcolor='white'
        )

    def entrar_click(self, e):
        # Aqui você pode fazer validação do login se quiser
        self.page.go("/home")
