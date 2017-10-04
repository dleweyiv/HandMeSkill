# Copyright 2017 David Lewis
# This file is part of the Villanova tour guide mrcroft skill
from os.path import dirname

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'dlew'

LOGGER = getLogger(__name__)

class HandMeSkill(MycroftSkill):
		def __init__(self):
				super(HandMeSkill, self).__init__(name="HandMeSkill")

		def initialize(self):
				hand_me_intent = IntentBuilder("HandMeIntent"). \
						require("HandMeKeyword").build()
				self.register_intent(hand_me_intent, self.handle_hand_me_intent)

		def handle_hand_me_intent(self, message):
				self_speak_dialog("hand.me")

		def stop(self):
				pass

def create_skill():
		return HandMeSkill()