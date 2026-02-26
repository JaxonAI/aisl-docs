# Model Declarations

A model declaration defines an LLM configuration that can be used to query
language models.

## Syntax

```
declare MODEL_NAME as model {
    OPTION = VALUE,
    OPTION = VALUE,
    ...
}
```

A model can also be declared without options, using defaults:

```
declare my_model as model
```

## Configuration options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `model_name` | string | `"gpt-3.5-turbo"` | The LLM model identifier |
| `endpoint` | string | (proxy default) | API endpoint URL |
| `temperature` | number | `0.7` | Controls randomness (0.0 to 2.0) |
| `max_tokens` | number | `150` | Maximum response length in tokens |
| `top_p` | number | `1.0` | Nucleus sampling parameter (0.0 to 1.0) |
| `frequency_penalty` | number | `0.0` | Penalizes repeated tokens (0.0 to 2.0) |
| `presence_penalty` | number | `0.0` | Penalizes token presence (0.0 to 2.0) |
| `timeout` | number | `30` | Request timeout in seconds |
| `response_format` | string | (none) | Expected response format (e.g., `"json"`) |
| `response_schema` | record | (none) | JSON schema for structured output |

## Examples

A basic model with default settings:

```
declare gpt4 as model {
    model_name = "chat"
}
```

A model with custom parameters:

```
declare creative_model as model {
    model_name = "chat",
    temperature = 1.2,
    max_tokens = 500,
    top_p = 0.9,
    frequency_penalty = 0.5
}
```

A model with a structured response schema:

```
declare classifier as model {
    model_name = "chat",
    temperature = 0.3,
    response_format = "json",
    response_schema = {
        "type": "object",
        "properties": {
            "label": { "type": "string" },
            "confidence": { "type": "number" }
        }
    }
}
```

## Using models

Once declared, a model can be passed to `query_model` to send prompts to the LLM:

```
declare my_model as model { model_name = "chat", temperature = 0.7 }

let response = query_model(my_model, "Is climate change real?", {"topic": "science"});
```

Models can also be associated with datasets to track which model produced a given
set of predictions:

```
declare predictions as dataset { data_file, key = y_pred, model = my_model }
```
