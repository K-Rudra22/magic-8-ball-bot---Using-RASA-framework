# actions.py
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionMagic8Ball(Action):

    def name(self) -> str:
        return "action_magic_8ball"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):

        responses = [
            "Yes, definitely!",
            "No way!",
            "Ask again later.",
            "It is certain.",
            "Better not tell you now.",
            "My sources say no.",
            "Outlook good.",
            "Very doubtful.",
            "You may rely on it.",
            "Signs point to yes."
        ]

        answer = random.choice(responses)
        dispatcher.utter_message(text=answer)
        return []
