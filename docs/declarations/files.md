# File Declarations

A file declaration defines a reference to a data file on disk.

## Syntax

```
declare FILE_NAME as file {
    name = FILENAME,
    type = FORMAT,
    model = MODEL_REF,
    key = FIELD_NAME,
    path = DIRECTORY
}
```

| Option | Required | Description |
|--------|----------|-------------|
| `name` | Yes | The filename without extension |
| `type` | Yes | The file format (currently `json`) |
| `model` | Optional | A model to associate with this file |
| `key` | Optional | A field name within the file |
| `path` | Optional | Directory path for the file |

## Examples

A basic file reference:

```
declare data_file as file { name = results, type = json }
```

This references a file called `results.json` in the working directory.

A file with a model association:

```
declare output_file as file {
    name = predictions,
    type = json,
    model = my_model
}
```

## How files are used

File declarations are primarily used as references in dataset declarations. The
dataset uses the file to locate and load data:

```
declare data_file as file { name = experiment_results, type = json }
declare ground_truth as dataset { data_file, key = labels }
declare predictions as dataset { data_file, key = outputs }
```

File declarations also create nodes in the object graph for lineage tracking.

## Supported formats

Currently, AISL supports JSON files only. The file must contain valid JSON that
can be parsed into arrays or objects.
