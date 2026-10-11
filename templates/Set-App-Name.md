Your app's name is set in `app/src/main/res/values/strings.xml`:

```xml
<resources>
    <string name="app_name">{{Lib}}</string>
</resources>
```

Replace `{{Lib}}` with your app's name, and leave the tags around it as they are. This is the name users see under your app icon and in the app itself.

If your app name has an `&` or an apostrophe, like "Jane's Walls", it needs to be written differently. See [Special characters](Edit-XML-Files#special-characters).
<!--only:kuper,blueprint-->

It's also used as the default name of your pack inside the Kustom apps. You can change that in [Change Kustom Settings](Change-Kustom-Settings).
<!--/only-->
