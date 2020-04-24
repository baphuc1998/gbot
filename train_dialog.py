# Imports
# -----------
# rasa core
import logging
import asyncio
from rasa_core import training
from rasa_core.actions import Action
from rasa_core.agent import Agent
from rasa_core.domain import Domain
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies import FallbackPolicy
# from rasa_core.policies import FallbackPolicy, FormPolicy
from rasa_core.policies.form_policy import FormPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.featurizers import MaxHistoryTrackerFeaturizer, BinarySingleStateFeaturizer
from rasa_core.interpreter import RegexInterpreter
from rasa_core.interpreter import RasaNLUInterpreter
from rasa.core.policies.mapping_policy import MappingPolicy

# Function
# ------------


def train_dialog(dialog_training_data_file, domain_file, path_to_model='models/'):
    logging.basicConfig(level='INFO')
    fallback = FallbackPolicy(
        fallback_action_name="utter_default", core_threshold=0.3, nlu_threshold=0.3)

    # agent = Agent(domain_file,
    #           policies=[MemoizationPolicy(max_history=1),KerasPolicy(epochs=200,
    #     batch_size=20), fallback, FormPolicy])
    agent = Agent(domain_file,
                  policies=[MemoizationPolicy(max_history=1), KerasPolicy(epochs=200,
                                                                      batch_size=20), FormPolicy(), fallback])

    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(agent.load_data(dialog_training_data_file))
    # training_data = agent.load_data(dialog_training_data_file)
    agent.train(
        data,
        augmentation_factor=50,
        validation_split=0.2)
    agent.persist(path_to_model)


# Train
# --------
train_dialog('data/stories.md', 'domain.yml')
