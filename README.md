[![Build Status](https://travis-ci.org/Nikoleta-v3/blackbook.svg?branch=master)](https://travis-ci.org/Nikoleta-v3/blackbook)
[![Coverage Status](https://coveralls.io/repos/github/Nikoleta-v3/blackbook/badge.svg?branch=add-coverage-badge)](https://coveralls.io/github/Nikoleta-v3/blackbook?branch=add-coverage-badge)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.2553363.svg)](https://doi.org/10.5281/zenodo.2553363)

# blackbook

`Black` for Jupyter notebooks.

## How?

```bash
$ pip install blackbook
$ blackbook .
2019-01-28 17:15:10.857 | INFO     | blackbook.__main__:main:25 - All done! 📖
2019-01-28 17:15:10.857 | INFO     | blackbook.__main__:main:27 - 1 notebooks
reformatted. 1 left unchanged.
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
