# FOSSA Multi-Config Setup for Monorepo

This repository demonstrates how to configure and run **multiple FOSSA CLI analyses** for different parts of a monorepo using separate `.fossa.yml` files. Each config targets a specific subdirectory and reports results under a distinct project name in FOSSA.

## 🧠 Problem

In a monorepo, you might have multiple services or modules that you want to scan **independently** with different project names, paths, and policies. A single `.fossa.yml` isn’t flexible enough for this setup.

## ✅ Solution

A solution would be to define **two separate `.fossa.yml` configurations**, one for each directory we want to analyze. Each config is passed to the FOSSA CLI using the `--config` flag in a GitHub Actions workflow.

---

## 📁 Directory Layout

```
.
├── .fossa-test-1.yml
├── .fossa-test-2.yml
├── test-1/
└── test-2/
```

---

## 🔧 Config 1: `.fossa-test-1.yml`

```yaml
version: 3

project:
  id: github.com/cmboling/fossa-multi-config-for-monorepo/test-1

paths:
  only:
    - ./test-1
```

## 🔧 Config 2: `.fossa-test-2.yml`

```yaml
version: 3

project:
  id: github.com/cmboling/fossa-multi-config-for-monorepo/test-2

paths:
  only:
    - ./test-2
```

Each project is scoped to its respective subdirectory (`test-1` or `test-2`) and tracked independently in FOSSA.

---

## ⚙️ GitHub Actions Workflow

```yaml
name: FOSSA CLI Analysis
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      FOSSA_API_KEY: ${{secrets.FOSSA_API_KEY}}

    steps:
      - uses: actions/checkout@v3

      - name: Running FOSSA CLI
        run: |
          curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/fossas/fossa-cli/master/install-latest.sh | bash
          fossa --version
          fossa analyze --config ./.fossa-test-1.yml --branch test-1-branch --revision test-1-revision
          fossa analyze --config ./.fossa-test-2.yml --branch test-2-branch --revision test-2-revision
```

---

## 🔍 Result

This setup ensures:

- **Separation of concerns**: Different configs for different directories.
- **Independent tracking**: Each scan reports to a different FOSSA project.
- **Full control**: Custom paths, revision metadata, and config values for each analysis.

---

## 📎 Related Links

- [FOSSA CLI Docs](https://docs.fossa.com/docs/fossa-cli)
- [This repository](https://github.com/cmboling/fossa-multi-config-for-monorepo)
