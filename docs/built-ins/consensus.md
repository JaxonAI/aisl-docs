# Consensus

These functions analyze agreement, voting patterns, and frequency distributions
across collections of responses.

## majority_vote

```
majority_vote(list)
```

Returns the most common element in a list.

**Parameters:**

- `list` - A list of values

**Returns:** The value that appears most frequently.

```
let winner = majority_vote(["yes", "no", "yes", "yes", "no"]);
// winner = "yes"
```

## consensus_threshold

```
consensus_threshold(list, threshold)
```

Checks whether the most common element in a list meets a frequency threshold.

**Parameters:**

- `list` - A list of values
- `threshold` - A number between 0 and 1 (default: `0.5`)

**Returns:** A record with three fields:

- `"consensus"` - Boolean indicating if the threshold is met
- `"value"` - The most common element
- `"frequency"` - The frequency of the most common element

```
let result = consensus_threshold(responses, 0.8);
// result = {"consensus": true, "value": "yes", "frequency": 0.85}
```

## mode

```
mode(list)
```

Returns the statistical mode (most frequent value) of a list.

**Parameters:**

- `list` - A list of values

**Returns:** The most frequent value.

```
let m = mode([1, 2, 2, 3, 3, 3]);
// m = 3
```

## agreement_rate

```
agreement_rate(list)
```

Computes the frequency of the most common element as a proportion of the total
list length.

**Parameters:**

- `list` - A list of values

**Returns:** A number between 0.0 and 1.0.

```
let rate = agreement_rate(["yes", "yes", "no", "yes"]);
// rate = 0.75
```

## unique_values

```
unique_values(list)
```

Returns the distinct values in a list, preserving their order of first
appearance.

**Parameters:**

- `list` - A list of values

**Returns:** A list of unique values.

```
let uniq = unique_values(["a", "b", "a", "c", "b"]);
// uniq = ["a", "b", "c"]
```

## value_counts

```
value_counts(list)
```

Counts the frequency of each distinct value in a list.

**Parameters:**

- `list` - A list of values

**Returns:** A record mapping each value to its count.

```
let counts = value_counts(["yes", "no", "yes", "yes"]);
// counts = {"yes": 3, "no": 1}
```
