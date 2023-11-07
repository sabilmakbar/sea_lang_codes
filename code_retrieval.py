import json
import babel.languages

from utils import merge_dict_append_values, extract_iso639_names


if __name__ == "__main__":

    with open("json_resources/sea_country_info_alpha2.json", "r") as f:
        alpha2_codes_dict = json.load(f)

    lang_codes = {}
    for country, code_list_info in alpha2_codes_dict.items():
        lang_info = {}
        for code_info in code_list_info:
            _babel_info = babel.languages.get_territory_language_info(code_info["code"])
            for key, val in _babel_info.items():
                _babel_info[key] = extract_iso639_names(key)
            if _babel_info != {}:
                lang_info = merge_dict_append_values(lang_info, _babel_info)
        lang_codes[country] = lang_info

    with open("json_resources/sea_country_langs_babel.json", "w") as f:
        json.dump(lang_codes, f, indent=4)
