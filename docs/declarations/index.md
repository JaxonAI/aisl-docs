# Declarations

Declarations are the primary way to define named entities in AISL. Every
declaration follows the same general syntax:

```
declare NAME as TYPE { ... }
```

Where `NAME` is an identifier and `TYPE` is one of the supported declaration
types.

## Declaration types

AISL supports five declaration types:

| Type | Purpose |
|------|---------|
| [`model`](models.md) | Define an LLM with configuration parameters |
| [`dataset`](datasets.md) | Load data from a JSON file |
| [`file`](files.md) | Reference a data file with metadata |
| [`performance`](performance.md) | Group metrics for evaluation |
| [`function`](../functions.md) | Define a reusable function |

## How declarations work

Each declaration creates a named variable in the global scope. After a
declaration, the name can be used in expressions and passed as an argument to
functions.

```
declare my_model as model { model_name = "chat" }

// my_model is now available as a variable
let response = query_model(my_model, "Hello");
```

## Lineage tracking

Declarations participate in AISL's object graph, which tracks data lineage and
provenance. When a dataset references a model, or a performance block uses
datasets and functions, these relationships are recorded. This allows you to trace
which models and data sources contributed to any given metric result.
