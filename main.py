from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.clock import mainthread  # Import mainthread decorator


class FileChooserApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.file_chooser = FileChooserListView(filters=["*.pdf"])
        layout.add_widget(self.file_chooser)

        select_button = Button(text="Select File", size_hint=(1, None), height=50)
        select_button.bind(on_press=self.select_file)
        layout.add_widget(select_button)

        self.file_path_label = Label(text="")
        layout.add_widget(self.file_path_label)

        return layout

    @mainthread  # Decorate the method to ensure it runs on the main thread
    def select_file(self, instance):
        selected_file = self.file_chooser.selection and self.file_chooser.selection[0] or ""
        self.file_path_label.text = selected_file


if __name__ == '__main__':
    FileChooserApp().run()
