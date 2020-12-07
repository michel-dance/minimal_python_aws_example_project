== merkle-tree ==

python3 -m pip install pytest
python3 -m pip freeze > requirements.txt

python3 -m pytest

python3 -m venv .

python3 -m pip install ./
python3 -m pip install -e ./

python3 -m pip uninstall merkle_example
