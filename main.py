from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from bs4 import BeautifulSoup
import requests
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.imagelist import SmartTileWithLabel
import threading
Window.size=(1000,600)
class Interface(MDBoxLayout):
    def processing(self):
        keyword = self.ids.input_keyword.text
        page = requests.get(f"https://unsplash.com/s/photos/{keyword}")
        soup = BeautifulSoup(page.content, 'lxml')
        rows = soup.find_all('div', class_='ripi6')
        for row in rows:
            figures = row.find_all('figure')
            for i in range(2):
                img = figures[i].find('img', class_='YVj9w')
                source = img['src']
                tiles = SmartTileWithLabel(source=source, box_color=[1, 1, 1, 0])
                self.grid.add_widget(tiles)
    def scraping(self):
        objects=self.ids.scroll_view.children
        if objects:
            self.ids.scroll_view.remove_widget(objects[0])
        self.grid=MDGridLayout(
            cols= 3,
        adaptive_height= True,
        spacing= "10dp",
        padding= "10dp",
        row_default_height= "200dp",
        row_force_default= True
        )
        self.ids.scroll_view.add_widget(self.grid)
        process=threading.Thread(target=self.processing)
        process.start()

class ScraperApp(MDApp):
    pass

ScraperApp().run()