mypy --strict src && \
pylint --enable=all **/*.py && \
pytest --cov