import json

if __name__ == "__main__":
    list_of_macrolangs_in_sea = {
    #curated from here: https://en.wikipedia.org/wiki/ISO_639_macrolanguage
        "Bikol": {"code": "bik", "country": ["Philippines"], "alt_names": ["Bicolano"]},
        "Bontok": {"code": "bnc", "country": ["Philippines"], "alt_names": ["Bontoc", "Finallig"]},
        "Hmong": {"code": "hmn", "country": ["Laos", "Myanmar", "Vietnam", "Thailand"], "alt_names": []},
        "Malay": {"code": "msa", "country": ["Laos", "Myanmar", "Vietnam", "Thailand"], "alt_names": []},
    }

    json_lang_to_add = {
        "Indonesia": {
            "bhp": {"article_in_wiki": True},
            "abs": {"macrolang": "msa", "article_in_wiki": True},
            "mui": {"macrolang": "msa", "article_in_wiki": True},
            "btk": {"article_in_wiki": True},
            "jax": {"macrolang": "msa", "article_in_wiki": True},
            "xmm": {"macrolang": "msa", "article_in_wiki": True},
            "mqg": {"macrolang": "msa", "article_in_wiki": False},
            "mkn": {"macrolang": "msa", "article_in_wiki": False},
            "mfp": {"macrolang": "msa", "article_in_wiki": False},
            "goq": {"macrolang": "msa", "article_in_wiki": False},
            "pea": {"macrolang": "msa", "article_in_wiki": False},
            "mhp": {"macrolang": "msa", "article_in_wiki": False},
            "mfb": {"macrolang": "msa", "article_in_wiki": True},
            "btj": {"macrolang": "msa", "article_in_wiki": True},
            "bve": {"macrolang": "msa", "article_in_wiki": True},
            "liw": {"macrolang": "msa", "article_in_wiki": True},
            "hji": {"macrolang": "msa", "article_in_wiki": True},
            "vkk": {"macrolang": "msa", "article_in_wiki": True},
        },
        "Malaysia": {
            "mfa": {"macrolang": "msa", "article_in_wiki": True},
            "meo": {"macrolang": "msa", "article_in_wiki": True},
            "zlm": {"macrolang": "msa", "article_in_wiki": False},
            "zsm": {"macrolang": "msa", "article_in_wiki": True},
            "mbf": {"macrolang": "msa", "article_in_wiki": True},
            "ccm": {"macrolang": "msa", "article_in_wiki": True},
            "coa": {"macrolang": "msa", "article_in_wiki": True},
        },
        "Brunei": {
            "kxd": {"macrolang": "msa", "article_in_wiki": True},
        },
        "Philippines": {
            "bcl": {"macrolang": "bik", "article_in_wiki": True},
            "bln": {"macrolang": "bik", "article_in_wiki": True},
            "cts": {"macrolang": "bik", "article_in_wiki": True},
            "lbl": {"macrolang": "bik", "article_in_wiki": False},
            "rbl": {"macrolang": "bik", "article_in_wiki": False},
            "ubl": {"macrolang": "bik", "article_in_wiki": True},
            "ebk": {"macrolang": "bnc", "article_in_wiki": True},
            "lbk": {"macrolang": "bnc", "article_in_wiki": True},
            "obk": {"macrolang": "bnc", "article_in_wiki": False},
            "rbk": {"macrolang": "bnc", "article_in_wiki": True},
            "vbk": {"macrolang": "bnc", "article_in_wiki": True}
        },
        "Vietnam": {
            "hmf": {"macrolang": "hmn", "article_in_wiki": False},
            "hmv": {"macrolang": "hmn", "article_in_wiki": False},
        },
        "Laos": {
            "hnj": {"macrolang": "hmn", "article_in_wiki": False},
            "mww": {"macrolang": "hmn", "article_in_wiki": False},
        }
    }

    json_lang_to_remove = {
        "Indonesia": [
            "ms_Arab",
            "zh_Hant"
            ],
        "Singapore": [
            "pa"
        ],
        "Malaysia": [],
        "Laos": [],
        "Timor-Leste": [],
        "Cambodia": [],
        "Thailand": ["zh_Hant"],
        "Myanmar": [],
        "Brunei": [
            "zh_Hant",
            "ms_Arab"],
        "Vietnam": [
            "zh_Hant",
            "ms_Arab"],
        "Philippines": ["zh_Hant"],
    }

    with open("json_resources/sea_listed_macrolangs.json", "w") as f:
        json.dump(list_of_macrolangs_in_sea, f, indent=4)

    with open("json_resources/lang_codes_to_add.json", "w") as f:
        json.dump(json_lang_to_add, f, indent=4)

    with open("json_resources/lang_codes_to_remove.json", "w") as f:
            json.dump(json_lang_to_remove, f, indent=4)
