# HTTP Egress

|           |                                                                               |
| --------- | ----------------------------------------------------------------------------- |
| Name      | HTTP Egress                                                                   |
| Version   | v1.0.0                                                                        |
| DockerHub | [weevenetwork/http-egress](https://hub.docker.com/r/weevenetwork/http-egress) |
| authors   | Jakub Grzelak, Mesud Pasic                                                    |

- [HTTP Egress](#http-egress)
  - [Description](#description)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
- [Test with curl](#test-with-curl)

## Description

HTTP Egress is a module responsible for passing all input data to a specified URL or a Webhook address by HTTP ReST API.
Two ReST API methods are supported: POST an GET. If POST is chosen, then data are passed to a specified URL. If GET is chosen,
then data are passed as URL's query string parameters.

This module is containerized using Docker.

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Environment Variables   | Type   | Description                                                                                                                                                        |
| ----------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| EGRESS_WEBHOOK_URLS     | string | List of comma (,) separated HTTP addresses where data is sent.                                                                                                     |
| METHOD                  | string | ReST API request method: POST or GET.                                                                                                                              |
| LABELS                  | string | List of comma (,) separated labels to read from a previous module. Leave empty ("") to keep all data.                                                              |
| CONTENT_TYPE_JSON       | string | Determines if during request 'Content-Type': 'application/json' will be passed on in request or not, default is no                                                 |
| AUTHENTICATION_REQUIRED | enum   | Determines if during request authentication is required                                                                                                            |
| ACCESS_TOKEN            | string | If authentication is required this is the input for token, it also requires method like Basic or Bearer for example: Barer adhjaskjhjd-dsfdsfjsdkjf#42389dfsajfd== |
| AUTHENTICATION_API_KEY  | string | If we need to specify authentication X-API-TOKEN, here users can enter it                                                                                          |
| ERROR_URL               | string | If specified, the module will pass the error code, URL, and payload sent to this URL, instead of the previous module, if the HTTP request fails.                                                                   |

### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                                                                          |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                                                                   |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)                                                       |
| INGRESS_HOST          | string | Host to which data will be received                                                                  |
| INGRESS_PORT          | string | Port to which data will be received                                                                  |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |

## Dependencies

```txt
bottle
requests
```

## Input

Input to this module is JSON body single object or array of objects:

Example:

```json
{
  temperature: 15,
}
```

```json
[
  {
    temperature: 15,
  },
  {
    temperature: 21,
  },
  {
    temperature: 25,
  },
];
```

## Output

Output to this module is identical JSON body as input that is sent to a chosen endpoint.

Example:

```json
{
  temperature: 15,
}
```

```json
[
  {
    temperature: 15,
  },
  {
    temperature: 21,
  },
  {
    temperature: 25,
  },
];
```

# Test with curl

```bash
curl --header "Content-Type: application/json" \
                --request POST \
                --data '{"random hash":"f36940fb3203f6e1b232f84eb3f796049c9cf1761a9297845e5f2453eb036f01"}' \
                localhost:5000
```
