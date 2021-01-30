import csv

def getKey(item):
    return item[1]

command_data = []

with open("command_data.csv", "r", encoding="utf8") as csvfile:
     spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')

     for row in spamreader:
        command_data.append(row)

print(command_data[3])
'''
['python3.4 submit_assignment.py -submit gowithflow.py', 'tiana']
'''

command_counter = {}

for data in command_data:
    if data[1] in command_counter.keys():
        command_counter[data[1]] += 1
    else:
        command_counter[data[1]] = 1

dictlist = []

for key, value in command_counter.items():
    temp = [key,value]
    dictlist.append(temp)

sorted_dict= sorted(dictlist, key=getKey, reverse=True)
print (sorted_dict[:100])
'''
[['bookworm', 8500], ['elsa', 7500], ['fillmore', 7394], ['francis', 5978], ['anton_ego', 5819], ['queen_grimhilde', 5000], ['kristoff', 4934], ['brent_mustangburger', 4838], ['emperor_zurg', 4470], ['tarzan', 4193], ['stitch', 3742], ['marlon_the_alligator', 3203], ['faline', 3115], ['meg', 3098], ['fear', 2968], ['roo', 2782], ['claire_wheeler', 2777], ['don_carlton', 2773], ['guido', 2541], ['flynn_rider', 1996], ['mama_odie', 1883], ['darla_sherman', 1861], ['tiger_lily', 1846], ['chick_hicks', 1678], ['louis_the_alligator', 1374], ['the_dodo', 1364], ['ray_the_firefly', 998], ['tigger', 884], ['jane_porter', 852], ['al_mcwhiggin', 777], ['tinker_bell', 696], ['peter_pig', 500], ['rocket_raccoon', 473], ['charlotte_la_bouff', 472], ['peter_pan', 463], ['auto', 458], ['kocoum', 438], ['prince_naveen', 425], ['flik', 424], ['dory', 410], ['bo_peep', 407], ['captain_hook', 403], ['aladdin', 402], ['chatter_telephone', 372], ['django', 371], ['charlie', 363], ['bomb_voyage', 337], ['riley_anderson', 330], ['flo', 324], ['finn_mcmissile', 319], ['nani_pelekai', 319], ['pocahontas', 312], ['chum', 311], ['bing_bong', 311], ['disgust', 305], ['anna', 304], ['boo', 304], ['fa_zhou', 299], ['francesco_bernoulli', 292], ['bambi', 275], ['prince_hans', 275], ['aurora', 267], ['duke_of_weselton', 264], ['bumblebee', 260], ['joy', 258], ['dolly', 254], ['flora', 247], ['fred', 244], ['brock_pearson', 242], ['dim', 240], ['eve', 239], ['white_rabbit', 237], ['mungo', 237], ['crush', 231], ['pascal', 224], ['carrie_williams', 223], ['rapunzel', 219], ['merryweather', 219], ['wendy_darling', 218], ['roger_rabbit', 211], ['collette_tatou', 206], ['cheshire_cat', 200], ['eudora', 191], ['lilo_pelekai', 190], ['mulan', 188], ['coral', 186], ['maximus', 172], ['emile', 168], ['tiana', 167], ['auguste_gusteau', 153], ['darrell_cartrip', 146], ['sadness', 133], ['nakoma', 133], ['chunk', 126], ['alice', 123], ['the_magic_mirror', 116], ['snow_white', 115], ['splunk_teamlab', 115], ['thor', 98], ['fritz', 94]]
'''
