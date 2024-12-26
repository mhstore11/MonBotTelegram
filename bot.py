import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Insérer ton token ici (ATTENTION : change-le après le test)
TOKEN = "8084312333:AAGCasCp9a-3r38yZULb9pwbUhJpQnQtxk4"

# Fonction pour démarrer le bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Salut ! Envoie-moi un lien de produit, et je vais chercher le prix le moins cher avec mon lien affilié. 😊")

# Fonction pour traiter les liens envoyés par les utilisateurs
def process_link(update: Update, context: CallbackContext):
    message = update.message.text
    if "aliexpress.com" in message:
        update.message.reply_text("Lien reçu, je recherche le meilleur prix...")

        # Logique pour trouver le produit le moins cher (à développer)
        # Ici, on fait un exemple simple avec un faux prix
        cheapest_price = "10.99$"  # Exemple d’un prix fictif
        affiliate_link = f"{message}?aff_link=test_affiliate"  # Ajouter ton lien affilié
        
        response = f"Produit trouvé ! 🎉\nPrix : {cheapest_price}\nLien affilié : {affiliate_link}"
        update.message.reply_text(response)
    else:
        update.message.reply_text("Ce n'est pas un lien AliExpress valide. Essaie encore !")

# Fonction principale
def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Commande /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Gestion des messages (liens)
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, process_link))

    # Lancer le bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
