> **⚠️ Legacy**
> Current versions of {{Lib}} don't support Zooper widgets: the sample project no longer includes the Zooper folders or the Zooper code. This page is kept only for people maintaining an app on an old version. For new apps, use [Kustom assets](Add-Kustom-Assets) instead.

In old versions, Zooper widgets were set up like this.

## Add your files

Zooper widgets need files in four folders inside `app/src/main/assets`: `bitmaps`, `fonts`, `iconsets` and `templates`. Copy your widget files into the matching folders.

## Turn on Zooper support

In `app/src/main/AndroidManifest.xml`, remove the comment marks (`<!--` and `-->`) around these two blocks:

```xml
<!-- TODO: Remove comment marks to enable Zooper
<intent-filter>
    <action android:name="org.zooper.zw.TEMPLATES"/>
</intent-filter>
-->
```

```xml
<!-- TODO: Remove comment marks to enable Zooper
<provider
    android:name=".zooper.TemplateProvider"
    android:authorities="${applicationId}.zwprovider"
    tools:ignore="ExportedContentProvider"/>
-->
```

## Paid apps

Google Play encrypts paid apps, which breaks how Zooper reads iconsets. To avoid that, keep each iconset both zipped and unzipped. For an iconset called `WeatherIcons.zip`:

1. Copy `WeatherIcons.zip` to `assets/iconsets/`.
2. Create a folder called `WeatherIcons` in `assets/iconsets/`.
3. Extract the contents of `WeatherIcons.zip` into that folder.
4. Keep both the zip and the folder.
