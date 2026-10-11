The Apply section lists the launchers users can apply your icon pack to. You choose which ones show up in `app/src/main/res/values/supported_launchers.xml`:

```xml
<string-array name="supported_launchers">
    <item>action</item>
    <item>adw</item>
    <item>nova</item>
    <!-- ... -->
</string-array>
```

To hide a launcher from the list, delete its line.

> **Note**
> Don't delete the launcher `intent-filter` blocks in `AndroidManifest.xml`. Launchers use them to detect your app as an icon pack.

## Smart Launcher

Smart Launcher needs some extra files. Someone from the community wrote a [step-by-step tutorial](https://drive.google.com/file/d/0Bw52d3_ZiSb9MlpQZU1oaEpXdlk/view?usp=sharing&resourcekey=0-2hCsWZ06rsCHXaV6_IFtgA) for them. Thanks to whoever made it. 🙌
