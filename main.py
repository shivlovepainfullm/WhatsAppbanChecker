from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import webbrowser

class CheckerApp(App):

    def build(self):
        self.title = "WhatsApp Ban Checker"

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=15
        )

        layout.add_widget(Label(
            text="[b]WhatsApp Ban Checker[/b]",
            markup=True,
            font_size="25sp",
            size_hint_y=None,
            height=65
        ))

        layout.add_widget(Label(
            text="Enter your WhatsApp number",
            size_hint_y=None,
            height=40
        ))

        self.number = TextInput(
            hint_text="+91XXXXXXXXXX",
            multiline=False,
            size_hint_y=None,
            height=55
        )
        layout.add_widget(self.number)

        check_button = Button(
            text="Check Account Guidance",
            size_hint_y=None,
            height=55
        )
        check_button.bind(on_press=self.check_status)
        layout.add_widget(check_button)

        self.result = Label(
            text="Your account guidance will appear here.",
            halign="center",
            valign="middle"
        )
        layout.add_widget(self.result)

        support_button = Button(
            text="Official WhatsApp Support",
            size_hint_y=None,
            height=55
        )
        support_button.bind(
            on_press=lambda x: webbrowser.open(
                "https://www.whatsapp.com/contact/"
            )
        )
        layout.add_widget(support_button)

        help_button = Button(
            text="WhatsApp Help Center",
            size_hint_y=None,
            height=55
        )
        help_button.bind(
            on_press=lambda x: webbrowser.open(
                "https://faq.whatsapp.com/"
            )
        )
        layout.add_widget(help_button)

        return layout

    def check_status(self, instance):
        number = self.number.text.strip()

        if not number:
            self.result.text = "Please enter your phone number."
            return

        self.result.text = (
            "Automatic ban verification is not available.\n\n"
            "Open WhatsApp and try logging in.\n"
            "If you see an account restriction message,\n"
            "use the official Request a Review option.\n\n"
            "This app does not send or verify your number."
        )

if __name__ == "__main__":
    CheckerApp().run()
