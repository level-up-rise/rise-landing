# RISE Hunter — landing

Site public de **RISE Hunter** (organisation [`level-up-rise`](https://github.com/level-up-rise)) :

- présentation de l’application
- infos éditeur / développeur (Google Play)
- contact, confidentialité, mentions légales (SIREN `944 601 327`)

## Local

```bash
docker build -t rise-landing .
docker run --rm -p 8080:80 rise-landing
```

## CI

`Jenkinsfile` : sur `main` / `master`, push Docker Hub `villaroyakevin/rise-landing:latest`.

## Play Store

Activer le bouton `#store-link` dans `index.html` quand l’URL Play Store est connue.
