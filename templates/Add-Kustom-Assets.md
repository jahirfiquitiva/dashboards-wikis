{{Lib}} can ship your Kustom creations: KWGT widgets, KLWP live wallpapers, KLCK lock screens and komponents. Users browse them in your app and open them in the matching Kustom app.

## Step 1: Add your files

Your files go in `app/src/main/assets`, in the folder for their type:

| Folder | What goes in it | File extension |
| --- | --- | --- |
| `widgets` | KWGT widgets | `.kwgt` |
| `wallpapers` | KLWP live wallpapers | `.klwp` |
| `lockscreens` | KLCK lock screens | `.klck` |
| `komponents` | Komponents | `.komp` |

Export each file from its Kustom app and copy it into the right folder. The sample has a few examples you can use as a reference, including some with a `.zip` extension added (like `.kwgt.zip`). Both work.

Delete the sample's files, and delete any folder you don't use.

## Step 2: Turn on Kustom support

Open `app/src/main/AndroidManifest.xml` and find this block:

```xml
<!-- TODO: Remove comment marks to enable Kustom Skins
* Remove intent-filter action lines according to your needs.
* If you're not going to provide one of the options, remove its respective line.
<provider
        android:name="org.kustom.api.Provider"
        android:authorities="${applicationId}.kustom.provider"
        android:exported="true"
        tools:ignore="ExportedContentProvider">
    <intent-filter>
        <action android:name="org.kustom.provider.WALLPAPERS"/>
        <action android:name="org.kustom.provider.WIDGETS"/>
        <action android:name="org.kustom.provider.KOMPONENTS"/>
        <action android:name="org.kustom.provider.LOCKSCREENS"/>
    </intent-filter>
</provider>
-->
```

1. Delete the first three lines (the `<!-- TODO` line and the two lines starting with `*`) and the `-->` line at the end. Make sure you delete the whole comment, including the two explanation lines.
2. Delete the `action` line of every type you don't include. For example, if you only have widgets, keep only the `WIDGETS` line.

It should end up like this, for an app with only widgets:

```xml
<provider
        android:name="org.kustom.api.Provider"
        android:authorities="${applicationId}.kustom.provider"
        android:exported="true"
        tools:ignore="ExportedContentProvider">
    <intent-filter>
        <action android:name="org.kustom.provider.WIDGETS"/>
    </intent-filter>
</provider>
```

## Step 3: Describe your pack

Set your pack's name and description, and a few other options, in [Change Kustom Settings](Change-Kustom-Settings).
