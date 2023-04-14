# sceptre-json-resolver

A Sceptre resolver to serialize and deserialize json.

## Motivation

There are use cases where you may want to pass in either a string
or a json object to a cloudformation or sceptre_user_data parameter.
This simple resolver can take some json and serialize it or deserialize
it before passing it into a cloudformation parameter or a
scepter_user_data parameter.

## Installation

To install directly from PyPI
```shell
pip install sceptre-json-resolver
```

To install from this git repo
```shell
pip install git+https://github.com/Sceptre/sceptre-json-resolver.git
```

## Usage/Examples

```yaml
parameters|sceptre_user_data:
  <name>: !from_json [ <string> ]

parameters|sceptre_user_data:
  <name>: !to_json [ <json object> ]
```

## Examples

Take some json object serialize it to a string then pass it to a parameter:
```yaml
parameters:
   myparam: !to_json [{"key": "value"}]
```

Take a string deserialize it to a json object then pass it to a parameter:
```yaml
sceptre_user_data:
  myparam: !from_json ['{"key": "value"}']
```

Make a request to a REST API, deserialize the response to a json object
then pass it to a parameter:
```yaml
sceptre_user_data:
  hounds: !from_json
    - !request 'https://dog.ceo/api/breed/hound/list'
```
__NOTE__: This use case requires the nested resolver feature in
Sceptre version 4.1 and greater.
