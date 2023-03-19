# API

## Python

Example discovery:

```python
>>> import json
>>> import putki.discover as api
>>> api.root('../local_putki_tasks_wun/tasks')
'/some/where/local_putki_tasks_wun/tasks'
>>> jobs = api.tasks(api.root('../local_putki_tasks_wun/tasks'))
>>> print(json.dumps(jobs, indent=2))
{
  "schema": "https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks/index.json",
  "tasks": [
    {
      "id": "wun",
      "source": {
        "path": "/local/path/to/root"
      },
      "branch": "branch-name",
      "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
    },
    {
      "id": "two",
      "source": {
        "path": "git@example.com:orga/repo"
      },
      "branch": "another-branch-name",
      "folder": "local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file",
      "discover": true
    },
    {
      "id": "three-complicated-kind-of",
      "source": {
        "path_elements": {
          "protocol": "https://",
          "host": "example.com",
          "port": 7999,
          "user": null,
          "token": null,
          "service_root": "/some/funny/path/",
          "address_template": "{{protocol}}{{host}}:{{port}}{{service_root}}project/orga/repos/repo"
        }
      },
      "branch": "branch-name-too",
      "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
    },
    {
      "id": "fourth-complicated-kind-of",
      "source": {
        "path_elements": {
          "protocol": "https://",
          "host": "your.needbucket.domain",
          "port": 7999,
          "user": "username",
          "token": "MAGIC_PLACE",
          "service_root": "/",
          "address_template": "{{protocol}}{{user}}@{{host}}:{{port}}{{service_root}}yourproject/repo.git"
        }
      },
      "branch": "another-branch-name-too",
      "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
    }
  ]
}
```

## JSON Schema

The JSON schema is provided per <https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks/index.json>.

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
        "folder": {
          "type": "string",
          "examples": [
            "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
          ],
          "default": "/"
        },
        "discover": {
          "type": "boolean",
          "default": false
        }
      },
      "required": [
        "folder",
        "id",
        "source",
        "branch"
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
