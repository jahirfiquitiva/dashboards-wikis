{{Lib}} loads your wallpapers from a JSON file: a small text file that lists each wallpaper's name, image link and other details. You upload the file somewhere online, and {{Lib}} downloads it when the app opens. That way, you can add wallpapers without publishing an app update.

> [!TIP]
> **New to JSON?**
>
> This [short tutorial](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON) covers everything you need.

## Step 1: Write the JSON file

The file is a list (`[ ]`) of wallpapers (`{ }`), separated by commas. Each wallpaper needs at least a `name` and a `url`:

```json
[
  {
    "name": "First Wallpaper",
    "url": "https://example.com/wallpapers/first.png"
  },
  {
    "name": "Second Wallpaper",
    "author": "Jane Doe",
    "url": "https://example.com/wallpapers/second.png",
    "thumbnail": "https://example.com/wallpapers/thumbnails/second.png",
    "collections": "Abstract, Gradients",
    "downloadable": true,
    "size": 345066,
    "dimensions": "1920 x 1080 px",
    "copyright": "CC BY-SA 4.0"
  }
]
```

### All the details you can add

| Key | Required | What it is | Example |
| --- | --- | --- | --- |
| `name` | Yes | The wallpaper's name | `"First Wallpaper"` |
| `url` | Yes | Direct link to the full-size image | `"https://example.com/first.png"` |
| `author` | No | Who made it | `"Jane Doe"` |
| `thumbnail` | No | Direct link to a smaller version, used in lists so they load faster | `"https://example.com/first-small.png"` |
| `collections` | No | The collections it belongs to, separated by commas | `"Abstract, Gradients"` |
| `downloadable` | No | Whether users can download it. If you leave it out, they can | `true` or `false` |
| `size` | No | File size in **bytes** | `345066` |
| `dimensions` | No | Image size | `"1920 x 1080 px"` |
| `copyright` | No | License or copyright info | `"CC BY-SA 4.0"` |

Text goes inside quotes. `true`, `false` and numbers don't.

Some keys also accept other names, in case your JSON already uses them:

| Key | Also accepted |
| --- | --- |
| `thumbnail` | `thumbUrl`, `thumb`, `url-thumb` |
| `collections` | `categories`, `category` |
| `dimensions` | `dimension` |

> [!TIP]
> A missing comma or quote breaks the whole file. Paste your JSON into a validator like [JSONLint](https://jsonlint.com/) before uploading it.

## Step 2: Upload it and connect it

1. Upload your JSON file somewhere online and get its **direct link**: when you open it in your browser, you should see only the JSON text, not a web page around it. For example, on GitHub use the **Raw** button.
2. Open `app/src/main/res/values/frames_setup.xml` and paste the link in `json_url`:

   ```xml
   <string name="json_url">https://example.com/wallpapers.json</string>
   ```

That's it. Run the app and your wallpapers should show up. 🖼️

## Using Google Drive

You can host your wallpapers and the JSON file on Google Drive, for free. There's a catch: the link Google Drive gives you opens a web page, not the file, so the app can't use it as it is. You have to change it first.

1. Upload the file to Google Drive.
2. Right-click it, select **Share**, and under **General access** choose **Anyone with the link**. The app can only load public files.
3. Click **Copy link**. You get a link like this:

   ```
   https://drive.google.com/file/d/FILE_ID/view?usp=sharing
   ```

   `FILE_ID` is a long code that's different for every file, but it's always between `/d/` and `/view`.

4. Put that code in this link instead:

   ```
   https://drive.google.com/uc?export=download&id=FILE_ID
   ```

For example:

| Google Drive gives you | You write |
| --- | --- |
| `https://drive.google.com/file/d/1aBcD2eFgH3/view?usp=sharing` | `https://drive.google.com/uc?export=download&id=1aBcD2eFgH3` |

Do this for every link: each wallpaper's `url` and `thumbnail`, and the JSON file itself.

> [!WARNING]
> **Using a Google Drive link in `json_url`?**
>
> `frames_setup.xml` is an XML file, and in XML the `&` in the link has to be written as `&amp;`. Otherwise the build fails:
>
> ```xml
> <string name="json_url">https://drive.google.com/uc?export=download&amp;id=1aBcD2eFgH3</string>
> ```
>
> In the JSON file, write `&` as it is. See [Edit XML Files](Edit-XML-Files#special-characters) for why.

## Keep wallpapers inside the app (optional)

If you'd rather not host anything online, you can ship the JSON file and the images inside the app. The trade-off: adding wallpapers then needs an app update, and every image makes your app bigger.

1. Put the files in `app/src/main/assets`. You can use subfolders.
2. Instead of a web link, use `file:///android_asset/` followed by the file's path inside `assets`:

   | File | Link to use |
   | --- | --- |
   | `app/src/main/assets/wallpapers.json` | `file:///android_asset/wallpapers.json` |
   | `app/src/main/assets/wallpaper.jpg` | `file:///android_asset/wallpaper.jpg` |
   | `app/src/main/assets/folder/0.jpg` | `file:///android_asset/folder/0.jpg` |

3. Use these links in `json_url`, and in the `url` and `thumbnail` of each wallpaper.

Avoid spaces and special characters in file names.

You can also mix both: keep the JSON inside the app and the images online, or the other way around.

## Make your wallpapers load faster

Big images take longer to load and use more of your users' data. Compressing them usually makes them much smaller without a visible difference:

- [Squoosh](https://squoosh.app/) (in the browser)
- [TinyPNG](https://tinypng.com/) (in the browser, PNG and JPG)
- [Caesium](https://saerasoft.com/caesium) (desktop app)
- [Pngyu](https://nukesaq88.github.io/Pngyu/) (desktop app, PNG)

Adding a `thumbnail` to each wallpaper helps too: lists load the small version, and the full image only loads when someone opens it.
