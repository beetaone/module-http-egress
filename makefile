SHELL := /bin/bash

# import config.
# You can change the default config with `make cnf="config_special.env" build`
cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

# import deploy config
# You can change the default deploy config with `make cnf="deploy_special.env" release`
dpl ?= deploy.env
include $(dpl)
export $(shell sed 's/=.*//' $(dpl))

create_image:
	docker build -t $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG) . -f image/Dockerfile
.phony: create_image

create_and_push_multi_platform:
	docker buildx build --platform linux/amd64,linux/arm,linux/arm64 -t $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG) --push . -f image/Dockerfile
.phony: create_and_push_multi_platform

push_latest:
	docker image push $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG)
.phony: push_latest

run_image:
	docker run -p 5000:80 --rm \
	--name $(MODULE_NAME) \
	--env-file=./config.env $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG)
.phony: run_image

listentest:
	make create_image
	echo "Starting module container"
	docker run --detach -p 5000:80 --rm \
	--name $(MODULE_NAME) \
	--env-file=./config.env $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG)
	echo "Waiting for 2 seconds..."
	sleep 2
	echo "Sending test payload"
	curl --header "Content-Type: application/json" \
                --request POST \
                --data '{"random hash":"f36940fb3203f6e1b232f84eb3f796049c9cf1761a9297845e5f2453eb036f01"}' \
                localhost:5000
	docker logs $(MODULE_NAME)
	echo "stopping the container..."
	docker stop $(MODULE_NAME)
	echo "Test done."

lint:
	pylint main.py app/
.phony: lint

install_local:
	pip3 install -r image/requirements.txt
.phony: install_local

run_local:
	python image/src/main.py
.phony: run_local

clean:
	docker stop $(MODULE_NAME)
	docker rmi $(ACCOUNT_NAME)/$(MODULE_NAME):$(VERSION_TAG)
.phony: clean
