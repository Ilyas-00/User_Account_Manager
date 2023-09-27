import random
import string
import hashlib
    

# Liste pour stocker les comptes utilisateur et admin
users = []
admins = []

class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = first_name.lower() + "." + last_name.lower()
        self.password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(8))
        self.password_hash = hashlib.sha256(self.password.encode('utf-8')).hexdigest()


class Admin(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(10))
        self.password_hash = hashlib.sha256(self.password.encode('utf-8')).hexdigest()

# Fonction pour ajouter un nouveau compte
def add_user():
    print("Choisissez le type de compte : ")
    print("1. Utilisateur")
    print("2. Administrateur")
    account_type = int(input("Entrez votre choix : "))
    first_name = input("Entrez votre prénom : ")
    last_name = input("Entrez votre nom de famille : ")

    if account_type == 1:
        user = User(first_name, last_name)
        users.append(user)
        print("Votre login est :", user.login)
        print("Votre mot de passe est :", user.password)
    elif account_type == 2:
        admin = Admin(first_name, last_name)
        admins.append(admin)
        print("Votre login est :", admin.login)
        print("Votre mot de passe est :", admin.password)
    else:
        print("Choix invalide. Veuillez réessayer.")

# Fonction pour connecter un utilisateur ou un admin
def login():
    print("Entrez vos informations de connexion : ")
    login = input("Login : ")
    password = input("Mot de passe : ")
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

    for admin in admins:
        if admin.login == login and admin.password_hash == password_hash:
            print("Connexion réussie en tant qu'administrateur.")
            admin_menu(admin)
            return
    for user in users:
        if user.login == login and user.password_hash == password_hash:
            print("Connexion réussie en tant qu'utilisateur.")
            user_menu(user)
            return

    print("Informations de connexion incorrectes. Veuillez réessayer.")

# *****************************************************ADMIN FONCTIONS
# Fonction pour modifier le mot de passe 

def change_password(admin):
    new_password = input("Entrez votre nouveau mot de passe : ")
    admin.password = new_password
    admin.password_hash = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
    print("Votre mot de passe a été modifié avec succès.")

# Fonction pour supprimer un compte utilisateur ou admin
def delete_account(admin):
    login = input("Entrez le login du compte à supprimer : ")

    for user in users:
        if user.login == login:
            users.remove(user)
            print("Compte utilisateur supprimé avec succès.")
            return
    for admin in admins:
        if admin.login == login:
            admins.remove(admin)
            print("Compte administrateur supprimé avec succès.")
            return
    print("Compte inexistant. Veuillez réessayer.")

# Fonction pour afficher les informations d'un compte utilisateur ou admin

def account_info(admin):
    print("Nom d'utilisateur :", admin.login)
    print("Mot de passe :", admin.password)
    print("Nom :", admin.first_name, admin.last_name)


# Fonction pour rechercher des utilisateurs
def search_users(admin):
    keyword = input("Entrez un mot clé : ")
    print(users, admins)
    print("Résultats de la recherche : ")
    return


   

# Fonction pour afficher le menu de l'administrateur
def admin_menu(admin):
    while True:
        print("Menu de l'administrateur : ")
        print("1. Modifier le mot de passe")
        print("2. Supprimer le compte")
        print("3. Consulter les informations du compte")
        print("4. Rechercher des utilisateurs")
        print("5. Quitter le menu")
        choice = int(input("Entrez votre choix : "))
        if choice == 1:
            change_password(admin)
        elif choice == 2:
            delete_account(admin)
        elif choice == 3:
            account_info(admin)
        elif choice == 4:
            search_users(admin)
        elif choice == 5:
            return
        else:
            print("Choix invalide. Veuillez réessayer.")


# *****************************************************USER FONCTIONS
def change_password(user):
    new_password = input("Entrez votre nouveau mot de passe : ")
    user.password = new_password
    user.password_hash = hashlib.sha256(new_password.encode('utf-8')).hexdigest()
    print("Votre mot de passe a été modifié avec succès.")

def delete_account(user):
    users.remove(user)
    print("Votre compte a été supprimé avec succès.")

def view_account_info(user):
    print("Nom d'utilisateur :", user.login)
    print("Mot de passe :", user.password)
    print("Nom :", user.first_name, user.last_name)

def view_shared_documents(user):
    print("Fonctionnalité à implémenter.")

# Fonction pour afficher le menu de l'utilisateur
def user_menu(user):
    while True:
        print("Menu de l'utilisateur : ")
        print("1. Modifier le mot de passe")
        print("2. Supprimer le compte")
        print("3. Consulter les informations du compte")
        print("4. Consulter les documents partagés avec vous")
        print("5. Quitter le menu")
        choice = int(input("Entrez votre choix : "))
        if choice == 1:
            change_password(user)
        elif choice == 2:
            delete_account(user)
            break
        elif choice == 3:
            view_account_info(user)
        elif choice == 4:
            view_shared_documents(user)
        elif choice == 5:
            break
        else:
            print("Choix invalide. Veuillez réessayer.")



def main():
    while True:
        print("Menu principal : ")
        print("1. S'inscrire")
        print("2. Se connecter")
        print("3. Quitter")
        choice = int(input("Entrez votre choix : "))
        if choice == 1:
            add_user()
        elif choice == 2:
            login()
        elif choice == 3:
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
