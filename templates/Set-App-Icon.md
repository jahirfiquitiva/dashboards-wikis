Your app needs two kinds of icons:

- An **adaptive icon**, used by Android 8.0 and newer. It has two layers, a foreground and a background, so each launcher can give it its own shape.
- **Legacy icons**, plain images used by older Android versions.

## The easy way: Image Asset

Android Studio can generate every icon size from one image:

1. In the Project panel, right-click `app/src/main/res` and select **New → Image Asset**.
2. Keep **Launcher Icons (Adaptive and Legacy)** selected and **ic_launcher** as the name.
3. Pick your foreground and background images, check the preview, and click **Next**, then **Finish**.

Android Studio warns you that some files will be overwritten. That's expected: they're the sample's icons.

> [!TIP]
> **New to adaptive icons?**
> The [adaptive icons guide](https://developer.android.com/develop/ui/views/launch/icon_design_adaptive) explains the sizes and safe zones.

## The manual way

If you prefer to create the files yourself, replace these.

### Adaptive icon

| Layer | Folder | File |
| --- | --- | --- |
| Foreground | `app/src/main/res/drawable-v24` | `ic_launcher_foreground.xml` |
| Background | `app/src/main/res/drawable` | `ic_launcher_background.xml` |

You can use a vector drawable (overwrite the `.xml` file) or an image (delete the `.xml` file and add a `.png` with the same name).

### Legacy icons

In `app/src/main/res` there are five folders that start with `mipmap-`. In each one, replace `ic_launcher.png` (the regular icon) and `ic_launcher_round.png` (the round icon) with your own, using these sizes:

| Folder | Icon size |
| --- | --- |
| `mipmap-mdpi` | 48 × 48 px |
| `mipmap-hdpi` | 72 × 72 px |
| `mipmap-xhdpi` | 96 × 96 px |
| `mipmap-xxhdpi` | 144 × 144 px |
| `mipmap-xxxhdpi` | 192 × 192 px |
