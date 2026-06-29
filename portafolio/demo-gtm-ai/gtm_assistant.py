"""
GTM Assistant — Asistente de Go-to-Market con IA.

Genera un borrador de plan Go-to-Market (público objetivo, propuesta de valor,
canales, mensajes clave y métricas) a partir de la descripción de un producto.

Diseñado por Ernesto Herrera Rosales como demo de portafolio: combina su
experiencia en estrategia de producto / GTM con el uso práctico de la OpenAI API.

Uso:
    python gtm_assistant.py --producto "TMS para PYMEs de transporte" --mercado "México"
    python gtm_assistant.py --producto "App de eventos" --mock   # sin API key

Si no hay OPENAI_API_KEY (o se usa --mock), corre en MODO MOCK con una
respuesta estructurada de ejemplo, para que el demo funcione siempre.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import textwrap

# Asegura salida UTF-8 también en consolas Windows (cp1252), que no codifican emojis.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[union-attr]
    except (AttributeError, ValueError):
        pass

PROMPT_SISTEMA = (
    "Eres un consultor senior de Go-to-Market y estrategia de producto con más de "
    "20 años de experiencia. Devuelves planes accionables, concisos y realistas. "
    "Responde SIEMPRE en español y EXCLUSIVAMENTE en JSON válido con las claves: "
    "publico_objetivo (lista), propuesta_de_valor (texto), canales (lista), "
    "mensajes_clave (lista), metricas_exito (lista), primeros_30_dias (lista)."
)


def construir_prompt_usuario(producto: str, mercado: str) -> str:
    """Arma el prompt del usuario para el modelo."""
    return (
        f"Producto/servicio: {producto}\n"
        f"Mercado objetivo: {mercado}\n\n"
        "Genera un plan Go-to-Market inicial siguiendo el formato JSON solicitado."
    )


def generar_con_openai(producto: str, mercado: str, modelo: str) -> dict:
    """Llama a la OpenAI API para generar el plan. Requiere OPENAI_API_KEY."""
    # Import diferido: el modo mock no necesita la dependencia instalada.
    from openai import OpenAI

    client = OpenAI()  # toma OPENAI_API_KEY del entorno
    respuesta = client.chat.completions.create(
        model=modelo,
        messages=[
            {"role": "system", "content": PROMPT_SISTEMA},
            {"role": "user", "content": construir_prompt_usuario(producto, mercado)},
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
    )
    contenido = respuesta.choices[0].message.content
    return json.loads(contenido)


def generar_mock(producto: str, mercado: str) -> dict:
    """Devuelve un plan de ejemplo sin llamar a ninguna API (modo demo)."""
    return {
        "publico_objetivo": [
            f"Tomadores de decisión en empresas del segmento objetivo de '{producto}'",
            f"Operaciones y dueños de proceso en {mercado}",
            "Early adopters con dolor claro y presupuesto asignado",
        ],
        "propuesta_de_valor": (
            f"'{producto}' reduce fricción operativa y mejora la visibilidad del proceso, "
            f"acelerando resultados medibles para clientes en {mercado}."
        ),
        "canales": [
            "Venta directa B2B y demos guiadas",
            "LinkedIn / Sales Navigator (prospección dirigida)",
            "Alianzas y referidos de partners del sector",
            "Contenido educativo (casos de éxito, webinars)",
        ],
        "mensajes_clave": [
            "Menos trabajo manual, más decisiones con datos",
            "Implementación rápida y ROI temprano",
            "Diseñado para la realidad operativa del mercado local",
        ],
        "metricas_exito": [
            "Leads calificados (SQL) por mes",
            "Tasa de conversión demo → cliente",
            "Tiempo de implementación (time-to-value)",
            "Retención / churn a 90 días",
        ],
        "primeros_30_dias": [
            "Definir ICP (perfil de cliente ideal) y lista de cuentas objetivo",
            "Preparar guion de demo y materiales de venta",
            "Lanzar prospección dirigida en 1-2 canales",
            "Cerrar 3-5 conversaciones de descubrimiento con clientes potenciales",
        ],
    }


def imprimir_plan(plan: dict, producto: str, mercado: str, modo: str) -> None:
    """Imprime el plan de forma legible en consola."""
    sep = "=" * 64
    print(sep)
    print(f"  PLAN GO-TO-MARKET  ·  {producto}  ·  {mercado}  [{modo}]")
    print(sep)

    secciones = [
        ("🎯 Público objetivo", "publico_objetivo"),
        ("💡 Propuesta de valor", "propuesta_de_valor"),
        ("📣 Canales", "canales"),
        ("🗣️  Mensajes clave", "mensajes_clave"),
        ("📊 Métricas de éxito", "metricas_exito"),
        ("🚀 Primeros 30 días", "primeros_30_dias"),
    ]
    for titulo, clave in secciones:
        valor = plan.get(clave)
        print(f"\n{titulo}")
        if isinstance(valor, list):
            for item in valor:
                for linea in textwrap.wrap(f"• {item}", width=62):
                    print(f"  {linea}")
        else:
            for linea in textwrap.wrap(str(valor), width=62):
                print(f"  {linea}")
    print(f"\n{sep}")


def parsear_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Genera un plan Go-to-Market a partir de la descripción de un producto."
    )
    parser.add_argument("--producto", required=True, help="Descripción del producto o servicio.")
    parser.add_argument("--mercado", default="México", help="Mercado objetivo (default: México).")
    parser.add_argument("--modelo", default="gpt-4o-mini", help="Modelo de OpenAI a usar.")
    parser.add_argument("--mock", action="store_true", help="Forzar modo mock (sin API).")
    parser.add_argument("--json", action="store_true", help="Imprimir salida en JSON crudo.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parsear_args(argv)

    usar_mock = args.mock or not os.getenv("OPENAI_API_KEY")
    modo = "MOCK" if usar_mock else f"OpenAI:{args.modelo}"

    try:
        if usar_mock:
            plan = generar_mock(args.producto, args.mercado)
        else:
            plan = generar_con_openai(args.producto, args.mercado, args.modelo)
    except Exception as exc:  # noqa: BLE001 — demo: degradar a mock ante cualquier fallo
        print(f"[aviso] Falló la llamada a OpenAI ({exc}). Usando modo mock.", file=sys.stderr)
        plan = generar_mock(args.producto, args.mercado)
        modo = "MOCK (fallback)"

    if args.json:
        print(json.dumps(plan, ensure_ascii=False, indent=2))
    else:
        imprimir_plan(plan, args.producto, args.mercado, modo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
