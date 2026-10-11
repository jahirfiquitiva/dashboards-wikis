Kustom settings live in `app/src/main/res/values/kuper_setup.xml`. Set them after you [add your Kustom assets](Add-Kustom-Assets).

| Setting | What it does | Default |
| --- | --- | --- |
| `kustom_pack_title` | Your pack's name, as shown inside the Kustom apps | Your app name (`@string/app_name`) |
| `kustom_pack_description` | A short description of what's in your pack | A sample description |
| `kolorette_required` | Set to `true` if your widgets need [Kolorette](https://play.google.com/store/apps/details?id=com.arun.themeutil.kolorette). The app then asks users to install it | `false` |
| `renoir_required` | Set to `true` if your widgets need [Renoir](https://play.google.com/store/apps/details?id=com.oh1.renoir). The app then asks users to install it | `false` |
| `kuper_preview_background` | A color to show behind your widget previews, instead of the user's wallpaper. Use a hex code like `#202020` | Empty (uses the user's wallpaper) |

For example:

```xml
<string name="kustom_pack_title">@string/app_name</string>
<string name="kustom_pack_description">Clean widgets for your home screen.</string>
<bool name="kolorette_required">false</bool>
<bool name="renoir_required">false</bool>
<color name="kuper_preview_background">#202020</color>
```
