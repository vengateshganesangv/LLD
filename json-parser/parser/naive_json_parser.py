from data.json import JSON
from data.string_constants import StringConstants
from parser.json_parser import JsonParser


class NaiveJsonParser(JsonParser):
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
    def parse(self, json_text):
        if json_text is None:
            raise RuntimeError("Invalid jsonText")
        
        if StringConstants.STARTING_PARAN_STRING not in json_text:
            json_text = json_text.strip().replace(StringConstants.DOUBLE_QUOTES_STRING, 
                                                StringConstants.EMPTY_STRING)
            key_to_values = {}
            key_to_values[json_text] = None
            return JSON(key_to_values)

        key_value_pairs = self.tokenizer.tokenize(json_text)
        key_to_values = {}
        for key_value_pair in key_value_pairs:
            key_to_values[key_value_pair.get_key()] = self.parse(key_value_pair.get_val())
        
        return JSON(key_to_values)

    def to_string(self, json):
        if json.is_leaf():
            return (StringConstants.DOUBLE_QUOTES_STRING + 
                   json.get_all_keys()[0].strip() + 
                   StringConstants.DOUBLE_QUOTES_STRING)

        json_text = StringConstants.STARTING_PARAN_STRING
        keys = json.get_all_keys()
        
        for key in keys:
            json_text += StringConstants.DOUBLE_QUOTES + key + StringConstants.DOUBLE_QUOTES
            json_text += StringConstants.COLON
            json_text += self.to_string(json.get(key))
            json_text += StringConstants.COMMA

        if json_text.endswith(StringConstants.COMMA_STRING):
            json_text = json_text[:-1]
            
        json_text += StringConstants.CLOSING_PARAN_STRING
        return json_text

