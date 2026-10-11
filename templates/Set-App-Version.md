Your app's version is set in `buildSrc/src/main/java/MyApp.kt`, next to the app ID:

```kotlin
object MyApp {
    const val appId = "com.yourname.yourapp"
    const val version = 1
    const val versionName = "1.0.0"
}
```

The sample starts with {{Lib}}'s own version numbers. Reset them for your first release.

## `version`

An internal number that Android and Google Play use to know which build is newer. Users don't see it.

- It must be a whole number, from `1` up to `2100000000`.
- It must go up with every release you upload to Google Play. Google Play rejects a build whose `version` isn't higher than the last one.

## `versionName`

The version users see, like `1.0.0` or `1.2 Beta`. It can be any text you want.

## Learn more

- [Set the application ID](https://developer.android.com/studio/build/application-id) (Android Developers)
- [Version your app](https://developer.android.com/studio/publish/versioning) (Android Developers)
