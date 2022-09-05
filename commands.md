# High level commands
High level commands are commands composed of low level commands. These commands
are intended for user interaction through stdin/stdout.

## add
## build
## clean
## commit
## download
## help
## info
## pretty
## remove
## search
## show
## status
## update
## validate

# Low level commands
Low level commands are intended for internal use or use by expert users. These
commands should do only one thing, and it should do it well. These commands are
also non interactive, meaning that they are a good choice for use by other
scripts or programs. Low level commands can be accessed by using the
`--low-level` top level option.

## add-module
`cfbs add-module [--help] --name NAME --index INDEX`

This command adds exactly one module specified by `NAME` to `cfbs.json` from an
index specified by `INDEX` which can be a file path or url.

## list-modules
`cfbs list-modules [--help] --index INDEX`

This command lists full names and aliases of modules available in an index
specified by `INDEX` which can be a file path or url.

## list-dependencies
`cfbs list-dependencies [--help] --name NAME --index INDEX`

This command recursivly looks for dependencies of a module specified by `NAME`
from an index specified by `INDEX` which can be a file path or url.
Dependencies are listed to stdout.

## git-clone
`cfbs git-clone [--help] <repository> <directory>`

This command clones a git repository specified by `repository` into a directory specified by `directory`.

## fetch-archive
`cfbs fetch-archive [--help] --achive archive --directory direcotry`

This command fetches an archive specified by `archive` into a directory specified by `directory` which can be a file path or url.

## resolve-alias
`cfbs resolve-alias [--help] --alias ALIAS --index INDEX`

This command resolves the full name of an alias specified by `ALIAS` in an index
specified by `INDEX` which can be a file path or url.

## module-exists
`cfbs module-exists [--help] --name NAME --index INDEX`

This command checks whether or not a module specified by `NAME` exists in an
index specified by `INDEX` which can be a filepath or url.

## get-index
`cfbs get-index [--help] [--name NAME]`
