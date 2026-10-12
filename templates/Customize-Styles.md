Beyond colors, you can change your app's fonts, the bottom navigation labels and the shape of its components. This is optional: the defaults look good.

Styles live in `app/src/main/res/values/styles.xml`. It has these styles:

| Style | Used for |
| --- | --- |
| `MyApp.SplashScreen` | The launch screen |
| `MyApp.Default` | The app, in light and dark themes |
| `MyApp.Default.Amoled` | The app, with the AMOLED dark theme |
| `MyApp.BottomNavigationView` | The bottom navigation bar |

Their Material You versions, for Android 12 and newer, are in `app/src/main/res/values/m3_styles.xml`. If you change something in one file, make the same change in the other.

> [!IMPORTANT]
> Don't change the `parent` of these styles. The app relies on them.

## Fonts

{{Lib}} uses two fonts: `customFontNormal` for regular text and `customFontBold` for titles. The sample uses Manrope.

1. Create a `font` folder in `app/src/main/res`, if it doesn't exist.
2. Add your font files (`.ttf` or `.otf`) to it. File names can only have lowercase letters, numbers and underscores.
3. In the same folder, create a **font family** XML file for each font. See [Fonts in XML](https://developer.android.com/develop/ui/views/text-and-emoji/fonts-in-xml) to learn how.
4. In every style, point both items to your **font family files**, not to the font files:

   ```xml
   <item name="customFontBold">@font/my_bold_font_family</item>
   <item name="customFontNormal">@font/my_normal_font_family</item>
   ```

These fonts apply to specific parts of the interface, not every single text in the app.

## Bottom navigation labels

`labelVisibilityMode` in `MyApp.BottomNavigationView` decides which tabs show their label:

| Value | Labels shown |
| --- | --- |
| `labeled` | All tabs |
| `selected` | Only the selected tab |
| `unlabeled` | None |
| `auto` | All tabs if there are 3 or fewer, only the selected one otherwise |

```xml
<item name="labelVisibilityMode">labeled</item>
```

## Shapes

You can change how rounded the corners of buttons, cards and other components are, in `app/src/main/res/values/shape_styles.xml` (and `m3_shape_styles.xml` for Material You):

- `cornerFamily` is either `rounded` or `cut` (diagonal corners).
- `cornerSize` points to a size in `app/src/main/res/values/dimens.xml`. Change the size there.

```xml
<item name="cornerFamily">rounded</item>
<item name="cornerSize">@dimen/cards_corner_size</item>
```

Don't rename the styles in this file, only change their items. Learn more in the [Shape theming guide](https://m2.material.io/develop/android/theming/shape).

## Going further

With Android styles and themes you can customize much more, but anything beyond this page is up to you, and we can't offer support for it. These are good places to start:

- [Styles and themes](https://developer.android.com/develop/ui/views/theming/themes)
- [Material Components theming](https://github.com/material-components/material-components-android/blob/master/docs/theming/Theming.md)
