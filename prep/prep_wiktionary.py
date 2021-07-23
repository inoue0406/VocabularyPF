# prep for wiktionary data

import json
import pandas as pd
#import wiktextract

def extract_pronunciation(sounds):
    # Extract American Pronunciation
    #list_country = ["General American","Received Pronunciation","US","UK"]
    ipa = ""
    for i in range(len(sounds)):
        if "ipa" in sounds[i].keys():
        #if "tags" in sounds[i].keys() and "ipa" in sounds[i].keys():
            #if sounds[i]['tags'][0] in list_country:
            ipa = ipa + sounds[i]['ipa']
    return ipa

if __name__ == '__main__':

    # Inputs
    
    # 1: Wiktionary dump file
    fjson = "../data/Wiktionary/kaikki.org-dictionary-English.json"
    
    # 2: word list (NGSL)
    df_words = pd.read_csv('../data/NGSL_Word_Freq_list.csv')

    # Outputs
    fcsv = open('../data/out_wordlist_NGSL_Wiktionary.csv', 'w', encoding='utf-8')

    print("word,sound,sense",file=fcsv)
    
    with open(fjson, "r") as f:
        count = 0
        for line in f:
            data = json.loads(line)
            # extract data
            if "word" in data.keys():
                word = data['word']
                
                if word == "pyre":
                    #import pdb;pdb.set_trace()
                    pass
                
                # if contained in NGSL list
                if sum(df_words["Lemma"] == word)==0:
                    print(word,"not contained in NGSL. Skip.")
                    continue
                
                print("processing word:",word)
                if "sounds" in data.keys():
                    sound =extract_pronunciation(data["sounds"])
                else:
                    sound = ""
                if "senses" in data.keys():
                    if "glosses" in data['senses'][0]:
                        sense = data['senses'][0]['glosses'][0]
                    else:
                        sense = "NA"
                else:
                    sense = "NA"
                #import pdb;pdb.set_trace()
                print("%s,%s,'%s'" % (word,sound,sense),file=fcsv)
                #lst.append(data)
                count = count + 1
                #if count > 100:


    
