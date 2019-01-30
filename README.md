[![Build
Status](https://travis-ci.org/Nikoleta-v3/blackbook.svg?branch=master)](https://travis-ci.org/Nikoleta-v3/blackbook)

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

These both work in a given notebook session, `blackbook` will search a directory
tree and reformat the notebooks in an uncompromising way.
