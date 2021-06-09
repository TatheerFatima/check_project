# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionSubmitSalesForm(Action):
    def name(self) -> Text:
        return "action_fine_reason"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["fine_reason"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("fine_reason")
        #dispatcher.utter_message(template="utter_you_entered")
        dispatcher.utter_message(template="utter_fine_if_wants_to_talk")
        return []


class ActionSubmitwhatsgoingonform(Action):
    def name(self) -> Text:
        return "action_whats_going_on"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["whats_going_on"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("whats_going_on")
        #dispatcher.utter_message(template="utter_you_entered_goingon")
        dispatcher.utter_message(template="utter_have_you_talked")
        return []


class ActionSubmitfeelingform(Action):
    def name(self) -> Text:
        return "action_feeling"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feeling"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("feeling")
        #dispatcher.utter_message(template="utter_you_entered_feeling")
        #dispatcher.utter_message(template="utter_made_you_feel")
        return []


class ActionSubmitfeelreasonform(Action):
    def name(self) -> Text:
        return "action_feel_reason"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_reason"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("feel_reason")
        #dispatcher.utter_message(template="utter_you_entered_feelreason")
        dispatcher.utter_message(template="utter_faith")
        dispatcher.utter_message(template="utter_okay")
        dispatcher.utter_message("?")

        return []


class ActionSubmitfunform(Action):
    def name(self) -> Text:
        return "action_fun"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["fun"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        #budget = tracker.get_slot("fun")
        dispatcher.utter_message(template="utter_if_wantsto_chat")
        #dispatcher.utter_message(template="utter_made_you_feel")
        return []








class ActionSubmitPositiveForm(Action):
    def name(self) -> Text:
        return "action_submit_positive"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_after_positive",
                                 positive_word=tracker.get_slot("positive_word"))
        
        return[]

class ActionSubmitcelebrationForm(Action):
    def name(self) -> Text:
        return "action_submit_celebration"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
                                 #celebration=tracker.get_slot("celebration"))
        dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_if_wantsto_chat")
                                                     
        
        return[]


class ActionSubmitProudForm(Action):
    def name(self) -> Text:
        return "action_proud"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_if_wantsto_chat")
                                                     
        
        return[]


class ActionSubmitBecauseForm(Action):
    def name(self) -> Text:
        return "action_because"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_faith_2")
        dispatcher.utter_message(template="utter_story")
                                                     
        
        return[]


class ActionSubmitPlanForm(Action):
    def name(self) -> Text:
        return "action_plan"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["plan"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        #budget = tracker.get_slot("fun")
        dispatcher.utter_message(template="utter_sounds_plan")
        dispatcher.utter_message(template="utter_conversation")
        #dispatcher.utter_message(template="utter_made_you_feel")
        return []


class ActionSubmitmovieForm(Action):
    def name(self) -> Text:
        return "action_movie"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_after_movie")                                                     
        
        return[]


class ActionSubmitfamilyfriendsForm(Action):
    def name(self) -> Text:
        return "action_familyfriends"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_after_familyorfriends")                                                     
        
        return[]


class ActionSubmitsportsForm(Action):
    def name(self) -> Text:
        return "action_sports"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_after_sports")                                                     
        
        return[]


class ActionSubmitfoodForm(Action):
    def name(self) -> Text:
        return "action_food"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_after_food")                                                     
        
        return[]

class ActionSubmitmusicForm(Action):
    def name(self) -> Text:
        return "action_music"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
        #dispatcher.utter_message(template="utter_after_celebration",
         #                        celebration=tracker.get_slot("celebration"))
        #dispatcher.utter_message(template="utter_way_celebrate")
        dispatcher.utter_message(template="utter_after_music")                                                     
        
        return[]