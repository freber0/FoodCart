# FoodCart
FoodCart est un projet dans le cadre du cours GLO-2005 de l'Université Laval. Le but étant de réaliser une application web suivant une architecture à trois niveaux et en utilisant les technologies vues dans le cours (HTML, CSS, JS, Python, Flask et MySQL). Vous trouverez dans ce repo tout le code de notre application. Il s'agit d'un site web de vente de produit d'épicerie gérant un des usagers et des paniers d'achât avec une base de données MySQL sur Docker.
## Contributeurs

 - [Antoine Adam](https://github.com/bidetzz)
 - [Frédéric Bernard](https://github.com/fredericbernard)
 - [Alex Raymond](https://github.com/mcfire02)

## Prérequis
Il s'agit des packages nécessaires pour faire rouler le docker-compose.
 - [docker](https://docs.docker.com/glossary/?term=installation)
 - [docker-compose](https://docs.docker.com/compose/install/)

## Démarrage

```
docker-compose up
```
Cette commande installera les packages requis dans le fichier requirements.txt automatiquement à l'aide du dockerfile. Par la suite, deux docker container seront créer pour l'application et pour la base de données MySQL.

## Accéder à l'application

Dans votre navigateur web, aller sur 
`localhost:8090` pour voir la page de login de notre application.

Un compte par défaut a été créer pour tester l'application:

| Nom d'usager       | Mot de passe 
| ------------- |:-------------:|
| admin     | admin | $1600 |

Vous pouvez également créer votre propre compte en cliquant sur **Enregistrez-vous**!

## Utiliser l'application

### Page d'accueil
Dans la page d'acceuil, vous pouvez "browse" tous les produits qui sont à vendre et rechercher par catégorie de produits en utilisant la barre de navigation de gauche. Il est même possible d'utiliser la barre de recherche pour trouver le produit que vous voulez. Quand vous voulez **ajouter un produit à votre panier**, il suffit de **cliquer sur le petit " +" orange** en dessous de la description du produit.
### Mon panier

Dans cette page, il est possible de voir tout les produits que vous avez ajouté à votre panier. Chaque produit est inscrit avec son prix, sa quantité ainsi que le sous-total de cette partie.
Si vous voulez **supprimer un produit** de votre panier, il suffit de **cliquer sur la petite poubelle rouge**. Lorsque vous êtes prêt à acheter vos produits, cliquez sur *commander*.

### Mon compte

Pour accéder à la page de votre compte, cliquez sur le petit icone dans le coin haut-droit de votre écran. Vous pourrez maintenant changer les informations par rapport à votre compte tel que votre adresse de livraison ou votre email.


# Librairies et framework utilisées

Pour ce projet, nous avons utilisé le framework [materialize](https://materializecss.com/) pour nous aider dans le visuel du site. Nous avons également utilisé des librairies publiques et nous réclamons aucune en être les auteurs.

 #### CSS et Javascript
 - [materialize](https://materializecss.com/)
#### Python
 - [flask](https://pypi.org/project/Flask/)
 - [flask-login](https://flask-login.readthedocs.io/en/latest/)
 - [werkzeug](https://pypi.org/project/Werkzeug/0.14.1/)
 - [flask_wtf](https://pypi.org/project/Flask-WTF/)
 - [wtforms](https://pypi.org/project/WTForms/)
 - [mysql-connector](https://pypi.org/project/mysql-connector/)
