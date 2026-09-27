# Anonymous modules artifact

This repository contains optimizer, target, and security-claim modules supplied
for anonymous review. Project-specific attribution, publishing automation, and
internal audit material are intentionally omitted.

## Layout

- `optimizers/`: attack strategies
- `targets/`: systems under test
- `security_claims/`: evaluation tasks and benchmarks

Each module is an independently installable Python package. Install the
companion framework artifact first, then install only the modules required for
the reviewed experiment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e /path/to/framework-artifact
pip install -e optimizers/<module>
pip install -e targets/<module>
pip install -e security_claims/<module>
```

The anonymized framework distribution and import package are both named
`anonframework`. Python 3.11 through 3.13 is supported.

## Data notice

Some modules include benchmark prompts, test records, serialized reference
hashes, and other upstream data required for faithful evaluation. These files
are intentional parts of the artifact. Generated runs, logs, credentials,
downloaded datasets, and local outputs must not be committed.
