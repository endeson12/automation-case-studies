# Geo Intelligence API

## Problema

Responder consultas de proximidade, cobertura radial e presença de equipamentos em territórios com contratos espaciais explícitos e dados rastreáveis.

## Solução

API FastAPI conectada ao PostgreSQL/PostGIS, com importação GeoJSON autenticada e transacional. Lotes recebem hash SHA-256, proveniência e controle de reimportação idempotente.

## Automações

- ingestão e validação de limites do IBGE e amostras OpenStreetMap;
- verificação de CRS, topologia, coordenadas e duplicidades;
- migrações e testes contra PostGIS real na CI;
- benchmark com `EXPLAIN (ANALYZE, BUFFERS)`;
- Ruff, mypy, pytest, auditoria de dependências, SBOM e scan de imagem.

## Evidências

- [Repositório público](https://github.com/endeson12/geo-intelligence-api)
- [Demonstração em mapa](https://endeson12.github.io/geo-intelligence-api/)
- [Execuções da CI](https://github.com/endeson12/geo-intelligence-api/actions)

## Limites

A demo web é estática e os dados públicos têm limitações documentadas. O projeto não afirma operação institucional, clientes ou SLA.
