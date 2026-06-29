# Sitio de portafolio — Ernesto Herrera Rosales

> El sitio web vive en la **raíz del repositorio** (`index.html`, `styles.css`, `script.js`)
> para poder publicarse en GitHub Pages desde la raíz. Esta carpeta solo conserva esta nota.

Sitio web estático (HTML + CSS + JS, sin dependencias ni build) con diseño ejecutivo claro,
responsivo (celular, tablet, PC) y bilingüe (español/inglés con toggle).

## Ver localmente

```bash
# desde la raíz del repositorio
python -m http.server 4321
# abrir http://localhost:4321
```

## GitHub Pages

Publicado desde la rama `main`, carpeta raíz (`/`):
`https://ernestoherrera73.github.io/GitHub-Ernesto/`

Configuración: **Settings → Pages → Source: Deploy from a branch → `main` / `/ (root)`**.

## Estructura (en la raíz del repo)

- `index.html` — contenido y secciones (perfil, impacto, trayectoria, portafolio, formación, contacto).
- `styles.css` — diseño y responsividad (variables CSS, grid/flex, breakpoints 860px y 480px).
- `script.js` — menú móvil, toggle de idioma ES/EN y año del footer.
