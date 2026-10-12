This page explains where your icons and the icon pack files go, so launchers and Blueprint can find them.

It doesn't explain how to design icons or how to write each launcher's files from scratch. For that, these XDA guides are a good place to start:

- [XDA guide 1](http://forum.xda-developers.com/showthread.php?t=2291008)
- [XDA guide 2](http://forum.xda-developers.com/showthread.php?t=2668234)
- [XDA guide 3](http://forum.xda-developers.com/showthread.php?t=2399426)

The sample already has every file you need, filled with example data. The easiest way to start is to open each one, see how it's written, and replace the examples with your own.

## Step 1: Add your icons

Put your icons, as PNG files, in `app/src/main/res/drawable-nodpi`. Delete the sample icons (like `amber_circle.png` or `blue_square.png`) once yours are in.

File names can only have lowercase letters, numbers and underscores, and Blueprint uses them to show a readable name for each icon. See [Naming icons](#naming-icons).

## Step 2: Fill in the launcher files

Launchers read your icon pack from a set of XML files. Some launchers look for them in `app/src/main/assets`, others in `app/src/main/res/xml`, so some files go in both folders.

| File | `assets` | `res/xml` | Do you need to edit it? |
| --- | --- | --- | --- |
| `appfilter.xml` | Yes | Yes | Yes. It tells launchers which icon goes with which app |
| `drawable.xml` | Yes | Yes | Yes. It lists all your icons, by category |
| `appmap.xml` | | Yes | Yes |
| `theme_resources.xml` | | Yes | Yes |
| `themecfg.xml` | Yes | Yes | Yes |
| `themeinfo.xml` | Yes | Yes | Yes |
| `app_func_theme.xml` | Yes | | No, keep it as it is |
| `desk.xml` | Yes | | No, keep it as it is |
| `noshader.xml` | | Yes | No, keep it as it is |
| `themefont.ttf` | Yes | | No, it's a font file |

When a file is in both folders, it should be **exactly the same** in both. Edit one, then copy it over the other.

> [!IMPORTANT]
> **Edit every file marked "Yes"**
>
> The sample files have data from a real icon pack. If you leave them as they are, your app will show that pack's info instead of yours.

> [!NOTE]
> Some launchers, like Lawnchair, create an "All" category on their own. Don't add an "All" category to `assets/drawable.xml`, or those launchers show it twice.

## Step 3: Fill in the resource files

A few more files are in `app/src/main/res/values`:

| File | What it's for | Do you need to edit it? |
| --- | --- | --- |
| `icon_pack.xml` | The icons and categories shown inside Blueprint | Yes, see below |
| `docks.xml` | Dock backgrounds, for launchers that support them | Only if you include docks |
| `wallpapers.xml` | Wallpapers some launchers apply with your icon pack | Only if you include them |
| `bools.xml` | Launcher settings | No, keep it as it is |
| `skin_colors.xml` | Launcher colors | No, keep it as it is |

### `icon_pack.xml`

This file decides which icons Blueprint shows, and in which categories:

```xml
<!-- Icons shown in the preview on the home screen. Add at least 8 -->
<string-array name="icons_preview">
    <item>google_chrome</item>
    <item>pay__pal</item>
    <!-- ... -->
</string-array>

<!-- The categories. Each name here needs its own string-array below -->
<string-array name="icon_filters">
    <item>all</item>
    <item>google</item>
</string-array>

<!-- One string-array per category, with the icons in it -->
<string-array name="all">
    <item>google_chrome</item>
    <item>pay__pal</item>
</string-array>

<string-array name="google">
    <item>google_chrome</item>
</string-array>
```

- Each item is an icon's file name, without `.png`.
- Every name in `icon_filters` must have a `string-array` with that exact name. You can create as many categories as you want.

> [!TIP]
> Blueprint can read your icons from `res/xml/drawable.xml` instead of `icon_pack.xml`, so you only have one list to maintain. Turn on `xml_drawable_enabled` in [Change Blueprint Settings](Change-Blueprint-Settings).

### `docks.xml`

List the names of your dock images. The images go in `app/src/main/res/drawable-nodpi`, next to your icons. If you don't have docks, leave the list empty. Don't rename `dock_backgroundlist`.

```xml
<string-array name="dock_backgroundlist">
    <item>dock_a</item>
    <item>dock_b</item>
</string-array>
```

### `wallpapers.xml`

List the names of the wallpapers that go with your icon pack, and pick a default one. The images go in `app/src/main/res/drawable-nodpi`. Don't rename `wallpapers` or `default_wallpaper`.

```xml
<string-array name="wallpapers">
    <item>my_wallpaper</item>
</string-array>
<string name="default_wallpaper">my_wallpaper</string>
```

These are different from the wallpapers in the Wallpapers section of your app. Those come from a JSON file: see [Add Wallpapers](Add-Wallpapers).

## Naming icons

Blueprint turns your icon file names into readable names, following these rules:

| In the file name | Result |
| --- | --- |
| Nothing special | The first letter becomes uppercase |
| `_` (one underscore) | A space, and the next letter becomes uppercase. At the very start, it makes the first letter lowercase instead |
| `__` (two underscores) | No space, and the next letter becomes uppercase |
| `___` (three underscores) | The next word becomes all uppercase |

Some examples:

| File name | Shown as |
| --- | --- |
| `betternet.png` | Betternet |
| `google_chrome.png` | Google Chrome |
| `pay__pal.png` | PayPal |
| `_blueprint.png` | blueprint |
| `___blueprint.png` | BLUEPRINT |
| `___npr_one.png` | NPR One |
| `material___os.png` | MaterialOS |
