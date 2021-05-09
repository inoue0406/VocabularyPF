# prep for wiktionary data

import json
#import wiktextract

if __name__ == '__main__':

    # Wiktionary dump file
    
    fjson = "../data/Wiktionary/kaikki.org-dictionary-English.json"

    fcsv = open('../data/out_wordlist_Wiktionary.csv', 'w', encoding='utf-8')
    print("word,sound,sense",file=fcsv)
    
    with open(fjson, "r") as f:
        count = 0
        for line in f:
            data = json.loads(line)
            # extract data
            if "word" in data.keys():
                word = data['word']
                print("processing word:",word)
                if "sounds" in data.keys():
                    if "ipa" in data['sounds'][0]:
                        sound = data['sounds'][0]["ipa"]
                    else:
                        sound = "NA"
                else:
                    sound = "NA"
                if "senses" in data.keys():
                    if "glosses" in data['senses'][0]:
                        sense = data['senses'][0]['glosses'][0]
                    else:
                        sense = "NA"
                else:
                    sense = "NA"
                print("%s,%s,%s" % (word,sound,sense),file=fcsv)
                #lst.append(data)
                count = count + 1
                #if count > 100:
                #    import pdb;pdb.set_trace()

    
