from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.clock import Clock


class NovaAI(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        header = Label(
            text="Nova AI 🤖",
            font_size=26,
            size_hint_y=None,
            height=dp(65)
        )
        self.add_widget(header)

        self.chat = BoxLayout(
            orientation="vertical",
            size_hint_y=None,
            padding=dp(10),
            spacing=dp(10)
        )
        self.chat.bind(minimum_height=self.chat.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.chat)
        self.add_widget(scroll)

        bottom = BoxLayout(
            size_hint_y=None,
            height=dp(60),
            spacing=dp(5),
            padding=dp(5)
        )

        self.entry = TextInput(
            hint_text="Type your message...",
            multiline=False
        )

        self.entry.bind(
            on_text_validate=self.send_message
        )

        bottom.add_widget(self.entry)

        send = Button(
            text="Send",
            size_hint_x=None,
            width=dp(90)
        )
        send.bind(on_press=self.send_message)
        bottom.add_widget(send)

        self.add_widget(bottom)

        clear_button = Button(
            text="Clear Chat",
            size_hint_y=None,
            height=dp(45)
        )
        clear_button.bind(on_press=self.clear_chat)
        self.add_widget(clear_button)

        self.add_message(
            "Nova AI 🤖",
            "Hello! How can I help you?"
        )

    def add_message(self, sender, message):

        label = Label(
            text=f"{sender}: {message}",
            size_hint_y=None,
            text_size=(dp(350), None),
            halign="left",
            valign="top"
        )

        label.bind(
            texture_size=lambda instance, value:
            setattr(instance, "height", value[1] + dp(15))
        )

        self.chat.add_widget(label)

    def send_message(self, instance):

        message = self.entry.text.strip()

        if not message:
            return

        self.add_message("You", message)

        self.entry.text = ""

        # Typing effect
        self.add_message(
            "Nova AI 🤖",
            "Nova is typing..."
        )

        Clock.schedule_once(
            lambda dt: self.show_response(),
            1.5
        )

    def show_response(self):

        # Remove the "Nova is typing..." message
        if self.chat.children:
            self.chat.remove_widget(self.chat.children[0])

        self.add_message(
            "Nova AI 🤖",
            "I'm Nova AI 🤖\n"
            "I received your message!"
        )

    def clear_chat(self, instance):

        self.chat.clear_widgets()

        self.add_message(
            "Nova AI 🤖",
            "Chat cleared! 🧹\n\n"
            "What would you like to talk about?"
        )


class NovaAIApp(App):

    def build(self):
        return NovaAI()


if __name__ == "__main__":
    NovaAIApp().run()