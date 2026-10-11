Your app's colors are set in `app/src/main/res/values/colors.xml`. Each color is a hex code, like `#3881fa`, or `#de000000` if you want transparency (the first two characters are the opacity).

The file has three groups, one per theme:

| Group | Used when | Names start with |
| --- | --- | --- |
| Light | The app uses the light theme | nothing, e.g. `accent` |
| Dark | The app uses the dark theme | `darkTheme`, e.g. `darkThemeAccent` |
| AMOLED | The dark theme with pitch black backgrounds is on | `amoledTheme`, e.g. `amoledThemeAccent` |

Set all three groups, so your app looks consistent whichever theme users pick.

## What each color is for

| Color | What it colors |
| --- | --- |
| `primary`, `primaryDark` | The top and bottom bars |
| `accent` | Buttons, selected items and other highlights |
| `surface` | Cards, sheets and dialogs. Also the launch screen background |
| `background` | The background of every screen |
| `snackbarBackgroundColor`, `snackbarTextColor`, `snackbarButtonColor` | The small messages that pop up at the bottom of the screen ([snackbars](https://m3.material.io/components/snackbar/overview)) |

Colors whose name starts with `on`, like `onAccent` or `onSurface`, are for text and icons placed **on top of** that color. Make sure they're easy to read against it.

## Material You

On Android 12 and newer, users can turn on Material You, which takes the colors from their wallpaper instead. Those colors are in `app/src/main/res/values-v31/m3_colors.xml`. You can leave that file as it is.

If you'd rather show your own colors by default, turn Material You off by default in [Change General Settings](Change-General-Settings). Users can still turn it on in the app's settings.

> **Need a hand picking colors?**
> The [Material Theme Builder](https://material-foundation.github.io/material-theme-builder/) generates a full palette from one color.
