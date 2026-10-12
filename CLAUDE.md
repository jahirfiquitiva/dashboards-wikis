# Dashboards wiki

Source of the Frames, Kuper and Blueprint wikis, published as `jahirfiquitiva/dashboards-wikis`. See `README.md` for how pages are generated and published.

## How the libraries relate

Frames is the base library. Kuper builds on Frames and adds Kustom support. Blueprint builds on both and adds icon packs. A feature that comes from Frames must read the same in all three wikis, so it belongs in a shared template, not in three copies.

## Editing rules

- Edit `templates/`, `history/` and `wikis.json` only. Never edit `frames/`, `kuper/`, `blueprint/` or `out/` directly: they're generated.
- `frames/`, `kuper/` and `blueprint/` are separate Git repos (the wiki clones), ignored by this one. Never commit or push to them, and never run `scripts/push.py`. You can run `scripts/pull.py`, `scripts/push.py --dry-run` and `scripts/preview.py`. Generate the pages, run the checks, and leave reviewing, committing and pushing to the maintainer.
- If a page only differs for one library, use an `<!--only:...-->` block inside the shared template instead of creating a separate page.
- Renaming or deleting a page: add the old name to `moved` in `wikis.json` so it becomes a stub. Old links from READMEs, Discord and blog posts must keep working.
- A new page needs an entry in `pages` in `wikis.json` and a link in `templates/_Sidebar.md`.
- After every change, run `python3 scripts/render.py` and `python3 scripts/check.py`. Both must pass.

## Checking facts

Readers copy what the wiki says, so every file path, setting name and default must match the current `sample` branch of the library (`https://github.com/jahirfiquitiva/<Lib>/tree/sample`). Library behavior is on the `master` branch, in `library/src/main`.

- Read the sample file before documenting a setting. Copy defaults from it, never from memory or an older page.
- Never point to line numbers. They change with every release. Point to the `TODO` comment or quote the code to look for.
- If you couldn't verify something, say so when reporting the change instead of guessing.

## Adding a version to an update page

Add it at the top of `history/<lib>.md`:

```markdown
### v2.7.0

Apply the changes in [this commit](https://github.com/jahirfiquitiva/Kuper/commit/<sha>).
```

Only add an entry when the version needs changes in users' projects. When a new major version comes out, move the previous major's entries into the `<details>` block at the bottom.

## Images

- Images go in `images/` as WebP, at twice their display width, quality 85. See "Adding an image" in `README.md` for the command.
- Link them with `https://raw.githubusercontent.com/jahirfiquitiva/dashboards-wikis/main/images/<name>`, with a `width` and an `alt` that describes what the image shows.
- Never link images uploaded to GitHub issues or comments. They can't be compressed or replaced later.

## Every page

Readers are often first-time Android developers. Write for someone who has never opened Android Studio.

1. Start with one or two sentences: what this sets up, and which file it lives in.
2. Mark optional pages as optional in the first lines.
3. Steps are numbered `## Step N: ...` sections when order matters.
4. Settings go in a table: `Setting | What it does | Default`.
5. Show the code to change, with realistic example values (`com.yourname.yourapp`, `Jane Doe`), not the sample's.
6. End with `## Common problems` when people actually get stuck on that page. Name the exact error message, then the fix.
7. Link to the related page instead of repeating its content.

## Writing style

- Casual and friendly, in second person ("you"). Write like you're explaining it to a friend sitting next to you.
- Plain language. Short sentences, one idea each. If a word needs a second read, use a simpler one.
- Explain *why* when a step looks pointless, in one sentence. For example, why the app ID and the Kotlin package must match.
- Name the UI exactly as Android Studio shows it, in bold: **File → Sync Project with Gradle Files**.
- USA spelling: color, customize, behavior, optimize, license, favorite.
- Emojis only in headings or friendly moments (a welcome, finishing a setup). At most one per line, and not on every page. `scripts/check.py` enforces the one-per-line limit.
- A button or setting *becomes* a state ("the logo becomes visible"), it doesn't do it to itself.
- Never use:
  - em dashes or en dashes
  - "drop" as a verb. Say what happens: delete, remove, leave out.
  - "handle", "address", "deal with" when you can name the actual action
  - hype words: "awesome", "blazing fast", "game-changer"
  - "simply" and "just" before an instruction that isn't simple for a beginner
- Notes use [GitHub alerts](https://github.com/orgs/community/discussions/16925): `> [!TYPE]` on its own line, then the text on the next lines, each starting with `>`. Pick the type by what the note says:
  - `[!CAUTION]`: something that can't be undone, like changing the package name after publishing.
  - `[!WARNING]`: something that breaks the app, or isn't supported.
  - `[!IMPORTANT]`: a step or rule readers must not skip.
  - `[!TIP]`: optional help, like "New to JSON?" links.
  - `[!NOTE]`: anything else.
  A note that needs a title puts it in bold on the first line after `> [!TYPE]`, then an empty `>` line, then the text. Without the empty line, GitHub joins the title and the text into one line. Don't add emojis to alerts, they have their own icons.
- "Common problems" is a list. Each item is the problem in bold, a blank line, then the fix indented by two spaces:

  ```markdown
  - **"Unresolved reference: R"**

    The `import ... .R` line still points to another package.
  ```
