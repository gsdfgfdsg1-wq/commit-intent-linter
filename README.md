# commit-intent-linter

A dependency-free CI linter that checks conventional commit intent against changed files, tests, and API impact.

## Quick start

```bash
python lint.py commit.json
```

Commit metadata includes a conventional `subject`, file paths, test evidence, and an optional `breaking_api` flag. The linter flags docs commits containing code, untested feature/fix commits, unmarked breaking changes, and chores that modify product source.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
