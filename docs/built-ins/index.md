# Built-in Functions

AISL includes over 40 built-in functions that are always available without
declaration. They cover machine learning metrics, statistics, data operations,
and LLM interaction.

## Categories

| Category | Description |
|----------|-------------|
| [ML Metrics](metrics.md) | Classification and evaluation metrics |
| [Statistics](statistics.md) | Statistical aggregation and tests |
| [Information Theory](information-theory.md) | Entropy, divergence, and mutual information |
| [Consensus](consensus.md) | Voting, agreement, and frequency analysis |
| [Data Operations](data-operations.md) | Extracting, filtering, and transforming data |
| [Response Parsing](parsing.md) | Parsing and extracting values from text |
| [LLM Queries](llm.md) | Querying language models |

## Quick reference

All built-in functions are called using standard function call syntax:

```
let result = function_name(arg1, arg2, ...);
```

### ML Metrics

| Function | Description |
|----------|-------------|
| `accuracy(y_true, y_pred)` | Classification accuracy |
| `f1_score(y_true, y_pred)` | F1 score |
| `precision(y_true, y_pred)` | Precision |
| `recall(y_true, y_pred)` | Recall |
| `confusion_matrix(y_true, y_pred)` | Confusion matrix |
| `roc_curve(y_true, y_pred)` | ROC curve data |
| `brier_score_model(y_true, y_pred)` | Brier score (whole set) |
| `brier_score_element(y_true, y_pred)` | Per-element Brier scores |

### Statistics

| Function | Description |
|----------|-------------|
| `mean(list)` | Arithmetic mean |
| `median(list)` | Median value |
| `variance(list)` | Sample variance |
| `standard_deviation(list)` | Sample standard deviation |
| `percentile(list, p)` | p-th percentile |
| `confidence_interval(list, level)` | Confidence interval bounds |
| `paired_t_test(mean_diff, std, n)` | Paired t-statistic |
| `t_test_p_value(t_stat, n)` | P-value from t-statistic |

### Information Theory

| Function | Description |
|----------|-------------|
| `binary_entropy(p)` | Shannon entropy for binary probability |
| `mean_entropy(probabilities)` | Average entropy |
| `aggregate_entropy(dataset)` | Per-model, per-question entropy |
| `kl_divergence(questions, answers, aggregate)` | KL divergence |
| `symmetric_kl_divergence(answers, aggregate)` | Symmetric KL divergence |
| `mutual_information_heatmap(data)` | Mutual information between models |

### Consensus

| Function | Description |
|----------|-------------|
| `majority_vote(list)` | Most common element |
| `consensus_threshold(list, threshold)` | Consensus check |
| `mode(list)` | Statistical mode |
| `agreement_rate(list)` | Rate of the most common element |
| `unique_values(list)` | Distinct values |
| `value_counts(list)` | Frequency of each value |

### Data Operations

| Function | Description |
|----------|-------------|
| `get(data, field)` | Extract a single field |
| `get_all(data, field)` | Extract a field from all rows |
| `filter_by_key(data, key, value)` | Filter rows by field value |
| `flatten(array)` | Flatten a multi-dimensional array |
| `argmax(array)` | Index of maximum value per element |
| `convert_to_one_hot(array)` | Convert to one-hot encoding |
| `fill(value, length)` | Create array of repeated values |
| `sum(list)` | Sum of elements |
| `size(list)` | Number of elements |
| `histogram(data, question, answer)` | Frequency distribution |
| `box_plot(data, question, answer, score)` | Box plot data |

### Response Parsing

| Function | Description |
|----------|-------------|
| `parse_json(text)` | Parse a JSON string |
| `extract_key(text, key, default)` | Extract a key from text |
| `extract_number(text)` | Extract the first number |
| `extract_sentiment(text)` | Classify sentiment |

### LLM Queries

| Function | Description |
|----------|-------------|
| `query_model(model, prompt, context)` | Query a declared model |
| `llm_query(prompt, context)` | Query the default LLM |
