# SEA Lang Codes Collection
Mini Repo Containing Lang Codes (ISO 639-1, ISO 639-2, and ISO 639-3) from Countries in Southeast Asia (SEA).

## Goal
The NLP Research & Development activities in SEA is starting to be recognized throughout the world, due to its potential of cultural, linguistic, and economy. However there are no accessible resources for activist or practitioners to obtain relevant information for Lang Codes that are spoken/originated in SEA.
This mini-repo resource is aimed to aid people to quickly check lang codes in SEA region, for the following purposes:
1. Check the lang coverage in SEA and Evaluate its Competency for any models released.
2. Filter and Extract any new datasets released for SEA languages.

The list of langs informations are available on ```json_resources/sea_country_lang_full_info.json```, and its lite version (containing json dict of ```country->lang_list``` only) available on ```json_resources/sea_country_lang_list.json```

The collection itself was constructed using a hybrid approach:
1. The initial collection were retrieved from [```babel py```](https://babel.pocoo.org/en/latest/api/languages.html), using manually constructed SEA Country Info available on ```json_resources/sea_country_info_alpha2.json``` and stored in ```json_resources/sea_country_langs_babel.json```. The lang names were obtained from [```iso639-lang py```](https://pypi.org/project/iso639-lang/) package by decoding its code using ```ISO 639-1```, ```ISO 639-2```, or ```ISO 639-3```.
2. The collection then filtered using manual curation effort w/ codes available in ```json_add_remove_collection.py```. The collection will only consider languages that were originated and/or commonly used by indigenous people/tribes in that Country.
3. Step 1 and Step 2 results are filtered and/or added by using ```code_updater.py```

This code is executed in ```Python 3.11.3```, so it's recommended to use the same version for reproducibility. Any contribution to this collection will be greatly appreciated by creating PR/raising Issue!
