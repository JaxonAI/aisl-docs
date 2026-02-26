# Response Parsing

These functions parse and extract structured information from text, particularly
useful for processing LLM responses.

## parse_json

```
parse_json(text)
```

Parses a JSON string into a record or list.

**Parameters:**

- `text` - A string containing valid JSON

**Returns:** The parsed JSON value (record or list).

```
let data = parse_json("{\"name\": \"test\", \"score\": 0.95}");
// data = {"name": "test", "score": 0.95}
```

## extract_key

```
extract_key(text, key, default)
```

Extracts the value associated with a key from a text string. Useful for pulling
structured information from LLM responses that contain key-value patterns.

**Parameters:**

- `text` - A string to search
- `key` - The key name to look for
- `default` - A fallback value if the key is not found (optional, defaults to
  none)

**Returns:** The extracted value, or the default if not found.

```
let value = extract_key(response_text, "answer", "unknown");
```

## extract_number

```
extract_number(text)
```

Extracts the first numeric value found in a text string.

**Parameters:**

- `text` - A string potentially containing numbers

**Returns:** The first number found, or none if no number is present.

```
let score = extract_number("The accuracy is 0.95 on this test");
// score = 0.95
```

## extract_sentiment

```
extract_sentiment(text)
```

Classifies the sentiment of a text string using simple heuristics.

**Parameters:**

- `text` - A string to analyze

**Returns:** A record with two fields:

- `"label"` - One of `"positive"`, `"negative"`, or `"neutral"`
- `"score"` - A confidence score between 0 and 1

```
let sentiment = extract_sentiment("This is a great result!");
// sentiment = {"label": "positive", "score": 0.8}
```
