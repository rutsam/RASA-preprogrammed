from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_menu_1"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         dispatcher.utter_message(text="Hitamo hagati ya 1 na karindwi, kuri rimwe uraba ihisemo amakuru ya covid, kabiri imibare y'abantu")
         answer_1 = tracker.get_slot("answer_1")
         if answer_1==None:
             #dispatcher.uuter_message(text="Nta slot irimo")
             print("No dispatcher found")

         return []

class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_menu_2"
     
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         answer_1 = tracker.get_slot("answer_1")
         if answer_1==1:
             dispatcher.utter_message(text="Hello World! you have chosen the first option")
         elif answer_1==2:
             dispatcher.utter_message(text="You have chosen the second option")
         elif answer_1==3:
             dispatcher.utter_message(text="You have chosen the third option")
         else:
             dispatcher.utter_message(text="Hitamo hagati ya 1 na karindwi, kuri rimwe uraba ihisemo amakuru ya covid, kabiri imibare y'abantu")
         
         return []
