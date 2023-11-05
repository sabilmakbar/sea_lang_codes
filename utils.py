from iso639 import Lang
from iso639.iso639 import InvalidLanguageValue

def merge_dict_append_values(dict_1, dict_2):
    _combined_dict = {}
    for key in (*dict_1.keys(), *dict_2.keys()):
        val_1 = dict_1.get(key)
        val_2 = dict_2.get(key)
        if val_1 is not None and val_2 is not None and val_1!=val_2:
            _combined_dict[key] = [val_1, val_2]
        elif val_1 is not None and val_2 is not None and val_1==val_2:
            _combined_dict[key] = val_1
        elif val_1 is not None:
            _combined_dict[key] = val_1
        elif val_2 is not None:
            _combined_dict[key] = val_2
        else:
            _combined_dict[key] = None
    
    return _combined_dict


def extract_iso639_names(lang_code: str):
    try:
        _lang_name = Lang(pt3=lang_code).name
        _identifier = "ISO 639-3"
    except InvalidLanguageValue:
        try:
            _lang_name = Lang(pt2=lang_code).name
            _identifier = "ISO 639-2"
        except InvalidLanguageValue:
            try:
                _lang_name = Lang(pt1=lang_code).name
                _identifier = "ISO 639-1"
            except InvalidLanguageValue:
                _lang_name = "Un-extractable via iso639 lang class!"
                _identifier = "Unavailable"

    return _lang_name, _identifier