from iso639 import Lang
from iso639.iso639 import InvalidLanguageValue, DeprecatedLanguageValue

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
    keys = ("name", "iso_identifier", "iso_639_1_code", "iso_639_2_code", "iso_639_3_code")
    _exception_list = (InvalidLanguageValue, DeprecatedLanguageValue)
    try:
        lang_obj = Lang(pt3=lang_code)
        lang_name = lang_obj.name
        lang_iso639_1 = lang_obj.pt1
        lang_iso639_2 = lang_obj.pt2b
        lang_iso639_3 = lang_obj.pt3
        identifier = "ISO 639-3"
    except _exception_list:
        try:
            lang_obj = Lang(pt2b=lang_code)
            lang_name = lang_obj.name
            lang_iso639_1 = lang_obj.pt1
            lang_iso639_2 = lang_obj.pt2b
            lang_iso639_3 = lang_obj.pt3
            identifier = "ISO 639-2"
        except _exception_list:
            try:
                lang_obj = Lang(pt1=lang_code)
                lang_name = lang_obj.name
                lang_iso639_1 = lang_obj.pt1
                lang_iso639_2 = lang_obj.pt2b
                lang_iso639_3 = lang_obj.pt3
                identifier = "ISO 639-1"
            except _exception_list:
                lang_name = "Un-extractable via iso639 lang class!"
                lang_iso639_1 = "Unavailable"
                lang_iso639_2 = "Unavailable"
                lang_iso639_3 = "Unavailable"
                identifier = "Unavailable"

    return dict(zip(keys, (lang_name, identifier, lang_iso639_1, lang_iso639_2, lang_iso639_3)))
