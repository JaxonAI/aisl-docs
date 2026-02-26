# Data Operations

These functions extract, filter, transform, and aggregate data.

## get

```
get(data, field)
```

Extracts a single field from a record or structured data object.

**Parameters:**

- `data` - A record or structured data object
- `field` - A string specifying the field name

**Returns:** The value of the specified field.

```
let response = query_model(my_model, "Is AI safe?", {"topic": "safety"});
let answer = get(response, "value");
```

## get_all

```
get_all(data, field)
```

Extracts a field from each element in a list of records.

**Parameters:**

- `data` - A list of records
- `field` - A string specifying the field name to extract

**Returns:** A list of values, one from each record.

```
let responses = [
    {"value": "yes", "confidence": 0.9},
    {"value": "no", "confidence": 0.6},
    {"value": "yes", "confidence": 0.8}
];
let values = get_all(responses, "value");
// values = ["yes", "no", "yes"]
```

## filter_by_key

```
filter_by_key(data, key, value)
```

Filters a list of records, keeping only those where the specified field matches
the given value.

**Parameters:**

- `data` - A list of records
- `key` - A string specifying the field name to filter on
- `value` - The value to match against

**Returns:** A filtered list of records.

```
let high_confidence = filter_by_key(responses, "confidence", 0.9);
```

## flatten

```
flatten(array)
```

Flattens a multi-dimensional array into a one-dimensional array.

**Parameters:**

- `array` - An array (possibly multi-dimensional)

**Returns:** A flat one-dimensional array.

```
let flat = flatten([[1, 2], [3, 4]]);
// flat = [1, 2, 3, 4]
```

## argmax

```
argmax(array)
```

Returns the index of the maximum value for each element in the array. For
multi-class probability arrays, this returns the predicted class label.

**Parameters:**

- `array` - An array of values or an array of probability arrays

**Returns:** An array of indices.

```
let predictions = argmax(probability_outputs);
```

## convert_to_one_hot

```
convert_to_one_hot(array)
```

Converts an array of probability distributions to one-hot encoded vectors.

**Parameters:**

- `array` - An array of probability arrays

**Returns:** An array of one-hot vectors where only the maximum probability index
is 1.

```
let one_hot = convert_to_one_hot(probabilities);
```

## fill

```
fill(value, length)
```

Creates an array of a specified length filled with a single value.

**Parameters:**

- `value` - The value to repeat
- `length` - The number of elements

**Returns:** An array of the given length.

```
let zeros = fill(0, 10);
// zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

## sum

```
sum(list)
```

Computes the sum of all elements in a list.

**Parameters:**

- `list` - A list of numbers

**Returns:** The sum.

```
let total = sum([1, 2, 3, 4, 5]);
// total = 15
```

## size

```
size(list)
```

Returns the number of elements in a list.

**Parameters:**

- `list` - A list

**Returns:** The length as an integer.

```
let n = size([10, 20, 30]);
// n = 3
```

## histogram

```
histogram(data, question_field, answer_field)
```

Computes a frequency distribution of answers grouped by question.

**Parameters:**

- `data` - A list of records
- `question_field` - The field name containing the question identifier
- `answer_field` - The field name containing the answer value

**Returns:** A record mapping questions to answer frequency distributions.

```
let dist = histogram(responses, "question", "answer");
```

## box_plot

```
box_plot(data, question_field, answer_field, score_field)
```

Computes box plot statistics grouped by question and answer.

**Parameters:**

- `data` - A list of records
- `question_field` - The field name for question grouping
- `answer_field` - The field name for answer grouping
- `score_field` - The field name containing numeric scores

**Returns:** A list of records with box plot statistics (min, max, median,
quartiles) for each group.

```
let plots = box_plot(results, "question", "answer", "score");
```
