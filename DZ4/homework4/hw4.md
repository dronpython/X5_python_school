## Теория

### Exceptions

- `try/except/else/finally`: https://pythonz.net/references/named/try-except-finally/
- `raise`: https://pythonz.net/references/named/raise/
- Иерархия Exception: https://docs.python.org/3/library/exceptions.html#exception-hierarchy
- Когда не нужно использовать Exception? https://sobolevn.me/2019/02/python-exceptions-considered-an-antipattern

### Decorators

- Декораторы шаг за шагом: https://pythonworld.ru/osnovy/dekoratory.html

### Generators

- Iterable vs Iterator vs Generator: https://nvie.com/posts/iterators-vs-generators/

### Comprehensions

- Comprehensions: https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html

### Context managers

- Менеджеры контекста: https://pythonz.net/references/named/contextmanager/
- `with`: https://pythonz.net/references/named/with/


## Практика

Задача: реализовать декоратор `@contract`. Смотри файл `contract.py`

Требования:

1. Необходимо проверять типы аргументов и тип выходного значения функции. Указываем кортеж типов для `arg_types`. Каждый тип в кортеже - соответсвует типу аргумента. Для типа выходного значения - указываем `return_type`

```python
@contract(arg_types=(int, int), return_type=int)
def add_two_numbers(first, second):
    return first + second

add_two_numbers(1, 2)  # ok
```

2. Если передан неправильный тип, вызываем ошибку `ContractError`:

```python
add_two_numbers('a', 'b')  # raises ContractError
```

3. Можно не передавать какое-то значение из `arg_types` или `return_type`. Или передать значение `None`: тогда ничего не будет происходить. Пример:

```python
@contract(return_type=int)  # validates only return type, args are ignored

@contract(return_type=None, arg_types=None)  # validation is disabled

@contract(arg_types=(str, str))  # return type check is disabled
```

4. Можно передать специальное значение `Any` для того, чтобы игнорировать какой-то один тип внутри `arg_types`. Например:

```python
@contract(arg_types=(int, Any))
def add_two_numbers(first, second):
    return first + second

add_two_numbers(1, 2)  # ok
add_two_numbers(1, 3.4)  # ok
add_two_numbers(2.1, 1)  # raises ContractError
```

5. Параметр `raises` отвечает за типы исключений, которые функция может кидать. Если выкинутое исключение отсутсвует в списке разрешенных, то мы добавляем `ContractError` (смотри `raise from`). Пример:

```python
@contract(arg_types=(int, int), return_type=float, raises=(ZeroDivisionError,))
def div(first, second):
    return first / second

div(1, 2)  # ok
div(1, 0)  # raises ZeroDisionError
div(1, None)  # raises ContractError from TypeError
```
