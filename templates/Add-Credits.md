The About screen shows a card for each person behind your app. You set them up in `app/src/main/res/values/about_setup.xml`.

## How it works

The file has five lists. Each person gets one `<item>` in every list, **in the same position**. The first item of each list makes the first card, the second item makes the second card, and so on.

```xml
<resources xmlns:tools="http://schemas.android.com/tools" tools:ignore="ExtraTranslation,MissingTranslation">
    <string-array name="credits_photos" formatted="false" tools:ignore="TypographyDashes">
        <item>https://example.com/jane.png</item>
    </string-array>

    <string-array name="credits_titles">
        <item>Jane Doe</item>
    </string-array>

    <string-array name="credits_descriptions">
        <item>Designer and developer.</item>
    </string-array>

    <string-array name="credits_buttons">
        <item>Website|Instagram</item>
    </string-array>

    <string-array name="credits_links">
        <item>https://example.com|https://instagram.com/janedoe</item>
    </string-array>
</resources>
```

| List | What goes in each item |
| --- | --- |
| `credits_photos` | A direct link to the person's photo |
| `credits_titles` | Their name |
| `credits_descriptions` | A short bio |
| `credits_buttons` | Button labels, separated by `\|` |
| `credits_links` | The link for each button, separated by `\|`, in the same order as the labels |

To add a person, add one item to each of the five lists. To remove one, delete their item from each list.

## Things to check

- **Photos need a direct link** to the image file, the kind that opens only the image in your browser. Share links from Google Drive or Dropbox open a web page instead, so the photo won't load.
- **Buttons and links must match.** If a person has `Website|Instagram`, their links item needs exactly two links, in that order. Otherwise buttons open the wrong page.
