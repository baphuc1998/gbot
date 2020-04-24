from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.forms import FormAction
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import SlotSet
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk.events import UserUttered
import geocoder
import spacy

# from util.spacy_ner.space_ner import get_category
from skills.response import ask_time
# from util.constant.commom import MessageTemplate
# from skills.recomemder.suggest_drop_voucher import recommender_voucher
# from skills.recomemder.suggest import recommender
# from util.helpers.helper import CustomResetSlot
# recomm_category = recommender()


class ActionResponseTime(Action):

    def name(self):
        return "action_response_time"

    def run(self, dispatcher, tracker, domain):
        intent = tracker.latest_message.get("intent").get("name")
        if intent == 'it_ask_time':
            mess = ask_time.get_time()
            print(mess)
            dispatcher.utter_message('The time now is ' + mess)
        if intent == 'it_ask_date':
            mess = ask_time.get_date()
            print(mess)
            dispatcher.utter_message('Today is ' + mess)
        return []

