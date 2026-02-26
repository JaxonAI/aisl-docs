# Information Theory

These functions compute entropy, divergence, and mutual information measures.

## binary_entropy

```
binary_entropy(p)
```

Computes the Shannon entropy for a single binary probability.

**Parameters:**

- `p` - A probability value between 0 and 1

**Returns:** The entropy value in bits. Maximum entropy (1.0) occurs at `p = 0.5`.

```
let h = binary_entropy(0.5);   // h = 1.0 (maximum uncertainty)
let h2 = binary_entropy(0.9);  // h2 ~ 0.469
```

## mean_entropy

```
mean_entropy(probability_array)
```

Computes the average binary entropy across an array of probabilities.

**Parameters:**

- `probability_array` - An array of probability values

**Returns:** The mean entropy value.

```
let probs = [0.5, 0.9, 0.1, 0.7];
let avg_h = mean_entropy(probs);
```

## aggregate_entropy

```
aggregate_entropy(dataset)
```

Computes entropy aggregated per model and per question from a structured dataset.

**Parameters:**

- `dataset` - A structured dataset containing model responses organized by
  question

**Returns:** A record with per-model and per-question entropy breakdowns.

```
let entropy_data = aggregate_entropy(all_responses);
```

## kl_divergence

```
kl_divergence(questions, model_answers, aggregate)
```

Computes the Kullback-Leibler divergence between model answer distributions and
ground truth.

**Parameters:**

- `questions` - Array of question identifiers
- `model_answers` - Array of model response data
- `aggregate` - Whether to aggregate results (`"True"` or `"False"`, default:
  `"False"`)

**Returns:** KL divergence values. When `aggregate` is `"False"`, returns
per-question values. When `"True"`, returns a single aggregate value.

```
let kl = kl_divergence(questions, model_responses, "False");
```

## symmetric_kl_divergence

```
symmetric_kl_divergence(model_answers, aggregate)
```

Computes the symmetric KL divergence between pairs of models.

**Parameters:**

- `model_answers` - Array of model response data
- `aggregate` - Whether to aggregate results (`"True"` or `"False"`, default:
  `"False"`)

**Returns:** Symmetric KL divergence values between model pairs.

```
let skl = symmetric_kl_divergence(model_responses, "True");
```

## mutual_information_heatmap

```
mutual_information_heatmap(data)
```

Computes the mutual information between pairs of models on a per-question basis.

**Parameters:**

- `data` - A structured dataset containing model responses

**Returns:** A record suitable for generating a heatmap of pairwise mutual
information values.

```
let mi = mutual_information_heatmap(all_responses);
```
