import flet as ft
import google.generativeai as genai

# Configurar sua API Key aqui
genai.configure(api_key="SUA_API")

model = genai.GenerativeModel("gemini-1.5-flash")

def chatbot(prompt):
    response = model.generate_content(prompt)
    return response.text

def main(page: ft.Page):
    page.title = "Chatbot com Gemini"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 500
    page.window_height = 700
    page.bgcolor = "#121212"
    page.scroll = "auto"

    
    chat_display = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True,
        padding=10
    )

    user_input = ft.TextField(
        label="Digite sua mensagem",
        expand=True,
        multiline=True,
        min_lines=1,
        max_lines=4,
        bgcolor="#1E1E1E",
        border_color="#333333",
        text_style=ft.TextStyle(color="white")
    )

    def send_message(e=None):
        if not user_input.value.strip():
            return

        
        chat_display.controls.append(
            ft.Container(
                content=ft.Text(f"Você: {user_input.value}", size=14, color="#BB86FC"),
                padding=10,
                # bgcolor="#2C2C2C",
                border_radius=6
            )
        )
        page.update()

       
        resposta = chatbot(user_input.value)
        chat_display.controls.append(
            ft.Container(
                content=ft.Text(f"Gemini: {resposta}", size=14, color="#03DAC5"),
                padding=10,
                # bgcolor="#1F1F1F",
                border_radius=6
            )
        )
        user_input.value = ""
        page.update()

    send_button = ft.ElevatedButton("Enviar", on_click=send_message)

    page.add(
        ft.Container(
            content=ft.Column([
                ft.Text("Chatbot com Gemini", size=24, weight="bold", color="#BB86FC"),
                ft.Divider(color="#333333"),
                ft.Container(
                    content=chat_display,
                    expand=True,
                    height=500,
                    bgcolor="#1A1A1A",
                    border_radius=10
                ),
                ft.Row([user_input, send_button])
            ]),
            padding=20,
            expand=True
        )
    )

    page.on_keyboard_event = lambda e: send_message(e) if e.key == "Enter" and not e.shift else None

ft.app(target=main)
