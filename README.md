AISL (AI Specification Language) is a domain-specific language for specifying and evaluating AI model performance. It provides a declarative syntax for defining models, loading datasets, running evaluations, and computing metrics.

https://jaxonai.github.io/aisl-docs/

## Building

```bash
uv run zensical build --clean && uv run python scripts/remove_zensical_footer.py site
```

The second step strips the "Made with Zensical" credit from the footer. CI runs the same two steps.
