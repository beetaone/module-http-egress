# Webhook Egress

|                |                                   |
| -------------- | --------------------------------- |
| Name           | Webhook Egress                    |
| Version        | v0.0.1                            |
| Dockerhub Link | weevenetwork/webhook-egress       |
| Authors        | Jakub Grzelak                     |



- [Webhook Egress](#webhook-egress)
  - [Description](#description)
  - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
  - [Docker Compose Example](#docker-compose-example)


## Description

Webhook Egress is a module responsible for passing all input data to a specified URL or a Webhook address.
This module is containerized using Docker.


## Features

* Egress data from data service
* Send data to a specified URL and Webhook


## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

The following module configurations can be provided in a data service designer section on weeve platform:


| Name                | Environment Variables | Type    | Description                                                          |
| ------------------- | --------------------- | ------- | -------------------------------------------------------------------- |
| Egress Webhook URL  | EGRESS_WEBHOOK_URL    | string  | Webhook URL or other HTTP ReST endpoint address where data is sent.  | 

Moreover, other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.


### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
| --------------------- | ------ | -------------------------------------- |
| MODULE_NAME           | string | Name of the module                     |


## Dependencies

```txt
Flask==1.1.1
requests
python-decouple==3.4
```

## Input

Input to this module is JSON body single object or array of objects:

Example:
```node
{
  temperature: 15,
}
```

## Output

Output to this module is identical JSON body as input that is sent to a chosen endpoint.

Example:
```node
{
  temperature: 15,
}
```

## Docker Compose Example

```yml
version: "3"
services:
  webhook:
    image: weevenetwork/webhook-egress
    environment:
      MODULE_NAME: webhook
      EGRESS_WEBHOOK_URL: https://hookb.in/r1YwjDyn7BHzWWJVK8Gq
      HANDLER_PORT: 80
    ports:
      - 5000:80
```