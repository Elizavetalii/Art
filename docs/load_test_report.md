# Отчёт по нагрузочному тестированию Art Culinary CRM

- Дата: 2026-02-24
- Инструмент: Locust (`locustfile.py`)
- Профиль: `20` пользователей, скорость набора `5`/с, длительность `45s`
- Хост: `http://127.0.0.1:8000`

## Сводные метрики
- Всего запросов: 4220
- Ошибок: 0 (0.00 fail/s)
- Throughput: 95.59 req/s
- Avg: 17.94 ms
- Median: 18 ms
- p95: 31 ms
- p99: 51 ms

## Топ endpoint по нагрузке
| Метод | Endpoint | Запросов | Ошибок | Req/s | Avg (ms) | p95 (ms) |
|---|---|---:|---:|---:|---:|---:|
| GET | /api/orders/ | 822 | 0 | 18.62 | 14.70 | 32 |
| GET | /api/clients/ | 804 | 0 | 18.21 | 17.39 | 37 |
| GET | /dashboard/admin/ | 352 | 0 | 7.97 | 23.84 | 32 |
| GET | /admin-panel/ | 344 | 0 | 7.79 | 23.08 | 31 |
| GET | /admin-panel/backups/ | 344 | 0 | 7.79 | 23.05 | 30 |
| GET | /admin-panel/roles/ | 344 | 0 | 7.79 | 22.81 | 31 |
| GET | /admin-panel/users/ | 344 | 0 | 7.79 | 23.02 | 30 |
| GET | /api/clients/5/ | 152 | 0 | 3.44 | 7.90 | 15 |
| GET | /api/clients/6/ | 151 | 0 | 3.42 | 7.97 | 15 |
| GET | /api/clients/3/ | 147 | 0 | 3.33 | 7.66 | 15 |

## Файлы артефактов
- `docs/locust_integration_stats.csv`
- `docs/locust_integration_stats_history.csv`
- `docs/locust_integration_failures.csv`
- `docs/locust_integration_exceptions.csv`