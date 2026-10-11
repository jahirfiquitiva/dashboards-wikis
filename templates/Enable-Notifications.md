You can send notifications to your users, for example when you add new wallpapers. {{Lib}} uses [OneSignal](https://onesignal.com/) for this, together with [Firebase](https://firebase.google.com/).

This is completely optional. If you don't need notifications, skip this page.

> **Note**
> OneSignal collects some data, and you have to declare it in the "Data safety" section of your Play Store listing: your app collects "Device or other IDs". See the [OneSignal documentation](https://documentation.onesignal.com/docs/google-play-data-safety-requirements) and the [Play Console documentation](https://support.google.com/googleplay/android-developer/answer/10787469).

## Before you start

Make sure your package name is set up: see [Set Package Name](Set-Package-Name). Notifications rely on it.

## Step 1: Set up OneSignal and Firebase

Follow [OneSignal's guide](https://documentation.onesignal.com/docs/generate-a-google-server-api-key) to create a Firebase project and a OneSignal app. Write down two values:

- Your **OneSignal App ID**
- Your **Firebase Sender ID** (also called project number)

## Step 2: Add your keys

Open `buildSrc/src/main/java/OneSignal.kt` and replace both values with yours:

```kotlin
object OneSignal {
    const val appId = "your-onesignal-app-id"
    const val googleProjectNumber = "your-firebase-sender-id"
}
```

## Step 3: Turn on the code

The notifications code is already in your project, but it's turned off with comment marks. You'll remove them in four files.

Comment marks look like this:

- `//` at the start of a line turns off that one line.
- `/*` and `*/` turn off everything between them.

Each place you need to change is marked with a `TODO: Remove comment marks to enable` comment. To find them all, open **Edit → Find → Find in Files** and search for `Remove comment marks to enable`.

### `app/build.gradle`

Remove the `//` before `implementation`:

```gradle
dependencies {
    implementation(Libs.{{lib}}) {
        transitive = true
    }
    // TODO: Remove comment marks to enable
    implementation Libs.oneSignal
}
```

### `MyApplication.kt` (in your package folder)

Remove the `//` from the three `import` lines, and the `/*` and `*/` around the OneSignal code inside `onCreate`. It should end up like this:

```kotlin
import com.onesignal.OneSignal
import com.onesignal.OSNotificationReceivedEvent
import dev.jahir.frames.extensions.context.preferences

class MyApplication : FramesApplication(BuildConfig.ONESIGNAL_APP_ID) {
    override fun onCreate() {
        super.onCreate()
        OneSignal.initWithContext(this);
        OneSignal.setAppId(BuildConfig.ONESIGNAL_APP_ID);
        // ...the rest of the OneSignal code
    }
}
```

### `NotificationServiceExtension.kt` (in your package folder)

Remove the `/*` near the top and the `*/` at the end of the file.

Then check the line that imports `R`. It must use **your** package name:

```kotlin
import com.yourname.yourapp.R
```

<!--only:blueprint-->
In the Blueprint sample it says `dev.jahir.kuper.app.R`, so you need to change it.

<!--/only-->
### `app/src/main/AndroidManifest.xml`

Near the end of the file, remove the `<!--` line and the `-->` line around the OneSignal `meta-data`:

```xml
<!-- OneSignal Notifications Service -->
<meta-data android:name="com.onesignal.NotificationServiceExtension"
    android:value="${applicationId}.NotificationServiceExtension" />
```

## Step 4: Sync, build and test

1. Click **File → Sync Project with Gradle Files**.
2. Run the app on your phone or emulator and allow notifications when it asks.
3. In your OneSignal dashboard, send a test notification. It should show up on your device. 🔔

## Notification icon

The small icon in the status bar comes from `app/src/main/res/drawable/ic_notification.xml`. To use your own, replace that file with a vector drawable with the same name. Android shows it as a white silhouette, so use a simple shape.

## Common problems

**"Unresolved reference: R" in `NotificationServiceExtension.kt`**
The `import ... .R` line still points to another package. Change it to your package name, as in step 3.

**"Unresolved reference: OneSignal"**
`implementation Libs.oneSignal` in `app/build.gradle` is still commented out, or you didn't sync after removing the `//`.

**The test notification never arrives**
Check that the App ID in `OneSignal.kt` matches the one in your OneSignal dashboard, that you allowed notifications on the device, and that notifications are turned on in the app's settings.
