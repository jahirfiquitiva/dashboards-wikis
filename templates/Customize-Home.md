The Home section is the first thing users see. You can customize it in `app/src/main/res/values/home_setup.xml`.

## Settings

| Setting | What it does | Default |
| --- | --- | --- |
| `home_actions_style` | The Share, Rate and Donate buttons: `0` hidden, `1` small, `2` big | `1` |
| `show_overview` | Shows an overview of your icon pack in the Home section | `true` |
| `show_menu_in_home_page` | Shows the menu (changelog, help, about, settings) in the Home section | `false` |
| `show_quick_apply_text` | Shows a label on the quick apply button, not only its icon | `false` |
| `quick_apply_custom_text` | Your own label for the quick apply button. Empty uses "Quick Apply". If you set it, add translations too, or it may not show in other languages | Empty |

## Your other apps

At the bottom of Home, you can list your other apps or useful links. Each one needs an item in these four lists, **in the same position**:

```xml
<string-array name="home_list_titles">
    <item>My Wallpapers</item>
</string-array>
<string-array name="home_list_descriptions">
    <item>Wallpapers that match this icon pack</item>
</string-array>
<string-array name="home_list_icons">
    <item>ic_my_wallpapers</item>
</string-array>
<string-array name="home_list_links">
    <item>https://play.google.com/store/apps/details?id=com.yourname.wallpapers</item>
</string-array>
```

| List | What goes in each item |
| --- | --- |
| `home_list_titles` | The title |
| `home_list_descriptions` | A short description |
| `home_list_icons` | The name of an icon in `drawable` or `drawable-nodpi`, without the extension |
| `home_list_links` | The link to open |

To show nothing there, delete all the items from the four lists.
