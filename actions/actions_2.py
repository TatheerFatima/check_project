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
        dispatcher.utter_message(template="utter_talk_about_it")
        return []



class ActionSubmitFineReason2Form(Action):
    def name(self) -> Text:
        return "action_fine_reason_2"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["fine_reason_2"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("fine_reason_2")
        #dispatcher.utter_message(template="utter_you_entered")
        dispatcher.utter_message(template="utter_talk_about_it")
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
        #dispatcher.utter_message(template="utter_made_feel")
        return []

class ActionSubmitfeelform(Action):
    def name(self) -> Text:
        return "action_feel"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("feel")
        dispatcher.utter_message(template="utter_why_happened")
        #dispatcher.utter_message(template="utter_made_feel")
        return []

class ActionSubmitdifferentform(Action):
    def name(self) -> Text:
        return "action_different"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["different"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("different")
        #dispatcher.utter_message(template="utter_felt_sorry_affirm")
        #dispatcher.utter_message(template="utter_learn_move_on")

        #dispatcher.utter_message(template="utter_made_feel")
        return []


class ActionSubmitgoingtodoform(Action):
    def name(self) -> Text:
        return "action_going_to_do"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["going_to_do"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("going_to_do")
        dispatcher.utter_message(template="utter_sadness_temporary")
        dispatcher.utter_message(template="utter_conversational_chat")
        return []


class ActionSubmitwhathappenedform(Action):
    def name(self) -> Text:
        return "action_what_happened"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["what_happened"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("what_happened")
        #dispatcher.utter_message(template="utter_felt_sorry_deny")
        #dispatcher.utter_message(template="utter_whats_next")
        return []


class ActionSubmittodonowform(Action):
    def name(self) -> Text:
        return "action_to_do_now"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["to_do_now"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("to_do_now")
        #dispatcher.utter_message(template="utter_feel_better")
        #dispatcher.utter_message(template="utter_best_option")
        return []


class ActionSubmitbestoptionform(Action):
    def name(self) -> Text:
        return "action_best_option"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["best_option"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("best_option")
        dispatcher.utter_message(template="utter_sadness_temporary")
        dispatcher.utter_message(template="utter_conversational_chat")
        return []

class ActionSubmittheytellyouform(Action):
    def name(self) -> Text:
        return "action_they_tell_you"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["they_tell_you"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("they_tell_you")
        #dispatcher.utter_message(template="utter_sadness_temporary")
        #dispatcher.utter_message(template="utter_conversational_chat")
        return []

class ActionSubmitfeelaboutthatform(Action):
    def name(self) -> Text:
        return "action_feel_about_that"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feel_about_that"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("feel_about_that")
        #dispatcher.utter_message(template="utter_sadness_temporary")
        #dispatcher.utter_message(template="utter_conversational_chat")
        return []

class ActionSubmittellstoryform(Action):
    def name(self) -> Text:
        return "action_tell_story"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["tell_story"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("tell_story")
        dispatcher.utter_message(template="utter_story_mean")
        #dispatcher.utter_message(template="utter_conversational_chat")
        return []


class ActionSubmitSomeoneForm(Action):
    def name(self) -> Text:
        return "action_someone"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["someone"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        #budget = tracker.get_slot("fun")
        dispatcher.utter_message(template="utter_why_happened")
        #dispatcher.utter_message(template="utter_conversation")
        #dispatcher.utter_message(template="utter_made_you_feel")
        return []


class ActionSubmitBecauseForm(Action):
    def name(self) -> Text:
        return "action_because"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["because"]

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Once we have all the information, attempt to add it to the
        Google Drive database"""


        budget = tracker.get_slot("because")
        #dispatcher.utter_message(template="utter_why_happened")
        #dispatcher.utter_message(template="utter_conversation")
        #dispatcher.utter_message(template="utter_made_you_feel")
        return []


