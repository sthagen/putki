# Usage

Simple specialized pipeline library - probably not useful to many.

## Discovery

Given a git repository URL discover the tasks pointing to other git repositories, branches, and folders.

Convention suggests a top level `/tasks` folder to recursively collect the `tasks.yml` files defining the tasks.

The order of execution is parallel per sub folders of the `/tasks` folder and lexcically sequential per tasks files entries.

The `tasks.yml` files offer the following structure:

```yaml
---
tasks:
- wun:
    repository: /local/path/to/root
    branch: branch-name
    folder: local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file
- two:
    repository: git@example.com:orga/repo
    branch: branch-name
    folder: local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file
```
