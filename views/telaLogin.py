import flet as ft

class Login(ft.View):
    def __init__(self, page: ft.Page, logo: ft.Row, title: str, bgcolor: str):
        super().__init__()
        self.route                  = "\login"
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

        self.texto_login = ft.Text(
            "LOGIN",
            color="#2a688a",
            size=25,
            font_family="League Spartan",
            weight=ft.FontWeight.W_600,
        )

        self.login_container = ft.Container(
            content=self.texto_login,
            padding=ft.padding.only(bottom=38) 
        )

        self.campo_email = ft.TextField(
            label="Email",
            label_style=ft.TextStyle(
                color="#2a688a",
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=20
            ), 
            color='black',
            border_color="#b8b9bb",
            cursor_color="red",
            bgcolor='white'
        )

        self.campo_senha = ft.TextField(
            label="Senha",
            password=True,
            can_reveal_password=True,
            label_style=ft.TextStyle(
                color="#2a688a",
                font_family="Open Sans",
                weight=ft.FontWeight.W_700,
                size=20
            ),
            color='black',
            border_color="#b8b9bb",
            cursor_color="red",
            bgcolor='white'
        )

        self.texto_cadastro = ft.Text("Não tem cadastro? Cadastre-se Aqui")

        self.botao_entrar = ft.Row(
            [
                ft.ElevatedButton(
                    "Entrar",
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
            alignment="center"
        )
    
        self.body = ft.SafeArea(
            ft.Column(
                [
                    ft.Container(
                        content=ft.Text("LOGIN", color="#2a688a", size=30, weight=ft.FontWeight.W_600),
                        alignment=ft.alignment.center,
                    ),
                    self.campo_email,
                    self.campo_senha,
                    ft.Row([self.botao_entrar], alignment="center")
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


    def entrar_click(self, e):
        # Aqui você pode fazer validação do login se quiser
        self.page.go("/home")
