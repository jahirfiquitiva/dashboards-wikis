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
| `frames/`, `kuper/`, `blueprint/` | Clones of the wiki repos. Ignored by this repo, each one has its own Git history |

### Template syntax

- `{{Lib}}` becomes `Frames`, `Kuper` or `Blueprint`. `{{lib}}` becomes the lowercase version.
- Content between `<!--only:kuper,blueprint-->` and `<!--/only-->` only shows in those wikis. Both markers go on their own line.
- Links between pages are relative, like `[Set App Name](Set-App-Name)`, so they work in every wiki.

## First-time setup

Clone the three wiki repos inside this folder:

```bash
git clone git@github.com:jahirfiquitiva/Frames.wiki.git frames
```

```bash
git clone git@github.com:jahirfiquitiva/Kuper.wiki.git kuper
```

```bash
git clone git@github.com:jahirfiquitiva/Blueprint.wiki.git blueprint
```

## Publishing a change

1. Make your change in `templates/`, `history/` or `wikis.json`, and commit it to this repo.
2. Generate the pages into the wiki clones:

   ```bash
   python3 scripts/render.py
   ```

3. Check them for broken links and style problems:

   ```bash
   python3 scripts/check.py
   ```

4. Review what changed in each wiki with `git -C frames diff` (and the same for `kuper` and `blueprint`). Most changes only touch one or two wikis.
5. Commit and push each wiki that changed.

`render.py` only writes pages, it never deletes them. If you remove a page from `wikis.json`, delete its file from the wiki clone yourself, or better, add it to `moved` so old links keep working.

To try a change without touching the wiki clones, pass `--out out` to both scripts. `out/` is ignored by Git.

### Checking file paths against the samples

To also check that every file path in the docs exists in the sample projects, clone the `sample` branches into one folder (`Frames`, `Kuper`, `Blueprint`) and pass it:

```bash
python3 scripts/check.py --samples ../samples
```
