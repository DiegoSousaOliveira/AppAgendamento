import flet as fp

def main(page: fp.Page):
    # Configurações da página
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.bgcolor = "#D3D3D3"
    page.window.width = 400
    page.fonts = {
        "League Spartan": "LeagueSpartan-VariableFont_wght.ttf"
    }

    logo = fp.Image(src="logo.png", width=50, height=50)

    textoNomeApp = fp.Text(
        "HugoMed", 
        color="#2a688a", 
        size=40, 
        font_family="League Spartan", 
        weight=fp.FontWeight.W_600
    )

    logo_completo = fp.Row([logo, textoNomeApp], alignment="center")

    page.appbar = fp.AppBar(
    title=fp.Container(
        content=logo_completo,
        margin=fp.margin.only(top=20) 
    ),
    bgcolor="#D3D3D3",
   # center_title=True  # 
)

    
    #fp.AppBar(title=logo_completo, bgcolor="#D3D3D3")
    

    texto_login = fp.Text(
        "LOGIN",
        color="#2a688a",
        size=25,
        font_family="League Spartan",
        weight=fp.FontWeight.W_600,
    )

    login_container = fp.Container(
        content=texto_login,
        padding=fp.padding.only(bottom=38) 
    )

    entrada_email = fp.TextField(
        label="Email",
        label_style=fp.TextStyle(
            color="#2a688a",
            font_family="Open Sans",
            weight=fp.FontWeight.W_700,
            size=20
        ), 
        color='black',
        border_color="#b8b9bb",
        cursor_color="red",
        bgcolor='white'
    )

    entrada_senha = fp.TextField(
        label="Senha",
        password=True,
        can_reveal_password=True,
        label_style=fp.TextStyle(
            color="#2a688a",
            font_family="Open Sans",
            weight=fp.FontWeight.W_700,
            size=20
        ),
        color='black',
        border_color="#b8b9bb",
        cursor_color="red",
        bgcolor='white'
    )

    texto_cadastro = fp.Text("Não tem cadastro? Cadastre-se Aqui")

   
    botao_entrar = fp.Row(
        [
            fp.ElevatedButton(
                "Entrar", 
                width=160,
                height=47, 
                bgcolor='red',
                color='white',
                style=fp.ButtonStyle(
                    text_style=fp.TextStyle(
                        size=22,
                        font_family="Open Sans",
                        weight=fp.FontWeight.W_700
                    )
                )
            )
        ],
        alignment="center"
    )

   
    coluna_login = fp.Column(
        [
            entrada_email,
            fp.Container(padding=3),
            entrada_senha,
            fp.Container(padding=3),
            botao_entrar,
        ],
        alignment="center",
        horizontal_alignment="center"  # Alinha os itens ao centro
    )

    page.add(
        login_container,
        coluna_login,
        texto_cadastro,
    )

fp.app(target=main)
