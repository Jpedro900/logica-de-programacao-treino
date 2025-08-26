# Desafios de Lógica e Estruturas de Dados

Evolução gradual em Python. Cada desafio fica em `desafios/` e os testes em `tests/` (pytest).

## ✅ Progresso (concluídos)
- [x] Desafio 001 — Soma simples (`sum_two`)
- [x] Desafio 002 — Máximo de três (`max_three`)
- [x] Desafio 003 — Contar pares (`count_evens`)
- [x] Desafio 004 — Reverter string (`reverse_str`)
- [x] Desafio 005 — Palíndromo básico (`is_palindrome`)
- [x] Desafio 006 — Contar vogais (`count_vowels`)
- [x] Desafio 007 — Remover vogais (`remove_vowels`)
- [x] Desafio 008 — Fatorial (iterativo) (`factorial`)
- [x] Desafio 009 — Fibonacci até n termos (`fibonacci`)
- [x] Desafio 010 — Anagramas (`is_anagram`)

## ▶️ Como rodar
```bash
py -m pip install pytest
py -m pytest -q
```

## Estrutura sugerida
```
<repo>/
├─ desafios/ (desafio_001.py ... desafio_010.py)
├─ tests/ (test_desafio_001.py ... test_desafio_010.py)
├─ pytest.ini  # com: [pytest]\npythonpath = .
└─ README.md
```
