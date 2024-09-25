PYTHON=python3
PIP=pip
POETRY=poetry
install:
    $(POETRY) install
brain-games:
    $(POETRY) run brain-games
build:
    $(POETRY) build
publish:
    $(POETRY) publish --dry--run
package-install:
    $(PIP) python3 -m pip install --user dist/*.whl
make lint:
    poetry run flake8 brain_games
