<!-- markdownlint-disable -->

<a href="../../backend/src/utils/repository.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils.repository`






---

<a href="../../backend/src/utils/repository.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AbstractRepository`







---

<a href="../../backend/src/utils/repository.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `AbstractRepository.get_result`

```python
get_result(limit: int)
```





---

<a href="../../backend/src/utils/repository.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `AbstractRepository.set_field`

```python
set_field(parameters: src.schemas.field.FieldDatabaseSchema)
```






---

<a href="../../backend/src/utils/repository.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SQLAlchemyRepository`







---

<a href="../../backend/src/utils/repository.py#L69"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SQLAlchemyRepository.get_result`

```python
get_result(limit: int) → list
```





---

<a href="../../backend/src/utils/repository.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `SQLAlchemyRepository.set_field`

```python
set_field(
    parameters: src.schemas.field.FieldDatabaseSchema
) → FieldResponseSchema
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
