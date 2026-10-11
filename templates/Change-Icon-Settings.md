Icon settings live in `app/src/main/res/values/blueprint_setup.xml`. Icon request settings are in the same file: see [Set Up Icon Requests](Set-Up-Icon-Requests).

| Setting | What it does | Default |
| --- | --- | --- |
| `email` | Your email address. Users' support emails and icon requests go here. **Change it** | `someone@email.com` |
| `email_subject` | The subject of support emails | Empty (uses "*Your app name* Support") |
| `sort_icons_alphabetically` | Sorts the icons in each category alphabetically | `true` |
| `icon_name_in_grid_list` | Shows each icon's name under it in the icons list | `false` |
| `xml_drawable_enabled` | Reads your icons from `res/xml/drawable.xml` (`true`) instead of `res/values/icon_pack.xml` (`false`). See [Add Icons](Add-Icons) | `false` |
| `includes_adaptive_icons` | Set to `true` if your icon pack includes adaptive icons | `false` |
| `icons_placeholder` | An image to show while icons load. Use the image's name in `drawable`, without the extension | Empty |
| `static_icons_preview_picture` | An image to show behind the icons preview, instead of the user's wallpaper. Use the image's name in `drawable`, without the extension | Empty |
| `static_icons_preview_picture_by_default` | Uses the image above by default. Users can still switch to their wallpaper | `false` |
| `with_drawer_texts` | Shows the app name and version at the top of the side menu. Only for the [drawer navigation style](Choose-Navigation-Style) | `true` |
