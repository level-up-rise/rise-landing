# INELLI — site vitrine

Site de présentation pour **Kevin Villarroya-Palau / INELLI** :

- activité de développeur
- produit **RISE Hunter**
- coordonnées
- mentions légales (SIREN `944 601 327`)

## Local

Ouvrir `index.html` dans un navigateur, ou :

```bash
docker build -t inelli-site .
docker run --rm -p 8080:80 inelli-site
```

Puis http://localhost:8080

## CI / CD

Le `Jenkinsfile` build & push l’image Docker Hub `villaroyakevin/inelli-site:latest` sur les branches `main` / `master` (agent Kaniko, credentials `dockerhub-creds`).

## Play Store

Remplacer le bouton « Lien Play Store à venir » dans `index.html` (`#store-link`) quand l’URL sera disponible.
