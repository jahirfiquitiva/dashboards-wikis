Wallpaper settings live in `app/src/main/res/values/frames_setup.xml`. The link to your wallpapers JSON is here too: see [Add Wallpapers](Add-Wallpapers).

## Settings

| Setting | What it does | Default |
| --- | --- | --- |
| `json_url` | The link to your wallpapers JSON file | The sample's JSON |
| `allow_immediate_downloads` | When `false`, users have to wait 3 hours after installing the app before they can download wallpapers. This makes it harder to install, download everything and ask for a refund | `true` |
| `downloads_on_wifi_only_enabled_by_default` | Whether downloading over Wi-Fi only starts turned on. Users can change it in the app's settings | `true` |
| `enable_colored_tiles` | Tints the footer of each wallpaper card with colors from the wallpaper, instead of a neutral color | `false` |
| `enable_filled_collection_preview` | Makes the footer of collection cards full height instead of compact | `false` |
| `show_wallpaper_palette_details` | Shows the wallpaper's main colors in its details | `true` |
| `wallpapers_placeholder` | Image shown while a wallpaper thumbnail loads. See [Placeholders](#placeholders) | Empty |
| `collections_placeholder` | Image shown while a collection thumbnail loads. See [Placeholders](#placeholders) | Empty |

## Placeholders

1. Add your images to `app/src/main/res/drawable`, for example `wallpaper_placeholder.png` and `collection_placeholder.png`.
2. Set their names, without the file extension:

   ```xml
   <string name="wallpapers_placeholder" translatable="false">wallpaper_placeholder</string>
   <string name="collections_placeholder" translatable="false">collection_placeholder</string>
   ```
<!--only:frames,kuper-->
3. Open `app/src/main/res/raw/keep.xml` and add both images, separated by a comma:

   ```xml
   <resources xmlns:tools="http://schemas.android.com/tools"
       tools:keep="@drawable/wallpaper_placeholder,@drawable/collection_placeholder" />
   ```

   Without this, the placeholders show in debug builds but disappear in the version you publish. [Change General Settings](Change-General-Settings#toolbar-logo) explains why.
<!--/only-->
