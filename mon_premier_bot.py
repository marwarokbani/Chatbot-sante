def repondre(question):
    question = question.lower()
    
    if "stress" in question:
        return "La respiration profonde (4-7-8) peut aider : inspirez 4s, retenez 7s, expirez 8s."
    
    elif "sommeil" in question:
        return "Essayez de dormir 7 a 8 heures et evitez les ecrans 1h avant le coucher."
    
    else:
        return "Je ne connais pas encore cette question. Pouvez-vous reformuler ?"

ma_question = "Comment reduire le stress ?"
reponse = repondre(ma_question)
print("Vous :", ma_question)
print("Bot :", reponse)