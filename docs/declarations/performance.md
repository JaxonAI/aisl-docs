# Performance Declarations

A performance declaration groups one or more metrics into an evaluation block.
Performance blocks are the primary way to define and collect evaluation results
in AISL.

## Syntax

```
declare PERFORMANCE_NAME as performance {
    metric[FUNCTION](ARGS) CONDITION,
    metric[FUNCTION](ARGS) CONDITION,
    ...
}
```

Each entry in a performance block is a **metric invocation** that calls a function
and optionally applies a pass/fail condition.

## Metric invocations

A metric invocation uses the `metric[...]()` syntax:

```
metric[FUNCTION_NAME](ARG1, ARG2, ...)
```

This calls the specified function with the given arguments and records the result
as a metric.

The function can be any built-in or user-defined function:

```
declare eval as performance {
    metric[accuracy](y_true, y_pred),
    metric[f1_score](y_true, y_pred),
    metric[mean](scores)
}
```

## Conditions and the ternary operator

Each metric can optionally include a condition that determines a pass/fail label.
The condition uses a comparison operator followed by the ternary operator:

```
metric[FUNCTION](ARGS) COMPARISON ? "PASS_LABEL" : "FAIL_LABEL"
```

```
declare eval as performance {
    metric[accuracy](y_true, y_pred) > 0.9 ? "Pass" : "Fail",
    metric[f1_score](y_true, y_pred) >= 0.85 ? "Acceptable" : "Needs improvement",
    metric[mean](latencies) < 2.0 ? "Fast" : "Slow"
}
```

The condition works as follows:

1. The metric function is called and its result is computed
2. The result is compared using the specified operator and threshold
3. If the comparison is true, the first string label is assigned
4. If the comparison is false, the second string label is assigned

Metrics without a condition simply record the computed value with no pass/fail
judgment:

```
metric[confusion_matrix](y_true, y_pred)
```

## Complete example

```
declare resnet as model { model_name = "resnet50" }
declare data_file as file { name = results, type = json }
declare ground_truth as dataset { data_file, key = y_true }
declare predictions as dataset { data_file, key = y_pred, model = resnet }

let y_true = argmax(ground_truth);
let y_pred = argmax(predictions);

declare model_performance as performance {
    metric[accuracy](y_true, y_pred) > 0.9 ? "Pass" : "Fail",
    metric[f1_score](y_true, y_pred) >= 0.85 ? "Pass" : "Fail",
    metric[precision](y_true, y_pred),
    metric[recall](y_true, y_pred),
    metric[confusion_matrix](ground_truth, predictions)
}
```

## Lineage tracking

Each metric invocation creates nodes in the object graph that link to its input
data and functions. This allows you to trace the provenance of every metric result
back to its source datasets and models.
