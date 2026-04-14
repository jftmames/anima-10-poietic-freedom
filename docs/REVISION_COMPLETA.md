# Revisión completa de la aplicación (ANIMa-10)

Fecha: 2026-04-14

## 1) Alcance

Se revisaron:

- Núcleo de cálculo (`src/`): `lstar.py`, `mdl_delta.py`, `network_rupture.py`, `pipeline.py`.
- Ejecución batch (`scripts/run_pipeline.py`).
- Interfaz Streamlit (`streamlit_app.py` y `pages/`).
- Documentación funcional mínima (`README.md`, `docs/data_dictionary.md`, `docs/METHODS.md`).
- Pruebas automáticas (`tests/test_basic.py`).

## 2) Estado general

**Resultado ejecutivo:** la base conceptual está bien delimitada y el repositorio es claro para uso académico/demo, pero actualmente hay **bloqueos de ejecución** importantes que impiden considerar la app como "lista para producción".

## 3) Hallazgos principales

### Crítico

1. **`src/pipeline.py` está incompleto/roto**
   - La función `eval_case` usa variables no definidas (`case`, `mdl`, `rupt`) y nunca carga el JSON ni computa señales.
   - Impacto: el pipeline de datos no puede funcionar correctamente incluso con dependencias instaladas.
   - Prioridad: **P0**.

2. **Dependencias no garantizadas en entorno de ejecución**
   - `pytest` falla por falta de `numpy`; `scripts/run_pipeline.py` falla por falta de `pandas`.
   - Impacto: no hay validación automática ni generación de reportes en un entorno limpio sin instalar paquetes.
   - Prioridad: **P0**.

### Alta

3. **Cobertura de tests insuficiente para rutas críticas**
   - Solo hay dos tests muy básicos (`L*` y `mdl_delta` vacío).
   - No hay tests para `pipeline`, `network_rupture`, lectura de casos, ni interfaz.
   - Impacto: regresiones silenciosas (como el `pipeline.py` actual).
   - Prioridad: **P1**.

4. **`scripts/run_pipeline.py` usa patrón glob frágil**
   - `data/case_files/**/**/*.json` es redundante y poco legible; puede ocultar errores de mantenimiento.
   - Prioridad: **P1**.

### Media

5. **Persistencia temporal en Streamlit mejorable**
   - En `2_🧪_Analizador_Interactivo.py` se escriben archivos temporales fijos (`temp_pre.csv`, `temp_post.csv`) sin limpieza.
   - Riesgo de colisión/sobrescritura si hay ejecuciones simultáneas o despliegues compartidos.
   - Prioridad: **P2**.

6. **Desajuste posible de activos del frontend**
   - `streamlit_app.py` intenta servir `pages/art3.pdf`, pero en el repo no se observa ese archivo en el listado principal.
   - Si falta en despliegue, el botón de descarga no funcionará (aunque se muestra mensaje de error).
   - Prioridad: **P2**.

## 4) Fortalezas detectadas

- Estructura de proyecto legible y modular.
- Separación explícita de licencias para código y datos.
- Modelo de dominio bien documentado (`data_dictionary`, `METHODS`).
- UI Streamlit útil para exploración y demostración didáctica.

## 5) Plan de remediación recomendado

### Fase 1 (urgente)

1. Reparar `src/pipeline.py`:
   - Cargar `case` desde `case_path`.
   - Resolver rutas de corpus/grafos.
   - Calcular `mdl_delta` y `rupture_score`.
   - Manejar faltantes con errores controlados.
2. Añadir tests unitarios del pipeline y de lectura de grafos/corpus.
3. Ajustar CI para instalar dependencias exactas (`environment.yml` o `requirements.txt` + lock).

### Fase 2

4. Sustituir temporales fijos en Streamlit por `tempfile.NamedTemporaryFile` o procesamiento en memoria.
5. Validar existencia de `art3.pdf` en build/deploy o parametrizar ruta.
6. Aumentar cobertura mínima objetivo (por ejemplo, >=80% en módulo `src/`).

### Fase 3

7. Endurecer validación de esquemas JSON (pydantic/jsonschema).
8. Añadir smoke tests de pipeline de extremo a extremo con un subconjunto de casos.

## 6) Conclusión

La aplicación tiene una **buena base académica y de diseño**, pero necesita resolver errores de ejecución y cobertura de pruebas para ser operativamente confiable. La prioridad inmediata es restaurar el pipeline y reforzar la validación automatizada.
