setup: uv git_init git_add precommit_install

precommit_install:
	pre-commit install --hook-type pre-commit --hook-type pre-push

git_init:
	git init

git_add:
	git add .
	git commit -m "initial commit"

uv:
	uv sync

.PHONY: setup
