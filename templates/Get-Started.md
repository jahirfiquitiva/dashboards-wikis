Welcome! This page gets the {{Lib}} sample project running on your computer. Every other page in this wiki builds on it. 👋

## What you need

- **[Android Studio](https://developer.android.com/studio)**, the latest stable version. Older versions may not be able to open the project.
- **An Android phone or emulator** to test your app. Android Studio can create an emulator for you: see [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds).
- **A [Google Play developer account](https://play.google.com/console/signup)**, but only when you're ready to publish.

> **New to Android Studio?**
> The [user guide](https://developer.android.com/studio/intro) explains the basics of the IDE.

## Step 1: Download the sample

[Download the sample project](https://github.com/jahirfiquitiva/{{Lib}}/archive/sample.zip) and extract it somewhere safe, like your Documents folder.

You'll get a folder called `{{Lib}}-sample`. Feel free to rename it to your app's name.

## Step 2: Open it in Android Studio

1. Open Android Studio and click **Open** (or **File → Open** if a project is already open).
2. Select the folder you extracted, the one that contains `settings.gradle.kts`, and click **OK**.
3. If Android Studio asks whether you trust the project, click **Trust Project**.

The first time, Android Studio downloads everything the project needs. This can take several minutes. You can follow the progress in the status bar at the bottom of the window.

> **Note**
> If Android Studio suggests upgrading the Android Gradle Plugin or other versions, dismiss it. The [Update {{Lib}}](Update-{{Lib}}) page tells you when and how to update them.

## Step 3: Run the sample

Before changing anything, press the green **Run** button and install the sample on your phone or emulator.

If it opens, your setup works. If it doesn't, fix that first: problems you run into later are much easier to solve when you know the untouched sample builds fine.

## Next step

Set your own package name: [Set Package Name](Set-Package-Name). Do it before anything else, because the other pages assume it's done.
