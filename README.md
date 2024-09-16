# uv-test-coloring

Test repository for [uv #7352](https://github.com/astral-sh/uv/issues/7352)

## test Cases

Two Python versions need to be tested:

Python 3.11:
```
requires-python = ">=3.11,<3.12"
```

Python 3.12:
```
requires-python = ">=3.12,<3.13"
```

### Test Ansible Coloring

Run the commands ans check if there's a colored output:
```
uv run ansible-playbook test-playbook.yaml
```

And:
```
source .venv/bin/activate
ansible-playbook test-playbook.yaml
```

If both __don't__ have a colored output check the `curses module`.

### Curses Module

Run the script and check if the output is a __positive__ integer:

- Without an environment:
```
python3 test_curses.py
```

- With `uv run` command:
```
uv run test_curses.py
```

- With activated environment:
```
source .venv/bin/activate
python3 test_curses.py
```

- With `pipenv run` command:
```
source .venv/bin/activate
python3 test_curses.py
```
