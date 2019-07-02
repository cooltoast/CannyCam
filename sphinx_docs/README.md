Sphinx Documentation Source
====================
In this directory are the files necessary for [Sphinx](http://www.sphinx-doc.org/en/1.8/contents.html) to generate the code documentation that lives in the [docs](../docs) directory.

This directory contains:
- The Master Sphinx document: `index.rst`
- A Sphinx configuration file: `conf.py`
- A `Makefile`

Prerequesites
----------------------------
Install the docs requirements
```bash
pushd ..
virtualenv docs_env
source docs_env/bin/activate
pip install -r requirements.txt -r docs_requirements.txt
popd
```

Generating Code Documentation
-----------------------------
Trigger the `github-docs` make rule
```bash
make github-docs
```

Commit and push the `docs` directory
```bash
git add ../docs
git commit -m "<message>"
git push origin <branch>
```
