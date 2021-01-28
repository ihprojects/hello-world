from datetime import date    # fuer den Zeitstempel
from operator import itemgetter

# Definition einer Vokabel
# Ein Test besteht aud den folgenden Wörte 
word_1 ={
    'english_word':'chair',          # Der zu übersetzende englische Begriff
    'german_choose_word':['Tisch','Stuhl','Sessel'],    # Liste der möglichen Antworten
    'answer_index':1,               # Nummer der richtigen Antwort in Listenelement
    'is_learned':False,          # Wurde richtig geantwortet TRUE / FALSE
    'trained_at':date(2021,1,26),  # Wann abgefragt
    }

word_2 ={
    'english_word':'window',          
    'german_choose_word':['Fenster','Tuer','Treppe'],
    'answer_index':0,               
    'is_learned':False,          
    'trained_at':date(2021,1,26),               
    }

word_3 ={
    'english_word':'fridge',          
    'german_choose_word':['Staubsauger','Spuelmaschine','Kuehlschrank'],
    'answer_index':2,               
    'is_learned':False,          
    'trained_at':date(2021,1,26),              
    }

word_old ={
    'english_word':'bed',          # Der zu übersetzende englische Begriff
    'german_choose_word':['Bett','Stuhl','Sessel'],    # Liste der möglichen Antworten
    'answer_index':1,               # Nummer der richtigen Antwort in Listenelement
    'is_learned':False,          # Wurde richtig geantwortet TRUE / FALSE
    'trained_at':date(2021,1,25),  # Wann abgefragt
    }

msg_answer = {"True" : "richtig",
    "False" : "falsch"}

msg_is_singular = {"True" : "ist",
    "False" : "sind"}

# Das ist mein Vokabulary zu lernen
vokabulary = [word_1, word_2, word_3]     # Eine Liste aus mehreren Dictionaries 

# Hier werden die antworten noch vorgegeben, da wir noch kein 'User-Input' kennen
answers = [1, 2, 3]
#answers = [2, 1, 3] # alle ok

# Anzahl von Antworten ist gleich wie die Anzahl von Worten
# Vokabelabfrage
# Prüfen die Antworten und ablegen in test_results
test_results = {}
for i in range(len(vokabulary)): 
    word = vokabulary[i]
    print(f"\n\nWie lautet das deutsche Wort für {word['english_word']}?")        # Die Frage wird ausgegeben

    # Listen möglichen Antworten
    print("Antwortmoeglichkeiten:")
    print(f"\t1. {word['german_choose_word'][0]}")
    print(f"\t2. {word['german_choose_word'][1]}")
    print(f"\t3. {word['german_choose_word'][2]}")

    print(f"Deine Antwort war: {answers[i]}.")

    print(f"Richtig ist: {word['answer_index'] + 1}. {word['german_choose_word'][word['answer_index']]}") # !? I'd never use that in practise

    answer_is_correct = (answers[i] - 1) == word['answer_index'] # True - für richtig, False - für falsch
    print(f"Du hast {msg_answer[str(answer_is_correct)]} geantwortet!")
    test_results[word['english_word']] = answer_is_correct
    # lass uns das nächste Wort prüfen

print(f"\nDas ist Test Ergebnis:")
print(test_results)

# Markieren, welche Wörte schon gelernt sind
# Und vieweil richtig
number_correct_answer = 0
for w, r in test_results.items():
    if r == True:
        number_correct_answer += 1
    for word in vokabulary:
        if word['english_word'] == w:
            word['is_learnt'] = r#
            word['trained_at'] = date.today()
             
print(f"{number_correct_answer} {msg_is_singular[str(number_correct_answer <= 1)]} richtig geantwortet!")

#print(sorted(vokabulary, key = lambda v: (v['is_learnt'], v['trained_at']), reverse=True))

#print(sorted(vokabulary, key=itemgetter('is_learnt', 'trained_at'), reverse=True))
print(vokabulary)


#vokabulary.append(word_old)
#print(sorted([word_1['trained_at'], word_2['trained_at'], word_3['trained_at']])
# vocabulary = [word_1['trained_at'], word_2['trained_at'], word_3['trained_at']] vocabulary.sort()

# Ausbaustufen:
# Sortieren der richtigen Antworten nach Timestamp absteigend, damit die ältesten als erste wiederholt werden: 

# Sortieren der falschen Antworten nach Timestamp absteigend, damit die ältesten als erste wiederholt werden: 
 # Auswertung - Anzahl von richtig, Anzahl von falsch 
# Gruppenweise Sortierung (falsch, richtig), damit sowohl bereits richtige und falsche abgefragt werden können
# Wir brauchen keine Timestamp  
