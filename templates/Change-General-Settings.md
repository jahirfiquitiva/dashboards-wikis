General settings live in `app/src/main/res/values/dashboard_setup.xml`. The defaults work fine, so only change what you want to.

## Settings

| Setting | What it does | Default |
| --- | --- | --- |
| `toolbar_logo` | Shows an image instead of the app name in the top bar. See [Toolbar logo](#toolbar-logo) | Empty (shows the app name) |
| `notifications_enabled_by_default` | Whether notifications start turned on. Only matters if you [enable notifications](Enable-Notifications) | `true` |
| `animations_enabled_by_default` | Whether interface animations start turned on | `true` |
| `privacy_policy_link` | Link to your privacy policy, shown in the app's settings | Empty |
| `terms_conditions_link` | Link to your terms and conditions, shown in the app's settings | Empty |
| `show_versions_in_settings` | Shows your app's version and the {{Lib}} version in the app's settings | `true` |
| `default_theme` | The theme for new installs: `0` light, `1` dark, `2` follow the system | `2` |
| `amoled_theme_enabled_by_default` | Uses pitch black instead of dark gray backgrounds in the dark theme | `false` |
| `material_you_enabled_by_default` | Uses colors from the user's wallpaper on Android 12 and newer. See [Set App Colors](Set-App-Colors#material-you) | `true` |
| `donation_items` | Your donation products. See [Use Donations](Use-Donations) | Empty |

Users can change most of these later in the app's settings. These values only decide how the app starts.

> [!TIP]
> Google Play asks for a privacy policy for many apps. If you don't have one yet, a [privacy policy generator](https://app-privacy-policy-generator.firebaseapp.com/) can help you get started.

## Toolbar logo

1. Add your logo to `app/src/main/res/drawable`, for example `my_logo.png` or `my_logo.xml`.
2. Set its name, without the file extension:

   ```xml
   <string name="toolbar_logo">my_logo</string>
   ```
<!--only:frames,kuper-->
3. Open `app/src/main/res/raw/keep.xml` and add your logo to it:

   ```xml
   <resources xmlns:tools="http://schemas.android.com/tools"
       tools:keep="@drawable/my_logo" />
   ```

> [!NOTE]
> **Why `keep.xml`?**
> When you build a release, Android removes the images it thinks the app doesn't use. {{Lib}} looks up your logo by its name, so Android can't tell it's being used and removes it. Adding it to `keep.xml` prevents that. Without it, the logo shows in debug builds but disappears in the version you publish.
<!--/only-->

The logo only shows in the main section of the app.
