# Glk
Notre projet est un CMS, Certes le but initial est l'apprentissage, mais il vise a faciliter la création des blogs.

## 3. Stack Technique

- **Framework :** express
- **Hashage des mots de passe:** bcrypt
- **Authentification par token :** jsonwebtoken
- **Gestion des variables d’environnement :** dotenv
- **Autorisation des requêtes depuis le frontend :** cors
- **Client PostgreSQL :** pg

```Arboressence
Glk/
│
├── backend/                # API Express
│   ├── src/
│   │   ├── config/          # Configurations (DB, env)
│   │   │   └── db.js
│   │   ├── models/          # Schémas et requêtes SQL
│   │   │   └── User.js
│   │   │   └── Post.js
│   │   ├── routes/          # Routes Express
│   │   │   └── authRoutes.js
│   │   │   └── postRoutes.js
│   │   ├── controllers/     # Logique métier
│   │   │   └── authController.js
│   │   │   └── postController.js
│   │   ├── middleware/      # Auth, sécurité
│   │   │   └── authMiddleware.js
│   │   ├── utils/           # Fonctions utilitaires
│   │   └── server.js        # Point d’entrée Express
│   ├── package.json
│   └── .env                 # Variables d’environnement
│
├── frontend/               # Interface utilisateur
│   ├── src/
│   │   ├── components/      # Composants React
│   │   ├── pages/           # Pages (Dashboard, Login, etc.)
│   │   ├── services/        # Appels API
│   │   └── App.js
│   ├── package.json
│
├── database/               # Scripts SQL
│   ├── schema.sql          # Création des tables
│   └── seed.sql            # Données de test
│
└── README.md
```