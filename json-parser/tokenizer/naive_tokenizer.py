from data.key_value_pair import KeyValuePair
from data.string_constants import StringConstants
from tokenizer.tokenizer import Tokenizer


class NaiveTokenizer(Tokenizer):
    def tokenize(self, text):
        text = self._pre_process(text)
        start_idx = 0
        key_val_pairs = []
        
        while len(text) > 0:
            end_idx = self._get_end_index(text)
            key_val_pairs.append(text[start_idx:end_idx])
            if end_idx >= len(text):
                break
            text = text[end_idx + 1:]

        key_val_tokens = []
        for key_val_pair in key_val_pairs:
            idx = key_val_pair.find(StringConstants.COLON)
            key = key_val_pair[:idx].strip().replace(
                StringConstants.DOUBLE_QUOTES_STRING, 
                StringConstants.EMPTY_STRING
            )
            val = key_val_pair[idx + 1:]
            key_val_tokens.append(KeyValuePair(key, val))

        return key_val_tokens

    def _get_end_index(self, text):
        idx = text.find(StringConstants.COLON)
        end_idx = idx + 1
        
        while text[end_idx] == StringConstants.WHITE_SPACE:
            end_idx += 1

        if text[end_idx] == StringConstants.DOUBLE_QUOTES:
            end_idx += 1
            while len(text) > end_idx and text[end_idx] != StringConstants.DOUBLE_QUOTES:
                end_idx += 1
            end_idx += 1
        elif text[end_idx] == StringConstants.STARTING_PARAN:
            cnt = 1
            end_idx += 1
            while cnt != 0 and len(text) > end_idx:
                if text[end_idx] == StringConstants.CLOSING_PARAN:
                    cnt -= 1
                elif text[end_idx] == StringConstants.STARTING_PARAN:
                    cnt += 1
                end_idx += 1
        else:
            raise RuntimeError("Illegal json")

        while end_idx < len(text) and text[end_idx] != StringConstants.COMMA:
            end_idx += 1

        return end_idx

    def _pre_process(self, text):
        try:
            text = text.strip()
            text = text[1:-1]
            text = text.strip()
        except Exception:
            raise RuntimeError("Invalid text")
        return text