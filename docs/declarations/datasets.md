# Dataset Declarations

A dataset declaration loads data from a JSON file and extracts a specific field
for use in evaluations.

## Syntax

```
declare DATASET_NAME as dataset {
    FILE_REFERENCE,
    key = FIELD_NAME,
    model = MODEL_NAME
}
```

| Component | Required | Description |
|-----------|----------|-------------|
| `FILE_REFERENCE` | Yes | An identifier referencing a previously declared file |
| `key` | Optional | The JSON field to extract from the loaded data |
| `model` | Optional | A model to associate with this dataset for lineage tracking |

## How datasets work

When a dataset is declared, AISL:

1. Resolves the file reference to find the JSON file on disk
2. Loads and parses the JSON content
3. Extracts the array at the specified `key`
4. Stores the result as an array accessible by the dataset name

## Examples

Loading ground truth and predictions from a file:

```
declare data_file as file { name = results, type = json }

declare ground_truth as dataset { data_file, key = y_true }
declare predictions as dataset { data_file, key = y_pred, model = resnet50 }
```

Given a JSON file `results.json` with this structure:

```json
{
    "y_true": [0, 1, 1, 0, 1],
    "y_pred": [0, 1, 0, 0, 1]
}
```

The `ground_truth` dataset would contain `[0, 1, 1, 0, 1]` and `predictions`
would contain `[0, 1, 0, 0, 1]`.

## Using datasets

Datasets can be used directly as arguments to built-in functions:

```
let acc = accuracy(ground_truth, predictions);
let f1 = f1_score(ground_truth, predictions);
```

You can also transform dataset values before use:

```
let y_true = argmax(ground_truth);
let y_pred = argmax(predictions);
let flat = flatten(ground_truth);
```

## Model association

Linking a dataset to a model via the `model` option records a lineage
relationship in the object graph. This tracks that the data in the dataset was
produced by that model:

```
declare my_model as model { model_name = "chat" }
declare model_outputs as dataset { data_file, key = responses, model = my_model }
```
