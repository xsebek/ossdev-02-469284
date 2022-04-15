# ossdev-02-469284

[![Python application](https://github.com/xsebek/ossdev-02-469284/actions/workflows/python-app.yml/badge.svg?branch=main)](https://github.com/xsebek/ossdev-02-469284/actions/workflows/python-app.yml)

Open Source Developement course git assignment.

- course page: [crocs-muni/open-source-development-course](https://github.com/crocs-muni/open-source-development-course)
- assignment description: [Single-developer scenario](https://github.com/crocs-muni/open-source-development-course/blob/master/assignments.md#1-single-developer-scenario-deadline-20-4)

## Run

You can check out the application with:

```bash
$ python3 primezz 11 42
11
13
17
19
23
29
31
37
41
```

## Install

If you want to list primes without switching directories, you can install the app:

```bash
$ pip install -e .
$ cd /your/other/working/dir
$ primezz -10 10
-7
-5
-3
-2
2
3
5
7
```

## Test

The tests use the `unittest` framework, which should come preinstalled with your Python distribution:
```bash
$ python -m unittest -v tests/unit.py
test_fact (tests.unit.PrimeExamples) ... ok
test_primality_example (tests.unit.PrimeExamples) ... ok
test_prime_0 (tests.unit.PrimeExamples) ... ok
test_prime_1 (tests.unit.PrimeExamples) ... ok
test_prime_2 (tests.unit.PrimeExamples) ... ok
test_prime_minus_2 (tests.unit.PrimeExamples) ... ok
test_primes_500 (tests.unit.ReferencePrime) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.032s

OK
```
