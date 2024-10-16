import smtplib
from email.message import EmailMessage

# Fonction pour envoyer des emails
def send_email(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password):
    # Créer le message email
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)  # Plusieurs destinataires
    
    try:
        # Connexion au serveur SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Sécuriser la connexion
            server.login(login, password)  # Se connecter au compte email
            server.send_message(msg)  # Envoyer l'email
            print(f"Email envoyé avec succès à {', '.join(to_emails)}")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")

# Paramètres de l'email
subject = "Notification importante"
body = "Bonjour, ceci est un email automatique pour vous informer d'une mise à jour importante."
from_email = "votre_email@gmail.com"
to_emails = ["destinataire1@example.com", "destinataire2@example.com", "destinataire3@example.com"]

# Informations SMTP (ici pour Gmail)
smtp_server = "smtp.gmail.com"
smtp_port = 587
login = "votre_email@gmail.com"  # Votre adresse email
password = "votre_mot_de_passe"  # Votre mot de passe d'application ou mot de passe de compte

# Envoi de l'email
send_email(subject, body, from_email, to_emails, smtp_server, smtp_port, login, password)
