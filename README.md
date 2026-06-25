# Parcial Testing TicketFast

Pruebas de Integración, Sistema y E2E para la plataforma de reserva de boletos TicketFast.

## Estructura del proyecto

- `src/` - Código fuente de la aplicación
- `src/database/` - Modelos, configuración y repositorio de base de datos
- `src/reservas/` - API FastAPI con endpoints de reservas
- `tests/integration/` - Pruebas de integración con TestContainers y PostgreSQL real
- `tests/system/` - Pruebas de sistema con httpx contra API desplegada en Docker
- `tests/e2e/` - Pruebas E2E de frontend con Playwright

## Cómo ejecutar las pruebas

### Pruebas de integración (locales con TestContainers)
```bash
pytest tests/integration/ -v
```

### Pruebas de sistema e integración (Docker)
```bash
docker-compose -f docker-compose.test.yml up --build
```

### Pruebas E2E frontend (Playwright)
```bash
playwright install chromium
pytest tests/e2e/ -v
```

## Resultados

- ✅ Pruebas de integración: PASSED
- ✅ Pruebas de sistema: PASSED  
- ✅ Pruebas E2E frontend: PASSED