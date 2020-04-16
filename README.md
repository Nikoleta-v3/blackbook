[![Build Status](https://travis-ci.org/Nikoleta-v3/blackbook.svg?branch=master)](https://travis-ci.org/Nikoleta-v3/blackbook)
[![GitHub Actions Status: CI](https://github.com/Nikoleta-v3/blackbook/workflows/CI/CD/badge.svg)](https://github.com/Nikoleta-v3/blackbook/actions?query=workflow%3ACI%2FCD+branch%3Amaster)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2553363.svg)](https://doi.org/10.5281/zenodo.2553363)

# blackbook

`Black` for Jupyter notebooks.

## How?

```bash
$ pip install blackbook
$ blackbook .
2019-01-28 17:15:10.857 | INFO     | blackbook.__main__:main:31 - All done! 📖
2019-01-28 17:15:10.857 | INFO     | blackbook.__main__:main:33 - 1 notebooks reformatted. 1 left unchanged.
```

You can also run `blackbook` over a single notebook

```bash
$ blackbook unformatted.ipynb
2019-01-28 17:15:12.663 | INFO     | blackbook.__main__:main:31 - All done! 📖
2019-01-28 17:15:12.663 | INFO     | blackbook.__main__:main:33 - 1 notebooks reformatted. 0 left unchanged.
```

## Why?

From [`black`](https://github.com/ambv/black):

> Black is the uncompromising Python code formatter. By using it, you agree to
> cede control over minutiae of hand-formatting. In return, Black gives you
> speed, determinism, and freedom from pycodestyle nagging about formatting. You
> will save time and mental energy for more important matters.

There are two `black` implementations for Jupyter notebooks:

- https://github.com/csurfer/blackcellmagic
- https://github.com/tobinjones/jupyterlab_formatblack
- https://github.com/betatim/joli

These both work in a given notebook session, `blackbook` will search a directory
tree and reformat the notebooks in an uncompromising way.
