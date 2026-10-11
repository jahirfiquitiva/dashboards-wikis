The changelog tells your users what's new in each version. You write it in `app/src/main/res/xml/changelog.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <version title="v1.1.0" />
    <item text="Added 20 new wallpapers" />
    <item text="Bug fixes" />

    <version title="v1.0.0" />
    <item text="First release" />
</resources>
```

- Each `version` starts a new section with that title.
- Each `item` after it becomes a bullet point in that section.
- Versions show in the order you write them, so put the newest one first.
- Empty items (`text=""`) are ignored.

Update it every time you publish a new version. 📝
