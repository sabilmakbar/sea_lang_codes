import json

from utils import extract_iso639_names

if __name__ == "__main__":

    # load manual curated on lang_codes_to_add & lang_codes_to_remove
    with open("json_resources/lang_codes_to_add.json", "r") as f:
        lang_codes_to_add = json.load(f)

    with open("json_resources/lang_codes_to_remove.json", "r") as f:
        lang_codes_to_remove = json.load(f)

    # load babel-extracted lang data
    with open("json_resources/sea_country_langs_babel.json", "r") as f:
        lang_dict_info = json.load(f)

    # add ingestion method in lang-code keys
    for country, lang_data in lang_dict_info.items():
        for lang_code in lang_data.keys():
            lang_dict_info[country][lang_code]["ingestion_method"] = "Py-Babel Retrieval"

    # add ISO 639 infos in lang_codes_to_add data
    for country, lang_data in lang_codes_to_add.items():
        for lang_code in lang_data.keys():
            lang_codes_to_add[country][lang_code] = extract_iso639_names(lang_code)
            lang_codes_to_add[country][lang_code]["ingestion_method"] = "Manual Curation"

    # remove & add data from lang_dict_info data
    for country, lang_data in lang_dict_info.items():
        #remove data
        data_to_remove = lang_codes_to_remove.get(country, list())
        if data_to_remove != []:
            lang_dict_info[country] = {k: v for k, v in lang_dict_info[country].items() if k not in data_to_remove}

        #add data
        data_to_add = lang_codes_to_add.get(country, [])
        if data_to_add != []:
            lang_dict_info[country].update(data_to_add)

    with open("json_resources/sea_country_lang_full_info.json", "w") as f:
        json.dump(lang_dict_info, f, indent=4)

    lang_dict_info_lite = {}
    for country, lang_data in lang_dict_info.items():
        iso_639_1_list = [info["iso_639_1_code"] for info in lang_data.values() if info["iso_639_1_code"] not in ("", "Unavailable")]
        iso_639_2_list = [info["iso_639_2_code"] for info in lang_data.values() if info["iso_639_2_code"] not in ("", "Unavailable")]
        iso_639_3_list = [info["iso_639_2_code"] for info in lang_data.values() if info["iso_639_2_code"] not in ("", "Unavailable")]
        lang_dict_info_lite[country] = dict(zip(("iso_639_1_code", "iso_639_2_code", "iso_639_3_code"), (iso_639_1_list, iso_639_2_list, iso_639_3_list)))

    with open("json_resources/sea_country_lang_list.json", "w") as f:
        json.dump(lang_dict_info_lite, f, indent=4)
