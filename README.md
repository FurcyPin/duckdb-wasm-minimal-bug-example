# Reproduction of a weird bug in duckdb-wasm


## Installation

- Run `./start_node.js` to start a local nodejs server.
- Open a browser to localhost:8001
- In the browser, open `WORKS.html`. It works.
- In the browser, open `DOES_NOT_WORK.html`. It does not work and fails with the following error:


```
Uncaught RuntimeError: null function or function signature mismatch
    at U.onMessage (async_bindings.ts:150:23)
```


The only difference between `WORKS.html` and `DOES_NOT_WORK.html` is that
they load different files. 
- `WORKS.html` loads `diff_with_201_top_cols.db`
- `DOES_NOT_WORK.html` loads `diff_with_1000_top_cols.db`

The two files were generated exactly the same way in Python, the only difference
is that `diff_with_1000_top_cols.db` contains more columns.


## Investigation

I also added a Python script to showcase that the problems seems to come
from duckdb-wasm itself, not duckdb.

It only require to have the `duckdb` Python package installed.
Personnaly I use Python Poetry but any setup (virtualenv + pip or else) should be fine.

To use it with Poetry, just run: 

- `poetry env use 3.8` 
- `poetry update` 
- `poetry run python WORKS.py` works (and loads `diff_with_201_top_cols.db`)
- `poetry run python WORKS_TOO.py` works too (and loads `diff_with_1000_top_cols.db`)
