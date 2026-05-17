# Таблица оценки решения

## Результат evaluate-score

```text
@1sandreevna ➜ /workspaces/sbd-contests-uggu-spring-2026-public (result) $ make evaluate-score

pipenv install --dev

To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

Installing dependencies from Pipfile.lock (c5405f)...
Installing dependencies from Pipfile.lock (c5405f)...

pipenv run python scripts/evaluate_contest_score.py --with-certification

Оценка по критериям (0–3 за критерий; сумма до 75), ROOT=/workspaces/sbd-contests-uggu-spring-2026-public:

  C01: Все тесты репозитория (включая тесты решения) завершаются успешно: 3.0  (OK)
  C02: Все тесты решения находятся в подкаталогах src_solution/tests: 3.0
  C03: Маркер security в pytest.ini и использование в тестах: 3.0
  C04: Покрытие тестами event_log / журнал: 3.0
  C05: Пример sga.json: 3.0
  C06: SBOM TCB / OTHER в примерах: 3.0
  C07: Успешное выполнение сертификации (пакет + ответ Регулятора): 3.0
  C08: Сквозной автотест ЦР–АБУ (основной сценарий): 3.0
  C09: Оформление кода в src_solution (flake8, PEP8): 3.0
  C10: Решение: журнал событий / event_log в src_solution: 3.0
  C11: Решение: зависимости (requirements / pyproject в src_solution): 3.0
  C12: Тесты репозитория импортируют код из src_solution (AST): 3.0
  C13: Раздел тестов безопасности в src_solution/docs/solution.md: 3.0
  C14: numpy в SBOM решения (SBOM_TCB vs SBOM_OTHER): 3.0
  C15: Тесты: журнал event_log и решение (импорты из src_solution + event_log): 3.0
  C16: Покрытие ДВБ решения (src_solution/abu/tcb) тестами: 3.0
  C17: Отчёт о решении (приоритет src_solution/docs/solution.md): 3.0
  C18: security_monitor, policies в src_solution; тесты политик: 3.0
  C19: домены и монитор; разнесение по процессам: 2.0
  C20: Стоимость сертификации — место в рейтинге: 0.0
  C21: Экспертно — соответствие политик архитектуре АБУ: 0.0
  C22: Экспертно — полнота отчёта и воспроизводимость: 0.0
  C23: Размер доменов ДВБ: 3.0
  C24: Количество интерфейсов домена ДВБ: 3.0
  C25: Наличие security_monitor, security-тесты и покрытие monitor-кода: 3.0

Сумма (raw): 65.0 / 75

Сертификация (ответ Регулятора):
успех=True
стоимость≈1093.01 усл. ед.
```

## Результат certify-abu

```text
@1sandreevna ➜ /workspaces/sbd-contests-uggu-spring-2026-public (result) $ make certify-abu

pipenv install --dev
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

Installing dependencies from Pipfile.lock (c5405f)...
Installing dependencies from Pipfile.lock (c5405f)...

bash scripts/prepare_certification_bundle.sh
Записано: /workspaces/sbd-contests-uggu-spring-2026-public/src_starting_point/sbom/SBOM_TCB.cdx.json
Записано: /workspaces/sbd-contests-uggu-spring-2026-public/src_starting_point/sbom/SBOM_OTHER.cdx.json
Пакет: /workspaces/sbd-contests-uggu-spring-2026-public/artifacts/abu_certification_bundle.tar.gz

pipenv run python scripts/run_certification.py
Результат сертификации: успешно
Стоимость (усл. ед.): 2255.40
ДВБ: строк кода abu=378, суммарная цикломатика=49
Сертификат (SHA-256 пакета): 4a1c3efc593d57d60ae46e3d2331b6ad95ed45edde158a7c417613382d5aa017
```
---

### Итог

- evaluate-score: **65 / 75**
- certification in evaluate-score: **success**, стоимость≈**1093.01** усл. ед.
- standalone certify-abu: **успешно**, стоимость **2255.40** усл. ед.
- TCB coverage: **100%**
- security_monitor coverage: **100%**