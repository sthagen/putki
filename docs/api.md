# API

Example discovery:

```python
>>> import json
>>> import putki.discover as api
>>> api.root('../local_putki_tasks_wun/tasks')
'/some/where/local_putki_tasks_wun/tasks'
>>> jobs = api.tasks(api.root('../local_putki_tasks_wun/tasks'))
>>> print(json.dumps(jobs, indent=2))
{
  "/some/where/local_putki_tasks_wun/tasks/wun": [
    {
      "wun": {
        "repository": "/local/path/to/root",
        "branch": "branch-name",
        "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
      }
    },
    {
      "two": {
        "repository": "git@example.com:orga/repo",
        "branch": "branch-name", 
        "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file"
      }
    }
  ],
  "/some/where/local_putki_tasks_wun/tasks/two": [
    {
      "three": {
        "repository": "/local/path/to/root/numba/three",
        "branch": "branch-name-three",
        "folder": "local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file-three"
      }
    }
  ]
}
```
