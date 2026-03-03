
![AISL Logo](images/logo.png)

# Introduction

AISL (AI Specification Language) is a domain-specific language for specifying and
evaluating AI model performance. It provides a declarative syntax for defining
models, loading datasets, running evaluations, and computing metrics.

## What AISL does

AISL is designed for AI evaluation workflows. It allows you to:

- **Declare models** with their configuration parameters (temperature, max tokens, etc.)
- **Load datasets** from JSON files and extract fields for evaluation
- **Query language models** with structured prompts and collect responses
- **Compute metrics** such as accuracy, F1 score, precision, recall, and many more
- **Evaluate performance** by grouping metrics with pass/fail conditions
- **Track lineage** between models, datasets, and metrics through an object graph

## A quick example

```
declare gpt4 as model {
    model_name = "chat",
    temperature = 0.7,
    max_tokens = 150
}

declare data_file as file { name = results, type = json }
declare ground_truth as dataset { data_file, key = y_true }
declare predictions as dataset { data_file, key = y_pred, model = gpt4 }

let y_true = flatten(ground_truth);
let y_pred = flatten(predictions);

declare eval as performance {
    metric[accuracy](y_true, y_pred) > 0.9 ? "Pass" : "Fail",
    metric[f1_score](y_true, y_pred),
    metric[precision](y_true, y_pred),
    metric[recall](y_true, y_pred)
}
```

This program declares a model, loads ground truth and prediction data from a JSON
file, computes four evaluation metrics, and marks accuracy as passing or failing
against a threshold.

## Program structure

An AISL program is a sequence of statements. Each statement is one of:

- A **declaration** (`declare ... as ...`)
- An **expression** followed by a semicolon
- A **variable assignment** (`let ... = ...;`)
- A **return statement** (`return ...;`)
- A **for loop** (`for N..M { ... }`)
- An **append statement** (`append ... with ...;`)
