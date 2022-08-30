from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.properties import OptionProperty, StringProperty, ObjectProperty, ListProperty, AliasProperty, \
    BooleanProperty, NumericProperty
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import geocoder as geo

def phonenumber(number):
    key = "ff40a7c831ce49e8b6f4de5779038315"
    ch_nmber = phonenumbers.parse(number, "CH")
    country = geocoder.description_for_number(ch_nmber,"en")

    service_nmber = phonenumbers.parse(number, "RO")
    service = carrier.name_for_number(service_nmber, "en")

    geocodere = OpenCageGeocode(key)

    query = (country)

    results = geocodere.geocode(query)

    lat = results[0]['geometry']['lat']

    lng = results[0]['geometry']['lng']

    coords = (lat,lng)

    end = country,service,coords

    return end



    
class layoutbox(BoxLayout):
    def phonenumbertr(self):
        myinput = self.ids.text_input.text
        try:
            end = phonenumber(myinput)
            end = str(end)
        except:
            end = "sorry it didn't work" 


        self.ids.number_label.text = end
        



class trackApp(App):
    def build(self):
        Window.clearcolor = (25/255, 63/255, 189/255, 1)
        return layoutbox()



trackApp().run()
