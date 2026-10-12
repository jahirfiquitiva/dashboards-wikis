Your package name is your app's unique ID, like `com.yourname.yourapp`. Android and Google Play use it to tell your app apart from every other app.

The sample uses `dev.jahir.{{lib}}.app`. You have to change it, because Google Play only allows one app per package name and that one is already taken.

This is the step people struggle with the most, so it's worth going slowly. Follow the steps in order and your app will build at the end. 💪

> [!CAUTION]
> Once you publish your app, you can't change its package name. Google Play treats a new package name as a completely different app.

## What you're going to change

The package name lives in two places, and **both have to be exactly the same**:

1. **The app ID** in `buildSrc/src/main/java/MyApp.kt`. This is what Android and Google Play see.
2. **The Kotlin package** of the 4 files in `app/src/main/kotlin/`. This is the folder they live in, plus the `package` line at the top of each file.

If they don't match, the app either doesn't build, or it builds and then crashes as soon as you open it. That's because:

- `AndroidManifest.xml` points to `.MainActivity` and `.MyApplication`. Android completes the leading `.` with your app ID, so it looks for `com.yourname.yourapp.MainActivity`. If the file is still in the old package, Android can't find it.
- Android Studio generates the `BuildConfig` and `R` classes in your app ID's package. Your Kotlin files can only use them without an `import` if they're in that same package.

## Before you start

- **Pick your package name.** It should look like `com.yourname.yourapp`:
  - It needs at least two parts separated by dots.
  - Each part must start with a letter.
  - Use only lowercase letters, numbers and underscores.
  - Don't use `dev.jahir`. That one belongs to the sample.
- **Run the sample once** without changing anything (see [Get Started](Get-Started)). If the untouched sample doesn't build, the problem is your setup, not this step.
- **If you use Git**, commit now, so you can go back if something goes wrong.

In the steps below, replace `com.yourname.yourapp` with your own package name.

## Step 1: Show the real folders

By default, Android Studio's Project panel (on the left) uses the **Android** view, which hides and merges some folders. You need to see the real ones.

1. At the top of the Project panel, click the dropdown that says **Android** and choose **Project**.
2. Open the panel's options menu (the **⋮** or gear icon at the top of the panel), go to **Appearance**, and make sure **Compact Middle Packages** is **unchecked**.

Now `app/src/main/kotlin/dev/jahir/{{lib}}/app` shows as separate nested folders, which you'll need in the next steps.

## Step 2: Create your package

1. In the Project panel, expand `app/src/main/`.
2. Right-click the `kotlin` folder and select **New → Package**.
3. Type your package name, for example `com.yourname.yourapp`, and press Enter.

You should now see a new folder structure next to `dev`: `kotlin/com/yourname/yourapp`.

## Step 3: Move the 4 files

1. Expand `app/src/main/kotlin/dev/jahir/{{lib}}/app`. Inside are 4 files:
   - `MainActivity.kt`
   - `MuzeiService.kt`
   - `MyApplication.kt`
   - `NotificationServiceExtension.kt`
2. Select all 4 (click the first one, then Shift + click the last one).
3. Drag them onto your new `yourapp` folder.
4. A **Move** dialog opens. Click **Refactor**.

> [!IMPORTANT]
> Move the files inside Android Studio, not with Finder or File Explorer. When Android Studio moves a file, it also updates the `package` line inside it. Your file manager doesn't.

## Step 4: Check the `package` line

Open each of the 4 files. The very first line should be your package name:

```kotlin
package com.yourname.yourapp
```

If any file still says `package dev.jahir.{{lib}}.app`, change it by hand.

## Step 5: Delete the old folder

The `dev/jahir/{{lib}}/app` folder should now be empty. Right-click the `dev` folder (inside `app/src/main/kotlin`) and select **Delete**.

If Android Studio warns that something inside is still in use, stop and check step 3 again. Something didn't move.

## Step 6: Set the app ID

Open `buildSrc/src/main/java/MyApp.kt` and set `appId` to the **exact same** package name:

```kotlin
object MyApp {
    const val appId = "com.yourname.yourapp"
    const val version = 1
    const val versionName = "1.0.0"
}
```

While you're here, you can also set your version. See [Set App Version](Set-App-Version).

> [!NOTE]
> You don't need to edit `AndroidManifest.xml`. Older versions of this guide asked you to change a `package="..."` line there. Current versions don't have it: the app takes the package name from `appId` automatically.

## Step 7: Fix leftover imports

Some files may still import `BuildConfig` or `R` from the old package. Find them all at once:

1. Open **Edit → Find → Find in Files** (Ctrl + Shift + F on Windows and Linux, Cmd + Shift + F on Mac).
2. Search for `import dev.jahir.`

You'll get a few results. Only change the ones that **end in `.app.R` or `.app.BuildConfig`**, for example:

```kotlin
import dev.jahir.{{lib}}.app.R
```

Either delete that line, or change it to use your package:

```kotlin
import com.yourname.yourapp.R
```

<!--only:blueprint-->

In the Blueprint sample, `NotificationServiceExtension.kt` imports `dev.jahir.kuper.app.R`. That's wrong for your app too, so change it to your package as well.

<!--/only-->

Leave every other `dev.jahir.` import alone, like `dev.jahir.{{lib}}.ui.activities...`. Those come from the {{Lib}} library itself, not from your app.

> [!NOTE]
> Some of these imports are inside comments, in code that's turned off until you set up notifications. Fix them now anyway, so notifications work later without surprises.

## Step 8: Sync and build

1. Click **File → Sync Project with Gradle Files** and wait until it finishes.
2. Click **Build → Clean Project**, then **Build → Rebuild Project**. If your version of Android Studio doesn't show these options, skip this part. The next step builds the app anyway.
3. Press the green **Run** button to install the app on your emulator or phone.

If the app opens, you're done. 🎉

## Quick check

Everything in this table should show your package name:

| Where                             | What it should say                                                     |
| --------------------------------- | ---------------------------------------------------------------------- |
| `buildSrc/src/main/java/MyApp.kt` | `const val appId = "com.yourname.yourapp"`                             |
| The folder of your Kotlin files   | `app/src/main/kotlin/com/yourname/yourapp/`                            |
| First line of each of the 4 files | `package com.yourname.yourapp`                                         |
| Imports of `R` or `BuildConfig`   | None, or `com.yourname.yourapp.R` / `com.yourname.yourapp.BuildConfig` |

## Common problems

- **"Unresolved reference: BuildConfig" or "Unresolved reference: R"**

  The `package` line of that file doesn't match `appId`, or the file still imports the old package. Go back to steps 4 and 7, then sync again.

- **The app installs, but closes as soon as you open it**
  
  Open **Logcat** at the bottom of Android Studio and look for `ClassNotFoundException`. It means your Kotlin files are in a different package than `appId`. Compare both against the table above.

- **You still see a `dev.jahir.{{lib}}.app` folder**
  
  The Project panel is probably back in the Android view, or Compact Middle Packages is on. Repeat step 1.

- **Everything matches the table, but Android Studio still shows errors**
  
  Android Studio's cache is out of date. Click **File → Invalidate Caches**, check **Clear file system cache and local history**, and click **Invalidate and Restart**.

Still stuck? Ask in the [Discord server](https://discord.gg/78h7xgj). Include a screenshot of your Project panel and the error message, so people can help you faster.
