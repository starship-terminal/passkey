# Features

passkey is a read-only command-line tool that finds, parses and audits the credential stores scattered across a macOS or Linux machine, with every secret masked by default.

## Commands

- **Scan**: lists every credential store present on the machine, grouped by kind, with absent stores hidden unless you pass `--all`. Status: stable. Surface: CLI. Entry point: `passkey` or `passkey scan`. Tests: `tests/test_cli.py`, `tests/test_parsers.py`.
- **Where**: finds a provider by id, alias, display name or kind (`gcp`, `k8s`, `aws`) and prints all of its paths, present or not. Status: stable. Surface: CLI. Entry point: `passkey where <query>`. Tests: `tests/test_cli.py`, `tests/test_registry.py`.
- **Bare store name shortcut**: treats a first word that names a store as a `where` lookup, so `passkey aws` means `passkey where aws`. Status: stable. Surface: CLI. Entry point: `passkey <store>`. Tests: `tests/test_cli.py`.
- **Show**: prints every profile and field of one store with secrets masked. Status: stable. Surface: CLI. Entry point: `passkey show <store>`. Tests: `tests/test_cli.py`, `tests/test_redact.py`.
- **Reveal**: prints full secret values for one store, only when you ask for it on `show`; no other flag implies it. Status: stable. Surface: CLI. Entry point: `passkey show <store> --reveal`. Tests: `tests/test_redact.py`.
- **Paths**: prints the full registry of known credential paths as a flat table, with `--found` dropping absent paths from the table and the JSON alike. Status: stable. Surface: CLI. Entry point: `passkey paths`. Tests: `tests/test_cli.py`.
- **Doctor**: prints only problems found across all stores, each with the provider command that fixes it, and exits 1 only when a credential is provably dead. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`, `tests/test_cli.py`.
- **JSON output**: emits machine-readable output on all five verbs, with the schema documented per verb. Status: stable. Surface: CLI. Entry point: `--json`, documented in `docs/json.md`. Tests: `tests/test_cli.py`.
- **Exit codes**: returns 0 on success, 1 for a dead credential in `doctor`, 2 for no match or a bad flag, 130 on Ctrl-C, and 0 when stdout is a closed pipe. Status: stable. Surface: CLI. Entry point: `src/passkey/cli.py`. Tests: `tests/test_cli.py` covers 0 and 2; its doctor call only asserts the exit is 0 or 1 and does not force a dead credential. guessing: no test covers 130 or the closed pipe.
- **Legacy `credmap` command**: keeps the old command name working for one release and prints a one-line notice. Status: beta (unreleased, on main). Surface: CLI. Entry point: `credmap`, `python -m credmap`. Tests: `tests/test_cli.py`.

## Store discovery

- **26 built-in providers**: knows the credential paths of AWS, Google Cloud SDK, Google Application Default Credentials, Azure, DigitalOcean, Kubernetes, Docker, Terraform, Pulumi, Vault, SSH, GnuPG, GitHub CLI, Git, netrc, npm, PyPI, Cargo, Firebase, Supabase, Vercel, Fly.io, Stripe, Wrangler, Hugging Face and Claude Code. Status: stable. Surface: CLI. Entry point: `src/passkey/registry.py`, listed in `docs/stores.md`. Tests: `tests/test_parsers.py`, `tests/test_registry.py`.
- **Marker files**: counts a store as present only when a file that proves it exists, so a directory created by an editor extension is not a false positive. Status: stable. Surface: CLI. Entry point: `marker=True` in `src/passkey/registry.py`. Tests: `tests/test_registry.py`.
- **Relocated paths**: follows the environment variables that move a store (`AWS_SHARED_CREDENTIALS_FILE`, `CLOUDSDK_CONFIG`, `KUBECONFIG` as a path list, `DOCKER_CONFIG`, `GOOGLE_APPLICATION_CREDENTIALS`, `XDG_CONFIG_HOME` and others) and marks redirected paths with `←$VAR`. Status: stable. Surface: CLI. Entry point: `src/passkey/resolve.py`. Tests: `tests/test_resolve.py`, `tests/test_registry.py`.
- **Home path display**: shows paths under your home directory with `~`, without mangling a sibling directory that shares a prefix. Status: stable. Surface: CLI. Entry point: `resolve.display` in `src/passkey/resolve.py`. Tests: `tests/test_resolve.py`.
- **Keychain indirection**: reports a store whose secrets live in the OS keychain (Docker `credsStore`) as configured, with a note, instead of as empty. Status: stable. Surface: CLI. Entry point: `src/passkey/parsers.py`. Tests: `tests/test_parsers.py`, `tests/test_registry.py`.
- **Merged identities across files**: combines what a store knows about one identity from several files, such as a gcloud account and its token expiry. Status: stable. Surface: CLI. Entry point: `StoreResult.profiles` in `src/passkey/model.py`. Tests: `tests/test_parsers.py`.
- **Offline, instant scan**: runs every verb without network access or subprocesses unless `--check` is given, in roughly a tenth of a second. Status: stable. Surface: CLI. Entry point: `src/passkey/scan.py`. Tests: none (guessing: no test asserts the timing or the absence of network calls).

## Credential formats

- **Ten parsers**: reads `ini`, `inidir`, `json`, `yaml`, `sqlite-gcloud`, `netrc`, `jsondir`, `keydir`, `raw` and `opaque` stores. Status: stable. Surface: CLI. Entry point: `src/passkey/parsers.py`, documented in `docs/formats.md`. Tests: `tests/test_parsers.py`.
- **Read-only SQLite**: opens gcloud's SQLite databases read-only through a percent-quoted URI, so a scan never locks or creates a database. Status: stable. Surface: CLI. Entry point: `parse_sqlite_gcloud` in `src/passkey/parsers.py`. Tests: `tests/test_parsers.py`.
- **Broken files reported, not fatal**: shows a malformed or unreadable credential file in the scan with an error instead of aborting; the details vary by parser, but never quote the file contents. Status: stable. Surface: CLI. Entry point: `parsers.parse` in `src/passkey/parsers.py`. Tests: `tests/test_parsers.py`, `tests/test_redact.py`.
- **Partly unreadable config directories**: keeps the profiles it could read from a directory and warns with a count of the files it could not open. Status: stable. Surface: CLI. Entry point: `parse_inidir` in `src/passkey/parsers.py`. Tests: `tests/test_parsers.py`.
- **Offline expiry detection**: marks cached tokens `expired` or `valid` from expiry times stored in the files, without a network call. Status: stable. Surface: CLI. Entry point: `src/passkey/parsers.py`. Tests: `tests/test_parsers.py`.

## Secret masking

- **Fingerprint masking**: replaces each secret with its length and, from 16 characters up, its last four characters, so you can match it against a provider console. Status: stable. Surface: CLI. Entry point: `redact.mask` in `src/passkey/redact.py`. Tests: `tests/test_redact.py`.
- **Default-deny field names**: masks any field whose name looks secret even if no registry entry declared it, while keeping identifiers such as access key IDs, client IDs and projects visible. Status: stable. Surface: CLI. Entry point: `redact.is_secret` in `src/passkey/redact.py`, documented in `docs/redaction.md`. Tests: `tests/test_redact.py`, `tests/test_registry.py`.
- **Multi-line values masked**: masks any value that spans lines, whatever its field is called, so an indented secret cannot hide inside a visible field. Status: stable. Surface: CLI. Entry point: `src/passkey/redact.py`. Tests: `tests/test_redact.py`.
- **Masking text without a field name**: fingerprints token-shaped runs and caps the length of provider CLI output before it reaches you. Status: stable. Surface: CLI. Entry point: `redact.scrub_text` in `src/passkey/redact.py`. Tests: `tests/test_redact.py`, `tests/test_liveness.py`.
- **Whole-program leak test**: runs the scan, show, JSON and doctor renderers over a synthetic home and fails if any sentinel secret appears in default output. It does not cover the `paths` renderer (`render_paths`). Status: stable. Surface: CLI. Entry point: `_all_output()` in `tests/test_redact.py`. Tests: `tests/test_redact.py`.

## Doctor checks

- **Shared secret**: warns when one secret string appears in two or more profiles, because revoking it breaks all of them. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`.
- **Expired token**: warns about a cached expiry in the past, read offline. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_parsers.py`.
- **Incomplete SSO login**: warns when an AWS SSO cache registered a client but never got an access token. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`, `tests/test_parsers.py`.
- **Loose permissions**: warns when a secrets, keys or token-cache path is readable by group or others and prints a shell-quoted `chmod` fix. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`.
- **Unparsable or unreadable file**: warns when a store's file could not be parsed or some profile files could not be opened. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`.
- **Store bloat**: reports a declared directory that outgrew its threshold (gcloud logs over 500 MB), in MB or GB, with a shell-quoted cleanup command. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`.
- **Empty store**: reports a store whose marker exists but where no profiles parsed and no note explains why. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`.
- **Informational notes**: reports keychain indirection, the current kube context and similar context as info, with severity set by the parser rather than by the wording. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_doctor.py`, `tests/test_registry.py`.
- **Pre-flight exit code**: exits non-zero only on an error-level finding, which today means `--check` proved a credential dead, so an offline `doctor` never fails a script. Status: stable. Surface: CLI. Entry point: `passkey doctor`. Tests: `tests/test_cli.py`, `tests/test_doctor.py`.

## Liveness checks

- **Provider probes**: asks each provider's own CLI whether a credential still works (AWS, gcloud, Azure, kubectl, gh) and marks profiles `live`, `dead`, `no-cli` or `unknown`. Status: stable. Surface: CLI. Entry point: `--check` on `scan`, `show` and `doctor`, documented in `docs/check.md`. Tests: `tests/test_liveness.py`.
- **Missing CLI is not death**: reports `no-cli` when the provider tool is not installed instead of calling the credential dead. Status: stable. Surface: CLI. Entry point: `src/passkey/liveness.py`. Tests: `tests/test_liveness.py`.
- **Identity matching**: matches store-level probe output against identities parsed from JSON or whole words, and applies one verdict to every copy of an identity. Status: stable. Surface: CLI. Entry point: `src/passkey/liveness.py`. Tests: `tests/test_liveness.py`.
- **Probe safety limits**: runs probes without a shell, one argv element per profile name, skips names starting with `-`, keeps only 64 KiB of output, kills the process group on timeout, and stops at an overall deadline. Status: stable. Surface: CLI. Entry point: `src/passkey/liveness.py`. Tests: `tests/test_liveness.py`.

## Custom providers

- **Registry overlay**: lets you add your own credential stores, aliases, field lists, probes and bloat directories without editing the package. Status: stable. Surface: CLI. Entry point: `~/.config/passkey/registry.toml`, documented in `docs/registry-toml.md`. Tests: `tests/test_registry.py`.
- **Override built-ins**: lets an overlay entry with a built-in id change only the fields it names, drop a field with an empty value, or hide the store with `paths = []`. Status: stable. Surface: CLI. Entry point: `~/.config/passkey/registry.toml`. Tests: `tests/test_registry.py`.
- **Overlay permission guard**: refuses an overlay file or directory writable by group or others and prints one warning to stderr. Status: stable. Surface: CLI. Entry point: `src/passkey/registry.py`. Tests: `tests/test_registry.py`, `tests/test_cli.py`.
- **Broken overlay tolerated**: ignores a malformed or non-UTF-8 overlay instead of crashing every command. Status: stable. Surface: CLI. Entry point: `src/passkey/registry.py`. Tests: `tests/test_registry.py`.
- **Legacy overlay location**: reads `~/.config/credmap/registry.toml` when the new passkey file is absent. Status: beta (unreleased, on main). Surface: CLI. Entry point: `src/passkey/registry.py`. Tests: `tests/test_registry.py`.

## Install and release

- **Nix flake**: installs passkey as a flake input or with `nix run`, and runs the test suite during `nix build`. Status: stable. Surface: CLI. Entry point: `flake.nix`, documented in `docs/install.md`. Tests: none (CI builds it in the `nix` job of `.github/workflows/ci.yml`).
- **Install from a checkout**: puts `passkey` on your PATH with `uv tool install .`. Status: stable. Surface: CLI. Entry point: `pyproject.toml`. Tests: none (CI smoke-tests the built wheel in the `package` job of `.github/workflows/ci.yml`).
- **GitHub release workflow**: runs the suite on a version tag, checks the tag against both version literals, and attaches the sdist and wheel to a GitHub release. Status: stable. Surface: job. Entry point: `.github/workflows/release.yml`. Tests: none.
- **Continuous integration**: runs tests on Linux and macOS with Python 3.11 and 3.13, plus coverage, lint, wheel smoke test and nix build jobs. Status: stable. Surface: job. Entry point: `.github/workflows/ci.yml`. Tests: none.
- **Reference documentation**: documents every verb, flag, exit code, store, JSON field, masking rule and the security model. Status: stable. Surface: docs. Entry point: `docs/README.md`. Tests: none.

## Planned

- **PyPI publishing**: publishes `passkey` to PyPI with Trusted Publishing so `uv tool install passkey` works; the job exists but stays switched off until the repository goes public. Status: planned. Surface: job. Entry point: `publish` job in `.github/workflows/release.yml`, described in `docs/releasing.md`. Tests: none.
- **First release under the passkey name**: cuts a tagged release that ships the `passkey` command, so Nix users can pin a tag instead of the default branch. Status: planned. Surface: CLI. Entry point: `docs/install.md`, `CHANGELOG.md` (Unreleased). Tests: none.
- **Removal of the `credmap` command**: drops the `credmap` console script after one release. Status: planned. Surface: CLI. Entry point: `CHANGELOG.md` (Unreleased), `AGENTS.md`. Tests: none.
