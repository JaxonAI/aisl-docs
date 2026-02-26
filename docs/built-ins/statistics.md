# Statistics

These functions compute statistical summaries and hypothesis tests.

## mean

```
mean(list)
```

Computes the arithmetic mean of a list of numbers.

**Parameters:**

- `list` - A list of numbers

**Returns:** The mean value.

```
let avg = mean([10, 20, 30]);
// avg = 20.0
```

## median

```
median(list)
```

Computes the median (middle value) of a list of numbers.

**Parameters:**

- `list` - A list of numbers

**Returns:** The median value.

```
let mid = median([1, 3, 5, 7, 9]);
// mid = 5.0
```

## variance

```
variance(list)
```

Computes the sample variance of a list of numbers (using `ddof=1`).

**Parameters:**

- `list` - A list of numbers

**Returns:** The sample variance.

```
let v = variance([2, 4, 6, 8]);
```

## standard_deviation

```
standard_deviation(list)
```

Computes the sample standard deviation of a list of numbers.

**Parameters:**

- `list` - A list of numbers

**Returns:** The sample standard deviation.

```
let sd = standard_deviation([2, 4, 6, 8]);
```

## percentile

```
percentile(list, p)
```

Computes the p-th percentile of a list of numbers.

**Parameters:**

- `list` - A list of numbers
- `p` - Percentile value between 0 and 100

**Returns:** The value at the specified percentile.

```
let p95 = percentile(scores, 95);
let p50 = percentile(scores, 50);  // equivalent to median
```

## confidence_interval

```
confidence_interval(list, confidence_level)
```

Computes a confidence interval for the mean of a list of numbers.

**Parameters:**

- `list` - A list of numbers
- `confidence_level` - Confidence level between 0 and 1 (default: `0.95`)

**Returns:** A record with three fields:

- `"lower"` - Lower bound of the interval
- `"upper"` - Upper bound of the interval
- `"mean"` - The sample mean

```
let ci = confidence_interval(scores, 0.95);
// ci = {"lower": 0.72, "upper": 0.88, "mean": 0.80}
```

## paired_t_test

```
paired_t_test(mean_diff, std, num_samples)
```

Computes a paired t-test statistic.

**Parameters:**

- `mean_diff` - Mean of the paired differences
- `std` - Standard deviation of the paired differences
- `num_samples` - Number of paired samples

**Returns:** The t-statistic.

```
let t_stat = paired_t_test(0.05, 0.02, 100);
```

## t_test_p_value

```
t_test_p_value(t_statistic, num_samples)
```

Computes a p-value from a t-statistic.

**Parameters:**

- `t_statistic` - The t-statistic value
- `num_samples` - Number of samples (used to compute degrees of freedom)

**Returns:** The two-tailed p-value.

```
let p = t_test_p_value(t_stat, 100);
```
