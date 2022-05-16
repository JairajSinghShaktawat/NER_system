### Multi-language Named Entity Recognition system 
### Used Spacy language models 
## Author: Jairaj Singh Shaktawat


import spacy

def NER(text, language_model):
    """
    Function that returns Named Entity recognition for a 
    given text using a given language model
    
    :param: text; string: text to generate entities
    :param: language_model; string: name of language model to load
    :return list: a list of entities where each entity is in dictionary form
    """
  # Load NER
    nlp = spacy.load(language_model)
    doc = nlp(text)
    entities = []
    for entity in doc.ents:
        temp = {}
        temp['text'] = entity.text
        temp['type'] = entity.label_
        temp['start_pos'] = entity.start
        temp['end_pos'] = entity.end

        entities.append(temp)
    return entities

#######################################################
# RUN A TEST SCRIPT                                   #
#######################################################
if __name__ == "__main__":
    # Sample text from Spacy     
    text = ('Apple is looking at buying U.K. startup for $1 billion')
    language_model = "en_core_web_sm"
    
    # Printing list of dictionary
    print(NER(text, language_model))
