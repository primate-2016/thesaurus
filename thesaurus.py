import json
import logging
from difflib import get_close_matches

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def get_definition(word: str) -> str:
    data = json.load(open('data.json'))
    # try:
    #     output = 'Your definition is: {}'.format(data[word.lower()])
    #     return output

    # except KeyError:

    #     logger.warning(f'Your word: "{word}" is not in the dictionary, checking for similar words')

    #     # returns an ordered list of words that are similar - the first being the most similar
    #     output = get_close_matches(word, data.keys())
    #     if output:
    #         check_again = input('Did you mean "{}"? y/n: '.format(output[0]))
    #         if check_again.lower() == 'y':
    #             return get_definition(output[0])
    #         else:
    #             return 'OK, not checking definitions again, please enter something else'
    #     else:
    #         return 'Could not find any similar words, please enter something else'

    word = word.lower()
    if word in data.keys():
        return data[word]
    # the dataset contains proper nouns capitlised e.g. 'Paris' so 'paris' would fail to match
    elif word.capitalize() in data.keys():
        return data[word.capitalize()]
    # cover things like nato to NATO
    elif word.upper() in data.keys():
        return data[word.upper()]
    else:
        logger.warning(f'Your word: "{word}" is not in the dictionary, checking for similar words')

        # returns an ordered list of words that are similar - the first being the most similar
        output = get_close_matches(word, data.keys())
        if output:
            check_again = input('Did you mean "{}"? y/n: '.format(output[0]))
            if check_again.lower() == 'y':
                return get_definition(output[0])
            else:
                return 'OK, not checking definitions again, please enter something else'
        else:
            return 'Could not find any similar words, please enter something else'


word = input('Enter a word: ')
definition = get_definition(word)
logger.info(definition)
