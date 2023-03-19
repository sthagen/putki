# Usage

Simple specialized pipeline library - probably not useful to many.

## Discovery

Given a git repository URL discover the tasks pointing to other local or remote git repositories, branches, and folder trees.

Convention suggests a top level `/tasks` folder in the disptach repository to recursively collect the `tasks.yml` files defining the tasks.

The order of execution is parallel per sub folders of the `/tasks` folder and lexically sequential per tasks files entries.

The resulting tasks file will maintain the uniqueness of the collected ids by prefixing with a path.

The `tasks.yml` files offer the following example structure and shall adhere to the schema at
<https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks.json>:

```yaml
---
schema: https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks.json
tasks:
- id: wun
  source:
    path: "/local/path/to/root"
- id: two
  source:
    path: git@example.com:orga/repo
  branch: another-branch-name
  target:
    root: local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file
    name: structures.yml
    globs:
    - structure.yml
  discover: true
- id: three-complicated-kind-of
  source:
    path_elements:
      protocol: https://
      host: example.com
      port: 7999
      user:
      token:
      service_root: "/some/funny/path/"
      address_template: "{{protocol}}{{host}}:{{port}}{{service_root}}project/orga/repos/repo"
  branch: branch-name-too
```

The default values for the key `branch` is `default`.
The `discover` value is assumed to be `false` per default.

The addressing is declared within a `source` object to cover two use cases:

1. For simple source addressing needs the `path` key shall be set to the local path or remote clone URL of a public repository.
2. Alternatively for more complex addressing the object `path_elements` is requireed providing the keys `protocol`, `host`, `port`, `service_root`, `user`, `token`, and `address_template`.

    The former keys are expected to be present in the latter key value (guarded by the usual pairs of `{{` and `}}`each.

As an example for the second use case some on-prem server product ...
```
https://username@your.needbucket.domain:7999/yourproject/repo.git
```

... could be represented as:
```yaml
---
schema: https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks.json
tasks:
- id: fourth-complicated-kind-of
  source:
    path_elements:
      protocol: https://
      host: your.needbucket.domain
      port: 7999
      user: username
      token: MAGIC_PLACE
      service_root: "/"
      address_template: "{{protocol}}{{user}}@{{host}}:{{port}}{{service_root}}yourproject/repo.git"
  branch: another-branch-name-too
```

The `putki`configuration provides the policy for processing upstream access credentials.

In case the executing process environment does not provide a token in the `PUTKI_TOKEN_MAGIC_PLACE`(derived from the task `token` key value by adding the `PUTKI_TOKEN_` prefix, the processor may override the given user value with a functional local default user as fallback (using some locally available token or pass phrase).

The `target` object caters the use case when the targeted locations deviate from the convention to
offer a `structures.yml` file in the top level directory of the folder tree that points to the
individual `structure.yml` files within the tree.

The expectation is that these files provide structural information that the tools
[`navigaattori`](https://pypi.python.org/pypi/navigaattori/) and [`liitos`](https://pypi.python.org/pypi/liitos/) understand.
