# Third Party Dependencies

<!--[[[fill sbom_sha256()]]]-->
The [SBOM in CycloneDX v1.4 JSON format](https://git.sr.ht/~sthagen/putki/blob/default/etc/sbom/cdx.json) with SHA256 checksum ([f72b657b ...](https://git.sr.ht/~sthagen/putki/blob/default/etc/sbom/cdx.json.sha256 "sha256:f72b657bb9d05fdf937715b4fcc913844b32833b77e16d000850d7b4b094f9c8")).
<!--[[[end]]] (checksum: 2fd0b28b2e46a12492fc643a3e732397)-->
## Licenses 

JSON files with complete license info of: [direct dependencies](direct-dependency-licenses.json) | [all dependencies](all-dependency-licenses.json)

### Direct Dependencies

<!--[[[fill direct_dependencies_table()]]]-->
| Name                                                           | Version                                              | License                 | Author                             | Description (from packaging data)                                    |
|:---------------------------------------------------------------|:-----------------------------------------------------|:------------------------|:-----------------------------------|:---------------------------------------------------------------------|
| [GitPython](https://github.com/gitpython-developers/GitPython) | [3.1.32](https://pypi.org/project/GitPython/3.1.32/) | BSD License             | Sebastian Thiel, Michael Trier     | GitPython is a Python library used to interact with Git repositories |
| [PyYAML](https://pyyaml.org/)                                  | [6.0.1](https://pypi.org/project/PyYAML/6.0.1/)      | MIT License             | Kirill Simonov                     | YAML parser and emitter for Python                                   |
| [dulwich](https://www.dulwich.io/)                             | [0.21.5](https://pypi.org/project/dulwich/0.21.5/)   | Apache Software License | Jelmer Vernooij <jelmer@jelmer.uk> | Python Git Library                                                   |
| [typer](https://github.com/tiangolo/typer)                     | [0.9.0](https://pypi.org/project/typer/0.9.0/)       | MIT License             | Sebastián Ramírez                  | Typer, build great CLIs. Easy to code. Based on Python type hints.   |
<!--[[[end]]] (checksum: 1da1ea69b1a612406b7130e60dbff30e)-->

### Indirect Dependencies

<!--[[[fill indirect_dependencies_table()]]]-->
| Name                                                                | Version                                                    | License                            | Author                                                                                | Description (from packaging data)                                      |
|:--------------------------------------------------------------------|:-----------------------------------------------------------|:-----------------------------------|:--------------------------------------------------------------------------------------|:-----------------------------------------------------------------------|
| [click](https://palletsprojects.com/p/click/)                       | [8.1.6](https://pypi.org/project/click/8.1.6/)             | BSD License                        | UNKNOWN                                                                               | Composable command line interface toolkit                              |
| [gitdb](https://github.com/gitpython-developers/gitdb)              | [4.0.10](https://pypi.org/project/gitdb/4.0.10/)           | BSD License                        | Sebastian Thiel                                                                       | Git Object Database                                                    |
| [smmap](https://github.com/gitpython-developers/smmap)              | [5.0.0](https://pypi.org/project/smmap/5.0.0/)             | BSD License                        | Sebastian Thiel                                                                       | A pure Python implementation of a sliding window memory map manager    |
| [typing_extensions](https://github.com/python/typing_extensions)    | [4.7.1](https://pypi.org/project/typing_extensions/4.7.1/) | Python Software Foundation License | "Guido van Rossum, Jukka Lehtosalo, Łukasz Langa, Michael Lee" <levkivskyi@gmail.com> | Backported and Experimental Type Hints for Python 3.7+                 |
| [urllib3](https://github.com/urllib3/urllib3/blob/main/CHANGES.rst) | [2.0.4](https://pypi.org/project/urllib3/2.0.4/)           | MIT License                        | Andrey Petrov <andrey.petrov@shazow.net>                                              | HTTP library with thread-safe connection pooling, file post, and more. |
<!--[[[end]]] (checksum: 9930fd2c09995c9a59d48b66ad984607)-->

## Dependency Tree(s)

JSON file with the complete package dependency tree info of: [the full dependency tree](package-dependency-tree.json)

### Rendered SVG

Base graphviz file in dot format: [Trees of the direct dependencies](package-dependency-tree.dot.txt)

<img src="./package-dependency-tree.svg" alt="Trees of the direct dependencies" title="Trees of the direct dependencies"/>

### Console Representation

<!--[[[fill dependency_tree_console_text()]]]-->
````console
dulwich==0.21.5
└── urllib3 [required: >=1.25, installed: 2.0.4]
GitPython==3.1.32
└── gitdb [required: >=4.0.1,<5, installed: 4.0.10]
    └── smmap [required: >=3.0.1,<6, installed: 5.0.0]
PyYAML==6.0.1
typer==0.9.0
├── click [required: >=7.1.1,<9.0.0, installed: 8.1.6]
└── typing-extensions [required: >=3.7.4.3, installed: 4.7.1]
````
<!--[[[end]]] (checksum: 16ecb075ed87a8a0366b8f1531808758)-->
