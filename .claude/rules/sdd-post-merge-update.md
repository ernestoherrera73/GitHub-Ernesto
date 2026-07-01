# SDD — Actualización de reglas tras merge

Al completar un cambio OpenSpec (specs nuevas + actualización de código + merge / `opsx:archive`),
DEBES ejecutar el siguiente paso adicional antes de cerrar el cambio:

## Paso obligatorio post-merge: actualizar reglas SDD

1. **Identificar aprendizajes del cambio**: patrones repetidos, restricciones descubiertas,
   decisiones de diseño no obvias, errores de proceso evitados.

2. **Actualizar los artefactos SDD afectados** (al menos uno debe quedar actualizado):
   - `docs/base-standards.md` — principios, convenciones de idioma, reglas OpenSpec.
   - `docs/documentation-standards.md` — estructura y mantenimiento de docs.
   - `docs/<area>-standards.md` — estándar específico del área (backend, frontend, sql, etc.).
   - `openspec/config.yaml` — reglas por artefacto o contexto del proyecto.
   - `.claude/rules/*.md` — reglas de comportamiento del agente.

3. **Criterio de qué agregar**: solo lo que no sea derivable del código o del historial git.
   - Restricciones ocultas o invariantes sutiles → `base-standards.md`.
   - Convenciones de estructura de archivos → `documentation-standards.md`.
   - Reglas de proceso del agente → `.claude/rules/`.
   - No copiar lo que ya está documentado; enlazar si ya existe en otro doc.

4. **Verificar integridad de referencias** (base-standards §6):
   - Sin enlaces rotos tras renombrar/mover artefactos.
   - Sin duplicación: cada dato tiene una sola fuente canónica.

## Cuándo aplica

- Al ejecutar `opsx:archive` o `/openspec-archive-change`.
- Al hacer merge de una feature branch de cualquier cambio OpenSpec.
- Si el cambio fue trivial y no generó aprendizajes nuevos, documentar explícitamente
  "Sin actualizaciones SDD requeridas" en el reporte de cierre.
