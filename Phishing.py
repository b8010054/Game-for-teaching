import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior

class MainMenu(Screen):
    pass

class PlayScreen(Screen):
    pass

class HowToPlayScreen(Screen):
    pass

class LevelOneScreen(Screen):
    pass

class LevelTwoScreen(Screen):
    pass

class LevelThreeScreen(Screen):
    pass

class LevelFourScreen(Screen):
    pass

class LevelFiveScreen(Screen):
    pass

class Game(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='MainMenuScreen'))
        sm.add_widget(HowToPlayScreen(name='HowToPlayScreen'))
        sm.add_widget(PlayScreen(name='PlayScreen'))
        sm.add_widget(LevelOneScreen(name='LevelOneScreen'))
        sm.add_widget(LevelTwoScreen(name='LevelTwoScreen'))
        sm.add_widget(LevelThreeScreen(name='LevelThreeScreen'))
        sm.add_widget(LevelFourScreen(name='LevelFourScreen'))
        sm.add_widget(LevelFiveScreen(name='LevelFiveScreen'))

        return sm

if __name__ == '__main__':
    Window.maximize()
    Game().run()
