# ML Metrics

These functions compute standard machine learning evaluation metrics.

## accuracy

```
accuracy(y_true, y_pred)
```

Computes classification accuracy: the proportion of correct predictions.

**Parameters:**

- `y_true` - Array of true labels
- `y_pred` - Array of predicted labels

**Returns:** A number between 0.0 and 1.0.

```
let acc = accuracy([1, 0, 1, 1], [1, 0, 0, 1]);
// acc = 0.75
```

!!! note

    `accuracy_score` is an alias for `accuracy`.

## f1_score

```
f1_score(y_true, y_pred)
```

Computes the F1 score, the harmonic mean of precision and recall.

**Parameters:**

- `y_true` - Array of true labels
- `y_pred` - Array of predicted labels

**Returns:** A number between 0.0 and 1.0.

```
let f1 = f1_score([1, 0, 1, 1], [1, 0, 0, 1]);
```

## precision

```
precision(y_true, y_pred)
```

Computes precision: the proportion of positive predictions that are correct.

**Parameters:**

- `y_true` - Array of true labels
- `y_pred` - Array of predicted labels

**Returns:** A number between 0.0 and 1.0.

```
let prec = precision([1, 0, 1, 1], [1, 0, 0, 1]);
```

!!! note

    `precision_score` is an alias for `precision`.

## recall

```
recall(y_true, y_pred)
```

Computes recall: the proportion of actual positives that were correctly predicted.

**Parameters:**

- `y_true` - Array of true labels
- `y_pred` - Array of predicted labels

**Returns:** A number between 0.0 and 1.0.

```
let rec = recall([1, 0, 1, 1], [1, 0, 0, 1]);
```

!!! note

    `recall_score` is an alias for `recall`.

## confusion_matrix

```
confusion_matrix(y_true, y_pred)
```

Computes a multi-class confusion matrix.

**Parameters:**

- `y_true` - Array of true labels
- `y_pred` - Array of predicted labels

**Returns:** A 2D array where element `[i][j]` is the number of samples with true
label `i` predicted as label `j`.

```
let cm = confusion_matrix(ground_truth, predictions);
```

## roc_curve

```
roc_curve(y_true, y_pred)
```

Computes the Receiver Operating Characteristic (ROC) curve.

**Parameters:**

- `y_true` - Array of true binary labels
- `y_pred` - Array of predicted probabilities

**Returns:** A record with three fields:

- `"fpr"` - Array of false positive rates
- `"tpr"` - Array of true positive rates
- `"thresholds"` - Array of thresholds

```
let roc = roc_curve(labels, probabilities);
```

## brier_score_model

```
brier_score_model(y_true, y_pred)
```

Computes the Brier score (mean squared error) for probability predictions over
the entire dataset.

**Parameters:**

- `y_true` - Array of true binary labels (0 or 1)
- `y_pred` - Array of predicted probabilities

**Returns:** A single number. Lower is better; 0.0 is a perfect score.

```
let brier = brier_score_model(labels, probabilities);
```

## brier_score_element

```
brier_score_element(y_true, y_pred)
```

Computes per-element Brier scores, returning a score for each prediction.

**Parameters:**

- `y_true` - Array of true binary labels (0 or 1)
- `y_pred` - Array of predicted probabilities

**Returns:** An array of per-element squared errors.

```
let element_scores = brier_score_element(labels, probabilities);
```
