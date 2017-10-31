from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import six

from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.converters import load_data
from rasa_nlu.model import Metadata, Interpreter
from rasa_core.training_utils.dsl import *

#StoryFileReader.load_from_file(name,domain)

def test_nlu():
    # create an NLU interpreter based on trained NLU model
    nlu_model_path = 'nlu/model/default/current_py3'
    interpreter = Interpreter.load(nlu_model_path, RasaNLUConfig("nlu/config.json"))

    # load vocab definition to run as tests
    training_data = load_data('nlu/musicplayer.rasa.md')
    #json = training_data.as_json()
    examples = training_data.entity_examples
    for example in examples:
        example_failed = False
        text = example.as_dict()['text']
        intent = example.as_dict()['intent']
        #print (example.as_dict())
        #print ('-------------------------------')
        lookup = interpreter.parse(text)
        #print(lookup)
        if (lookup['intent']['name'] == intent):
            #print ('-------------------------------')
            #print ('INTENT OK')
            #print ('-------------------------------')
            slotsFailed = False
            for slot in example.as_dict()['entities']:
                slotFound = False
                #print("TRY MATCH {}".format(slot))
                for entity in lookup['entities']:
                    #print("AGAINST {}".format(entity))
                    if (entity['entity'] == slot['entity']):
                        #print ('FOUND')
                        slotFound = True
                    else:
                        pass
                        #print('NO MATCH')
                if (not slotFound):
                    slotsFailed = True
                    example_failed = True
                    print ('-------------------------------')
                    print("{} - {}".format(text,intent))
                    print ('-------------------------------')
                    print ('FAIL slots')
                    print ('-------------------------------')
                else:
                    pass
                    #print ('-------------------------------')
                    #print ('OK slots')
                    #print ('-------------------------------')
        else:
            example_failed = True;
            print ('-------------------------------')
            print("{} - {}".format(text,intent))
            print ('-------------------------------')
            print ('-------------------------------')
            print ('FAIL intent')
            print ('-------------------------------')
    #if (example_failed):
        #print ('-------------------------------')
        #print ('FAIL EXAMPLE')
        #print ('-------------------------------')
    #else:
        #print ('-------------------------------')
        #print ('OK EXAMPLE')
        #print ('-------------------------------')
    

if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    test_nlu()
