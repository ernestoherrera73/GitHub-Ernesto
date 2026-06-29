# SDR-002 — Build vs. Buy para automatización de procesos

- **Estado:** Aceptada
- **Ámbito:** Optimización de procesos · automatización con IA y no-code
- **Decisores:** Liderazgo tecnológico y dueños de proceso

## Contexto

Varios procesos operativos repetitivos consumían tiempo del equipo y eran propensos a error
(captura de datos, notificaciones, conciliaciones). Se buscaba automatizarlos rápido y con bajo
riesgo, sin desviar al equipo de las prioridades de producto.

## Opciones consideradas

1. **Desarrollo propio (build).** Control total; requiere recursos de ingeniería y mantenimiento continuo.
2. **Plataformas no-code / iPaaS + IA (buy).** Implementación rápida, mantenibles por el negocio; menor control de bajo nivel.
3. **No automatizar (mantener manual).** Sin inversión; conserva el costo y el riesgo de error actuales.

## Criterios de decisión

- **Velocidad de implementación** — semanas, no trimestres.
- **Costo y mantenimiento** — quién lo opera después del despliegue.
- **Riesgo** — reversibilidad y dependencia de proveedor.
- **Foco del equipo** — preservar la capacidad de ingeniería para lo diferenciador.
- **Impacto** — volumen y repetición del proceso (mayor volumen, mayor ROI).

## Decisión

Para procesos estándar de alto volumen se eligió **automatizar con plataformas no-code + IA (opción 2)**,
reservando el **desarrollo propio (opción 1)** solo para lo que constituye ventaja competitiva.

## Consecuencias

- **Positivas:** automatización en semanas; el negocio mantiene los flujos; ingeniería enfocada en lo diferenciador.
- **Compromisos:** dependencia de plataformas externas (mitigada documentando los flujos y datos clave).
- **Seguimiento:** medir horas ahorradas y reducción de errores; revisar periódicamente qué conviene internalizar.
