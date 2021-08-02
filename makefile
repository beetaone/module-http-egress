SHELL := /bin/bash
MODULE=weevenetwork/webhook-egress
create_image:
	docker build -t ${MODULE} .
.phony: create_image

create_and_push_multi_platform:
	docker buildx build --platform linux/amd64,linux/arm,linux/arm64 -t ${MODULE} --push .
.phony: create_and_push_multi_platform

push_latest:
	docker image push ${MODULE}
.phony: push_latest

run_image:
	docker run -p 8000:5000 --rm ${MODULE}:latest
.phony: run_image

lint:
	pylint main.py app/
.phony: lint

install_local:
	pip3 install -r requirements.txt
.phony: install_local

run_local:
	 python main.py
.phony: run_local
