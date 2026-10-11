You can replace some of the images Blueprint itself uses, like the launcher logos in the Apply section or the icons in menus. This is optional.

It works by adding a file with the **same name** as Blueprint's to your own project. Android then uses yours instead.

## Launcher logos

These are the logos shown in the Apply section.

1. Find the logo you want to replace in [Blueprint's `drawable-nodpi` folder](https://github.com/jahirfiquitiva/Blueprint/tree/master/library/src/main/res/drawable-nodpi). Launcher logos start with `ic_`, like `ic_nova.png`.
2. Create your version as a 512 × 512 px PNG, with the exact same name.
3. Put it in `app/src/main/res/drawable-nodpi`.

## Interface icons

These are the small icons in menus and buttons.

1. Find the icon you want to replace in [Blueprint's `drawable` folder](https://github.com/jahirfiquitiva/Blueprint/tree/master/library/src/main/res/drawable). They start with `ic_`, like `ic_share.xml`.
2. Create your version as a 24 × 24 px SVG.
3. Convert it to a vector drawable: in Android Studio, right-click `app/src/main/res/drawable` and select **New → Vector Asset**, then choose **Local file** and pick your SVG.
4. Name it exactly like Blueprint's icon.
