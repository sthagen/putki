# Usage

Simple specialized pipeline library - probably not useful to many.

## Synopsis

```console
❯ putki

 Usage: putki [OPTIONS] COMMAND [ARGS]...

 Pipeline (Finnish: putki) - discovering and executing a specific task description.

╭─ Options ───────────────────────────────────────────────────────────────────────────────────╮
│ --version  -V        Display the application version and exit                               │
│ --help     -h        Show this message and exit.                                            │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────────────────────────────────────────────╮
│ verify       Verify the structure definition against the file system.                       │
│ version      Display the application version and exit.                                      │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Verify

Given a location that does not contain tasks files:

```console
❯ putki verify -d putki --verbose
2023-03-19T21:53:51.707890+00:00 DEBUG [git.cmd]: Popen(['git', 'rev-parse', '--show-toplevel'], cwd=/some/where, universal_newlines=False, shell=None, istream=None)
2023-03-19T21:53:51.719358+00:00 INFO [PUTKI]: Identified tasks default root at /some/where/example/basic/tasks
2023-03-19T21:53:51.719850+00:00 ERROR [PUTKI]: No tasks files found
```

Given a location that does indeed contain tasks files:

```console
❯ python -m putki verify -d example/minimal-tree/tasks/wun --verbose 2>&1 | cut -c 34-
DEBUG [git.cmd]: Popen(['git', 'rev-parse', '--show-toplevel'], cwd=/some/where, universal_newlines=False, shell=None, istream=None)
INFO [PUTKI]: Identified tasks default root at /some/where/example/basic/tasks
INFO [PUTKI]: Mapped tasks below specified root at example/minimal-tree/tasks/wun
INFO [PUTKI]: The 1 tasks files collected below specified root at example/minimal-tree/tasks/wun are:
INFO [PUTKI]: - example/minimal-tree/tasks/wun
INFO [PUTKI]: Collected the following 2 tasks from 1 tasks files:
INFO [PUTKI]: id: /wun
INFO [PUTKI]: source:
INFO [PUTKI]:   path: /local/path/to/another/root
INFO [PUTKI]: ---
INFO [PUTKI]: branch: another-branch-name
INFO [PUTKI]: discover: true
INFO [PUTKI]: id: /two
INFO [PUTKI]: source:
INFO [PUTKI]:   path: git@example.com:orga/repo
INFO [PUTKI]: target:
INFO [PUTKI]:   globs:
INFO [PUTKI]:   - structure.yml
INFO [PUTKI]:   name: structures.yml
INFO [PUTKI]:   root: local/path/from/repo/root/to/folder/that/should/host/a/liitos/structures/file
INFO [PUTKI]:
INFO [PUTKI]: OK
```

### Verification - Help

(WIP)

```console
❯ putki verify --help

 Usage: putki verify [OPTIONS] [DOC_ROOT_POS]

 Verify the structure definition against the file system.

╭─ Arguments ─────────────────────────────────────────────────────────────────────────────────╮
│   doc_root_pos      [DOC_ROOT_POS]                                                          │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ───────────────────────────────────────────────────────────────────────────────────╮
│ --document-root  -d      TEXT  Root of the document tree to visit. Optional (default:       │
│                                positional tree root value)                                  │
│ --structure      -s      TEXT  structure mapping file (default: {DEFAULT_STRUCTURE_NAME})   │
│                                [default: structure.yml]                                     │
│ --target         -t      TEXT  target document key                                          │
│ --facet          -f      TEXT  facet key of target document                                 │
│ --verbose        -v            Verbose output (default is False)                            │
│ --strict         -s            Ouput noisy warnings on console (default is False)           │
│ --help           -h            Show this message and exit.                                  │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Version

Asking for the version:

```console
❯ putki version
Pipeline (Finnish: putki) - discovering and executing a specific task description. version 2023.3.19+parent.983ce130
```

### Version - Help

For completeness:

```console
❯ putki version --help

 Usage: putki version [OPTIONS]

 Display the application version and exit.

╭─ Options ───────────────────────────────────────────────────────────────────────────────────╮
│ --help  -h        Show this message and exit.                                               │
╰─────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Discovery

Given a git repository URL discover the tasks pointing to other local or remote git repositories, branches, and folder trees.

Convention suggests a top level `/tasks` folder in the disptach repository to recursively collect the `tasks.yml` files defining the tasks.

The order of execution is parallel per sub folders of the `/tasks` folder and lexically sequential per tasks files entries.

The resulting tasks file will maintain the uniqueness of the collected ids by prefixing with a path.

Example: Collecting task with id `top` in top level tasks file as well as another task with id `top` from a tasks file at `/tasks/some/other/tasks.yml` results in the two task ids:

```yaml
- id: '/tasks/top'
- id: '/tasks/some/other/top'
```

The `tasks.yml` files offer the following example structure and shall adhere to the schema at
[/schema/1/tasks.json](https://git.sr.ht/~sthagen/putki/blob/default/schema/1/tasks.json):

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

    The former keys are expected to be present in the latter key value (each inserted between the usual pairs of `{{` and `}}`).

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
