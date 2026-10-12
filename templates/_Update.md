New {{Lib}} versions bring fixes and new features. Updating usually takes a couple of minutes, but some versions also need small changes in your project. This page tells you which ones.

## Step 1: Find your version and the latest one

- **Your version** is in `buildSrc/src/main/java/Versions.kt`:

  ```kotlin
  const val {{lib}} = "x.x.x"
  ```

- **The latest version** is: ![Latest version](https://img.shields.io/github/v/release/jahirfiquitiva/{{Lib}}?label=%20) (ignore the `v`).

## Step 2: Apply the changes for each version, in order

Look at the [list below](#changes-for-each-version). Starting from the version right after yours, apply each version's changes, **one version at a time**, until you reach the latest.

For example, if you're on `2.3.0` and the latest is `2.3.7`, apply `2.3.1`, then `2.3.2`, and so on. If a version isn't listed, it doesn't need any changes, so skip it.

Most entries link to a commit, a page on GitHub that shows what changed in each file. It looks like this:

<img src="https://raw.githubusercontent.com/jahirfiquitiva/dashboards-wikis/main/images/commit-diff-example.webp" width="720" alt="A commit on GitHub, with the changed files on the left, and removed lines in red and added lines in green on the right" />

- **Red** lines were removed. Delete them from your file.
- **Green** lines were added. Add them to your file.
- When only part of a line changed, that part is highlighted in a darker color.

Make the same changes in your project. You can skip changes to files you've customized with your own content, like icons, wallpapers or texts, unless the entry says otherwise.

## Step 3: Update the version number

Set `{{lib}}` in `Versions.kt` to the latest version, then click **File → Sync Project with Gradle Files** and run your app to check that everything works. 🚀

Stuck on a version? Ask in the [Discord server](https://discord.gg/78h7xgj), and mention which version you're updating from.

## Changes for each version
