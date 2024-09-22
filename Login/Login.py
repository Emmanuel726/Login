import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    
    x1 = "0"
    x2 = "100"
    
    def traslate(self): # Metodo para trasladar el Login y el Register
        if self.x1 == "0":
            self.x1 = "100"
            self.x2 = "0"
        else:
            self.x1 = "0"
            self.x2 = "100"
    ...

style_a = { # -> Estilos para los componentes de la barra de navegacion
    "#a": {
        "position": "relative",
        "font-size": "16px",
        "color": "#e4e4e4",
        "text-decoration": "none",
        "font-weight": "500",
        "margin-right": "30px",
        "cursor": "pointer",
    },
    "#a::after": {
        "content": '""',
        "position": "absolute",
        "left": "0",
        "bottom": "-6px",
        "width": "100%",
        "height": "2px",
        "background": "#e4e4e4",
        "border-radius": "5px",
        "transform": "translateY(10px)",
        "opacity": "0",
        "transition": ".5s",
    },
    "#a:hover::after": {
        "transform": "translateY(0)",
        "opacity": "1",
    }
}

def navbar() -> rx.Component: # -> Barra de navegacion
    return rx.flex(
        rx.link("Home", id="a",),
        rx.link("About", id="a",),
        rx.link("Services", id="a",),
        rx.link("Contact", id="a",),
        style={
            "position": "fixed",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "10%",
            "padding": "25px 12.5px",
            "background": "transparent",
            "display": "flex",
            "justify-content": "right",
            "align-items": "center",
            "z-index": "100",
        },
    )

def fondo() -> rx.Component: # -> Imagen de fondo difuminado
    return rx.container(
        style={
            "width": "100%",
            "height": "100vh",
            "background": "url(/wallpaperbetter.jpg) no-repeat",
            "background-size": "cover",
            "background-position": "center",
            "filter": "blur(10px)",
        }
    )

def contenedor() -> rx.Component: # -> Contenedor principal
    return rx.flex(
        rx.flex( # -> Contenedor para la descripcion de la web
            style={
                "width": "55%",
                "height": "100%",
                "border": "5px double transparent",
            }
        ),
        rx.flex( # -> Contenedor para el Login y el Register
            rx.flex( # -> Contenedor del Login
                rx.text("Login", color="white", font_weight ="bold", font="oblique bold 300% cursive", margin_top="80px"),
                rx.input(
                    placeholder="User",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    border_radius = "10px"
                ),
                rx.input(
                    placeholder="Password",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    type="password",
                    border_radius = "10px"
                ),
                rx.hstack(
                    rx.checkbox(
                        "Remember me",
                        spacing="2",
                    ),
                    rx.link("Forgot your password.?", cursor="pointer", color="white"),
                    align="center",
                    spacing="7",
                ),
                rx.button(
                    rx.text("Login", size="4"),
                    width = "80%",
                    height = "10%",
                    cursor = "pointer",
                    bg="#c4103d"
                ),
                rx.hstack(
                    rx.text("Do not have an account.?", font_size = "15px"),
                    rx.button("Register", font_size = "15px", cursor = "pointer", font="bold", color="white", bg = "transparent", on_click=State.traslate),
                    spacing="1",
                    align="center"
                ),
                style={ # -> Estilos para el contenedor del Login
                    "position": "absolute",
                    "width": "100%",
                    "height": "100%",
                    "border": "5px double transparent",
                    "transform": f"translateX({State.x1}%)",
                    "transition": "transform .6s ease",
                    "transition-delay": ".7s",
                },
                direction="column",
                align="center",
                spacing="4"
            ),
            rx.flex( # -> Contenedor del Register
                rx.text("Register", color="white", font_weight ="bold", font="oblique bold 300% cursive", margin_top="20px"),
                rx.input(
                    placeholder="User",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    border_radius = "10px",
                ),
                rx.input(
                    placeholder="Email",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    border_radius = "10px",
                ),
                rx.input(
                    placeholder="Password",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    type="password",
                    border_radius = "10px",
                ),
                rx.input(
                    placeholder="Repeat your Password",
                    font_size = "100%",
                    width = "80%",
                    height = "10%",
                    padding = "5px",
                    type="password",
                    border_radius = "10px",
                ),
                rx.hstack(
                    rx.checkbox(
                        "Accept the terms and conditions",
                        spacing="2",
                    ),
                    align="start",
                ),
                rx.button(
                    rx.text("Register", size="4"),
                    width = "80%",
                    height = "10%",
                    cursor = "pointer",
                    bg="#c4103d"
                ),
                rx.hstack(
                    rx.text("You already have an account.?", font_size = "15px"),
                    rx.button("Login", font_size = "15px", cursor = "pointer", font="bold", color="white", bg = "transparent", on_click=State.traslate),
                    spacing="1",
                    align="center"
                ),
                style={ # -> Estilos para el contenedor del Register
                    "position": "absolute",
                    "width": "100%",
                    "height": "100%",
                    "border": "5px double transparent",
                    "transform": f"translateX({State.x2}%)",
                    "transition": "transform .6s ease",
                    "transition-delay": ".7s",
                },
                direction="column",
                align="center",
                spacing="4",
            ),
            style={ # -> Estilos para el contenedor del Login y el Register
                "width": "45%",
                "height": "100%",
                "border": "5px double transparent",
                "justify-content": "center",
                "align-items": "center",
                "overflow": "hidden",
                "display": "flex",
                "background": "transparent",
                "backdrop-filter": "blur(20px)",
            }
        ),
        style={ # -> Estilos para el contenedor principal
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "width": "75%",
            "height": "80%",
            "background": "url('/wallpaperbetter.jpg') no-repeat",
            "background-size": "cover",
            "background-position": "center",
            "border-radius": "10px",
            "margin-top": "20px",
        }
    )

@rx.page(route="/", title="Login")
def login() -> rx.Component: # -> Pagina de Login y Register
    return rx.flex(
        navbar(),
        fondo(),
        contenedor(),
    )


app = rx.App(style=style_a)
