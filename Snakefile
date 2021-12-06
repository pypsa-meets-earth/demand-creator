# SPDX-FileCopyrightText: : 2021 The PyPSA-Africa Authors
#
# SPDX-License-Identifier: MIT

from os.path import normpath, exists, isdir
from shutil import copyfile
from snakemake.remote.HTTP import RemoteProvider as HTTPRemoteProvider
HTTP = HTTPRemoteProvider()

configfile: "config.yaml"

wildcard_constraints:
    simpl="[a-zA-Z0-9]*|all",
    clusters="[0-9]+m?|all",
    ll="(v|c)([0-9\.]+|opt|all)|all",
    opts="[-+a-zA-Z0-9\.]*",


#################################
########### RULES ###############
#################################


if config['cat-options'].get('salt-bae')==True:
    rule salt_bae_extractor:
        output:
            picture=expand("results/salt-bae{number}.png", **config["wildcard"])
        script: "scripts/salt-bae-extractor.py"


if config['cat-options'].get('fat-cat')==True:
    rule fat_cat_extractor:
        output:
            name="results/fat-cat007.png"
        script: "scripts/fat-cat-extractor.py"
    
    
rule png2pdf:
    input:
        picture="results/salt-bae{number}.png"
    output:
        catpdf="results/salt-bae{number}.pdf"
    script: "scripts/png2pdf.py"

