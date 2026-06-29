# Portafolio — Ernesto Herrera Rosales

> Líder Tecnológico · Product & Business Transformation · +20 años en TI
>
> Email: ernesto.herrera@gmail.com · LinkedIn: [ingernestoherrera](https://www.linkedin.com/in/ingernestoherrera/)

**Español** · [English](#english)

Este directorio contiene el portafolio de GitHub de Ernesto, organizado como **carpetas independientes**.
Cada carpeta está pensada para convertirse en un **repositorio público propio** en su cuenta de GitHub.

## Contenido

| Carpeta | Repo destino sugerido | Descripción |
| --- | --- | --- |
| [`perfil-github/`](./perfil-github/) | `ernestoherrera/ernestoherrera` | Profile README: portada del perfil de GitHub. |
| [`gtm-strategy-playbook/`](./gtm-strategy-playbook/) | `gtm-strategy-playbook` | Framework reutilizable de Go-to-Market. |
| [`ai-for-business/`](./ai-for-business/) | `ai-for-business` | Marco de decisión para adoptar IA en operaciones. |
| [`strategy-decision-records/`](./strategy-decision-records/) | `strategy-decision-records` | Decisiones de negocio documentadas (estilo ADR). |
| [`reclutalia/`](./reclutalia/) | `reclutalia-case-study` | Caso de estudio: reclutamiento con automatización. |
| [`zeus-eventos/`](./zeus-eventos/) | `zeus-eventos-case-study` | Caso de estudio: eventos con registro inteligente. |
| [`demo-gtm-ai/`](./demo-gtm-ai/) | `gtm-assistant` | Demo técnico funcional: asistente GTM con OpenAI API (Python). |
| Sitio web (raíz del repo) | GitHub Pages | Sitio de portafolio (HTML/CSS/JS) con diseño ejecutivo, responsivo y bilingüe. Ver [`web/README.md`](./web/README.md). |

> **Sitio en vivo:** https://ernestoherrera73.github.io/GitHub-Ernesto/
> · **CV (PDF):** [descargar](../CV_ErnestoHerrera_ESP_202501.pdf)

> Enfoque ejecutivo: el portafolio prioriza **criterio estratégico, liderazgo y resultados**.
> El componente técnico demuestra fluidez con el entorno (Git, Python, APIs), no es código de producción.

## Cómo publicarlo en GitHub (cuando esté listo)

> Por ahora todo es **local**. Estos pasos son la guía para la migración a la cuenta de Ernesto.

1. Crear el perfil/cuenta pública (sugerencia: `github.com/ernestoherrera`).
2. Para el **Profile README**, crear un repo público con el mismo nombre que el usuario (`ernestoherrera`) y subir el contenido de `perfil-github/`.
3. Para cada repo, crear un repositorio público y subir la carpeta correspondiente:

   ```bash
   cd gtm-strategy-playbook
   git init -b main
   git add .
   git commit -m "docs: GTM strategy playbook"
   git remote add origin git@github.com:ernestoherrera/gtm-strategy-playbook.git
   git push -u origin main
   ```

4. Fijar (pin) en el perfil los repos más estratégicos: `gtm-strategy-playbook`, `ai-for-business` y `strategy-decision-records`.

---

## English

This directory holds Ernesto's GitHub portfolio, organized as **standalone folders**. Each folder is meant
to become its **own public repository**. The portfolio leads with **strategy, leadership and results**;
the technical piece shows fluency with the environment (Git, Python, APIs), not production code.

**Contents:** profile README, GTM strategy playbook, AI-for-business decision framework, strategy decision
records, two product case studies (Reclutalia, ZEUS Eventos) and a working GTM assistant demo.

**Publishing (when ready):** create the public account, push `perfil-github/` to a repo named exactly like
the username to enable the profile README, then create one public repo per folder and pin the most strategic ones.
