# Usage

Simple specialized pipeline library - probably not useful to many.

## Discovery

Given a git repository URL discover the tasks pointing to other git repositories, branches, and folders.

Convention suggests a top level `/tasks` folder to recursively collect the `task.yml` files defining the tasks.

The order of execution is parallel per direct sub folders of the `/tasks` folder and lexcically sequential per further descendants.
