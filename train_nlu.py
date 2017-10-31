from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import six

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.converters import load_data
from rasa_nlu.model import Trainer

if six.PY2:
    model_name = 'current_py2'
else:
    model_name = 'current_py3'

def train_nlu():
    training_data = load_data('nlu/musicplayer.rasa.md')
    trainer = Trainer(RasaNLUConfig("nlu/config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('nlu/model',
                                      fixed_model_name=model_name)
    return model_directory


if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    train_nlu()
