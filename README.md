# WorkmateTestTask

CLI-утилита для генерации отчётов по зарплатам сотрудников на основе CSV-файлов.

---

## Установка

1. Создать и активировать виртуальное окружение:

```bash
    python -m venv .venv
    source .venv/bin/activate    # для Linux/macOS
    .venv\Scripts\activate       # для Windows
````

2. Установить зависимости:

```bash
    pip install -r requirements.txt
```

---

## Запуск

```bash
    python main.py data1.csv data2.csv data3.csv --report payout
```

---

## Тесты

```bash
    pytest
```

Покрытие:

```bash
    pytest --cov=. --cov-report=term
```

---

## Автор

[Khalil](https://t.me/itskhalilS)

