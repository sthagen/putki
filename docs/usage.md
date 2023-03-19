# Usage

Simple specialized pipeline library - probably not useful to many.

## Discovery

Given a git repository URL discover the tasks pointing to other git repositories, branches, and folders.

Convention suggests a top level `/tasks` folder to recursively collect the `tasks.yml` files defining the tasks.

The order of execution is parallel per sub folders of the `/tasks` folder and lexically sequential per tasks files entries.

The `tasks.yml` files offer the following structure:

```yaml
---
schema: https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks/index.json
tasks:
- id: wun
  source:
    path: "/local/path/to/root"
- id: two
  source:
    path: git@example.com:orga/repo
  branch: another-branch-name
  folder: local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file
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
  folder: local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file
```

The default values for the keys `branch` and `folder` are `default` and `/`respectively.
The `discover` value is assumed to be `false` per default.

The addressing is declared within a `source` object to cover two use cases:

1. For simple source addressing needs the `path` key shall be set to the local path or remote clone URL of a public repository.
2. Alternatively for more complex addressing the object `path_elements` is requireed providing the keys `protocol`, `host`, `port`, `service_root`, `user`, `token`, and `address_template` The former keys are expected to be present in the latter key value (guarded by the usual pairs of `{{` and `}}`each. Example for some on-prem server product:

```
https://username@your.needbucket.domain:7999/yourproject/repo.git
```

Could be represented as:
```yaml
---
schema: https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks/index.json
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
  folder: local/path/from/repo/root/to/folder/hosting/a/liitos/structures/file
```

The `putki`configuration provides the policy for processing upstream access credentials.

In case the executing process environment does not provide a token in the `PUTKI_MAGIC_PLACE`(derived from the task `token` key value by adding the application prefix, the processor may override the given user value with a functional local default user as fallback (using some locally available token or pass phrase).
