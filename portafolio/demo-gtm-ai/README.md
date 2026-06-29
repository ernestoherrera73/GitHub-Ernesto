# GTM Assistant — Asistente de Go-to-Market con IA

Demo técnico **funcional**: genera un borrador de plan **Go-to-Market** a partir de la descripción
de un producto, usando la **OpenAI API** (con modo *mock* para correr sin clave). Une la experiencia
en estrategia de producto / GTM con el uso práctico de IA.

**Español** · [English](#english)

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI_API-412991?logo=openai&logoColor=white)
![Licencia](https://img.shields.io/badge/Licencia-MIT-green)

---

## Qué hace

A partir de un producto y un mercado, genera un plan GTM estructurado con: público objetivo,
propuesta de valor, canales, mensajes clave, métricas de éxito y acciones de los primeros 30 días.

## Inicio rápido

> No necesitas clave para probarlo: corre en modo *mock* automáticamente.

```bash
# 1) (Opcional) entorno virtual
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 2) Probar en modo mock (sin instalar nada)
python gtm_assistant.py --producto "TMS para PYMEs de transporte" --mercado "México" --mock
```

### Modo real (con OpenAI)

```bash
pip install -r requirements.txt
cp .env.example .env          # y coloca tu OPENAI_API_KEY
export OPENAI_API_KEY=sk-...  # Windows PowerShell: $env:OPENAI_API_KEY="sk-..."

python gtm_assistant.py --producto "App de gestión de eventos" --mercado "LatAm"
```

> Si no hay `OPENAI_API_KEY`, o si la llamada falla, el script degrada automáticamente a modo *mock*
> para que el demo nunca se rompa.

## Opciones

| Flag | Descripción | Default |
| --- | --- | --- |
| `--producto` | Descripción del producto/servicio (requerido) | — |
| `--mercado` | Mercado objetivo | `México` |
| `--modelo` | Modelo de OpenAI | `gpt-4o-mini` |
| `--mock` | Forzar modo mock (sin API) | `false` |
| `--json` | Imprimir salida en JSON crudo | `false` |

## Ejemplo de salida (mock)

```
================================================================
  PLAN GO-TO-MARKET · TMS para PYMEs de transporte · México [MOCK]
================================================================

Público objetivo
  - Tomadores de decisión en empresas del segmento objetivo...
  - Operaciones y dueños de proceso en México
  ...

Propuesta de valor
  'TMS para PYMEs de transporte' reduce fricción operativa...
```

## Decisiones de diseño

- **Funciona siempre:** modo mock más *fallback* ante errores; ideal para un demo de portafolio.
- **Salida estructurada:** se fuerza JSON (`response_format`) para resultados parseables.
- **Sin secretos en el repo:** la clave va en `.env` (ignorado por Git).
- **Dependencias mínimas:** el mock usa solo la librería estándar.

> Este demo implementa la plantilla del repo **gtm-strategy-playbook**.

---

## English

**GTM Assistant** is a small, working demo that drafts a **Go-to-Market plan** from a product description
using the **OpenAI API**, with a built-in **mock mode** so it runs without an API key.

```bash
python gtm_assistant.py --producto "TMS for SMB carriers" --mercado "Mexico" --mock
```

It outputs target audience, value proposition, channels, key messages, success metrics and first-30-days
actions. Without `OPENAI_API_KEY` (or on any API error) it gracefully falls back to mock mode, so the demo
never breaks. It implements the template from the **gtm-strategy-playbook** repo.

---

Licencia MIT · Demo educativa de portafolio.
