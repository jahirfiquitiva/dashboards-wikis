# Dashboards wikis

The source of the [Frames](https://github.com/jahirfiquitiva/Frames/wiki), [Kuper](https://github.com/jahirfiquitiva/Kuper/wiki) and [Blueprint](https://github.com/jahirfiquitiva/Blueprint/wiki) wikis.

The three libraries share most of their setup, so most pages are written once in `templates/` and generated for each wiki. The pages are generated into clones of the three wiki repos inside this folder, and each wiki is pushed by hand.

> **Don't edit the wikis on GitHub.** The next time the pages are generated, any change made there gets overwritten. Every wiki page links back here in its footer, so open an issue or a pull request in this repo instead.

## How it's organized

| Path | What's in it |
| --- | --- |
| `templates/` | One file per page. Shared pages use placeholders and conditional blocks (see below) |
| `templates/_Update.md` | The intro of each library's update page |
| `history/<lib>.md` | The list of versions and their required changes, appended to the update page |
| `wikis.json` | Which pages each wiki gets, and the stubs for renamed pages |
| `scripts/render.py` | Generates the pages into `frames/`, `kuper/` and `blueprint/` |
| `scripts/check.py` | Checks the generated pages for broken links and style rules |
| `scripts/pull.py` | Clones the wiki repos that are missing, and pulls the ones that exist |
| `scripts/push.py` | Commits and pushes each wiki that changed, after running `check.py` |
| `scripts/preview.py` | Serves one wiki locally with Gollum, re-rendering it while you edit |
| `frames/`, `kuper/`, `blueprint/` | Clones of the wiki repos. Ignored by this repo, each one has its own Git history |

### Template syntax

- `{{Lib}}` becomes `Frames`, `Kuper` or `Blueprint`. `{{lib}}` becomes the lowercase version.
- Content between `<!--only:kuper,blueprint-->` and `<!--/only-->` only shows in those wikis. Both markers go on their own line.
- Links between pages are relative, like `[Set App Name](Set-App-Name)`, so they work in every wiki.

## First-time setup

Clone the three wiki repos inside this folder:

```bash
python3 scripts/pull.py
```

It uses SSH. Add `--https` to clone with HTTPS instead.

## Publishing a change

1. Make your change in `templates/`, `history/` or `wikis.json`, and commit it to this repo.
2. Get the latest version of each wiki, in case someone edited one on GitHub:

   ```bash
   python3 scripts/pull.py
   ```

3. Generate the pages into the wiki clones:

   ```bash
   python3 scripts/render.py
   ```

4. Preview a wiki in your browser (see [Previewing](#previewing)), and see what would be committed in each one:

   ```bash
   python3 scripts/push.py --dry-run
   ```

   For the full diff of one wiki, run `git -C frames diff` (or `kuper`, `blueprint`).

5. Commit and push:

   ```bash
   python3 scripts/push.py
   ```

   It runs `check.py` first and stops if it finds problems. Then, for each wiki that changed, it lists the changed files and asks before committing and pushing. Wikis without changes are skipped.

`pull.py` and `push.py` take wiki names to limit them to some wikis, like `python3 scripts/push.py blueprint`. `push.py` also takes `-m "message"` for a custom commit message (the default points to this repo's latest commit), and `--yes` to skip the questions.

`render.py` only writes pages, it never deletes them. If you remove a page from `wikis.json`, delete its file from the wiki clone yourself, or better, add it to `moved` so old links keep working.

To try a change without touching the wiki clones, pass `--out out` to both scripts. `out/` is ignored by Git.

## Previewing

To see a wiki the way GitHub shows it, with the sidebar, the footer and working links between pages, use [Gollum](https://github.com/gollum/gollum). Install it once:

```bash
gem install gollum
```

Then preview a wiki:

```bash
python3 scripts/preview.py frames --watch
```

Open http://localhost:4567. With `--watch`, every time you save a file in `templates/`, `history/` or `wikis.json`, the wiki is rendered again and `check.py` runs on it. Refresh the browser to see the change. `--port` changes the port.

Gollum only shows committed pages, so the script renders into `out/<lib>`, a separate Git repo ignored by this one, and commits there. Your wiki clones stay untouched, and nothing is pushed.

### Checking file paths against the samples

To also check that every file path in the docs exists in the sample projects, clone the `sample` branches into one folder (`Frames`, `Kuper`, `Blueprint`) and pass it:

```bash
python3 scripts/check.py --samples ../samples
```
