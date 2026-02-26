# LLM Queries

These functions send prompts to language models and return structured responses.

## query_model

```
query_model(model, prompt, context)
```

Queries a declared model with a prompt and optional context.

**Parameters:**

- `model` - A model variable (created via `declare ... as model`)
- `prompt` - A string containing the question or prompt
- `context` - An optional record providing additional context for the query

**Returns:** A record whose structure depends on the model's configuration:

**With context (binary mode):**

- `"value"` - Boolean answer
- `"p_yes"` - Probability of "yes"
- `"p_no"` - Probability of "no"
- `"confidence"` - Confidence score

**With `response_schema` configured:**

Returns a record matching the schema defined in the model declaration.

**Without context (free-form mode):**

- `"text"` - The raw LLM response text
- `"confidence"` - Always 1.0

### Example: binary question answering

```
declare my_model as model {
    model_name = "chat",
    temperature = 0.7
}

let response = query_model(
    my_model,
    "Is climate change caused by human activity?",
    {"topic": "science", "source": "IPCC"}
);

let answer = get(response, "value");
let confidence = get(response, "confidence");
```

### Example: collecting multiple responses

```
declare model as model { model_name = "chat", temperature = 0.8 }
let responses = [];

for 1..20 {
    let result = query_model(model, "Is AI beneficial?", {"topic": "ai"});
    append responses with result;
}

let values = get_all(responses, "value");
let consensus = majority_vote(values);
let agreement = agreement_rate(values);
```

### Example: custom response schema

```
declare classifier as model {
    model_name = "chat",
    temperature = 0.3,
    response_format = "json",
    response_schema = {
        "type": "object",
        "properties": {
            "category": { "type": "string" },
            "confidence": { "type": "number" }
        }
    }
}

let result = query_model(classifier, "Classify this text: 'I love this product'");
// result matches the defined schema
```

## llm_query

```
llm_query(prompt, context)
```

Queries the default LLM with a prompt and optional context. Unlike `query_model`,
this function does not require a declared model.

**Parameters:**

- `prompt` - A string containing the question or prompt
- `context` - An optional record providing additional context

**Returns:**

**With context:**

A record in binary mode with `"answer"`, `"confidence"`, `"p_yes"`, and `"p_no"`
fields.

**Without context:**

A record with `"answer"` (the raw text response) and `"confidence"` (always 1.0).

```
let response = llm_query("What is the capital of France?");
let answer = get(response, "answer");
```
