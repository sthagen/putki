# API

## Python

Example discovery:

```python
>>> import json
>>> import putki.discover as api
>>> api.root('~/d/bb/dilettants/src/mit/')
'/some/where/d/bb/dilettants/src/mit/tasks'
>>> task_map = api.tasks(api.root('~/d/bb/dilettants/src/mit/'))
>>> tasks = api.combine(task_map)
>>> print(json.dumps(tasks, indent=2))
[
  {
    "id": "/wun",
    "source": {
      "path": "/local/path/to/root"
    }
  },
  {
    "id": "/wun/wun",
    "source": {
      "path": "/local/path/to/another/root"
    }
  },
  {
    "id": "/wun/two",
    "source": {
      "path": "git@example.com:orga/repo"
    },
    "branch": "another-branch-name",
    "target": {
      "root": "local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file",
      "name": "structures.yml",
      "globs": [
        "structure.yml"
      ]
    },
    "discover": true
  }
]
```

## JSON Schema

The JSON schema is provided per [/schema/1/tasks.json](https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks.json).

As a service to the user it is stated below:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema#",
  "type": "object",
  "$defs": {
    "schema": {
      "description": "The URI of the JSON schema corresponding to the version.",
      "type": "string",
      "format": "uri"
    },
    "path_type": {
      "type": "string",
      "examples": [
        "git@example.com:orga/repo"
      ]
    },
    "path_elements_type": {
      "type": "object",
      "properties": {
        "protocol": {
          "type": "string",
          "examples": [
            "https://"
          ],
          "default": ""
        },
        "host": {
          "type": "string",
          "examples": [
            "your.needbucket.domain"
          ],
          "default": ""
        },
        "port": {
          "type": "string",
          "default": ""
        },
        "user": {
          "type": "string",
          "examples": [
            "username"
          ],
          "default": ""
        },
        "token": {
          "type": "string",
          "examples": [
            "MAGIC_PLACE"
          ],
          "default": ""
        },
        "service_root": {
          "type": "string",
          "examples": [
            "/"
          ],
          "default": ""
        },
        "address_template": {
          "type": "string",
          "examples": [
            "{{protocol}}{{user}}@{{host}}:{{port}}{{service_root}}yourproject/repo.git"
          ],
          "default": ""
        }
      }
    },
    "target_type": {
      "type": "object",
      "properties": {
        "root": {
          "type": "string",
          "examples": [
            "local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file"
          ],
          "default": ""
        },
        "name": {
          "type": "string",
          "examples": [
            "structures.yml"
          ],
          "default": "structures.yml"
        },
        "globs": {
            "type": "array",
            "minItems": 0,
            "items": {
                "type": "string",
                "examples": [
                  "structure.yml"
                ],
                "default": "structure.yml"
            }
        }
      }
    },
    "task_type": {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "examples": [
            "wun"
          ]
        },
        "source": {
          "type": "object",
          "oneOf": [
            {
              "$ref": "#/$defs/path_type"
            },
            {
              "$ref": "#/$defs/path_elements_type"
            }
          ]
        },
        "branch": {
          "type": "string",
          "examples": [
            "branch-name"
          ],
          "default": "default"
        },
        "target": {
          "$ref": "#/$defs/target_type"
        },
        "discover": {
          "type": "boolean",
          "default": false
        }
      },
      "required": [
        "id",
        "source"
      ]
    },
    "tasks_type": {
      "type": "array",
      "minItems": 0,
      "items": {
        "$ref": "#/$defs/task_type"
      }
    },
    "source_type": {
      "type": "object",
      "oneOf": [
        {
          "$ref": "#/$defs/path_type"
        },
        {
          "$ref": "#/$defs/path_elements_type"
        }
      ]
    }
  },
  "properties": {
    "schema": {
      "$ref": "#/$defs/schema"
    },
    "tasks": {
      "$ref": "#/$defs/tasks_type"
    }
  },
  "required": [
    "tasks"
  ],
  "additionalProperties": false
}
```
