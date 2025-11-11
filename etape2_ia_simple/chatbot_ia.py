from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

phrases = [
    "Je suis stressee" , "Trop de pression " , "Je me sens anxieuse", "J'ai peur ", "Je dors mal ", "Insomie"," Probleme d'endordissement", "Je suis fatiguee le matin ","Que manger ?", "Alimentation saine ","Mieux manger","Je grignote beaucoup"
]

intentions= [
    "stress","stress","stress","stress",
    "sommeil","sommeil","sommeil","sommeil",
    "alimentation","alimentation","alimentation","alimentation"
]

vectorizer = CountVectorizer() # transformer les mots en choiffres
modele = MultinomialNB () #apprendre les liens entre mots et intentions

# phrases -> nombres : une matrice
x=vectorizer.fit_transform (phrases)
y=intentions

modele.fit(x,y)

nouvelle_phrase="J'ai du mal a me detendre le soir"

x_new=vectorizer.transform([nouvelle_phrase])

intention_predite= modele.predict(x_new)[0]

reponses ={
    "stress":"Respiration 4-7-8 : inspirez 4s, retenez 7s, expirez8s. Repetez 3x ",
    "sommeil" : "Evitez les ecrans 1h avant le coucher. Tisane + lecture legere ",
    "alimentation" : "Privilegez fruits, legumes, eau.Evitez le sucre ajoutee"
}

print ("Vous : ", nouvelle_phrase)
print ("IA detecte : ", intention_predite)
print ("Bot : ",reponses[intention_predite])

