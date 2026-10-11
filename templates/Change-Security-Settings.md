Security settings protect your app from piracy. They live in `MainActivity.kt`, inside your package folder (`app/src/main/kotlin/com/yourname/yourapp/`).

```kotlin
override val billingEnabled = true

override fun amazonInstallsEnabled(): Boolean = false
override fun checkLPF(): Boolean = true
override fun checkStores(): Boolean = true

override fun getLicKey(): String? = "MIIBIjANBgkqhkiGgKglYGYGihLuihUuhhuBlouBkuiu"

override fun getLicenseChecker(): PiracyChecker? {
    destroyChecker() // Important
    return if (BuildConfig.DEBUG) null else super.getLicenseChecker()
}
```

## Settings

| Setting | When `true` | Default |
| --- | --- | --- |
| `billingEnabled` | Turns on in-app purchases. See [Use Donations](Use-Donations) | `true` |
| `amazonInstallsEnabled` | Allows installs from the Amazon Appstore. Turn it on if you publish there | `false` |
| `checkLPF` | Blocks the app if Lucky Patcher (a popular piracy tool) is installed | `true` |
| `checkStores` | Blocks the app if a third-party store known for pirated apps is installed, like Aptoide | `true` |

## License key

The license checker blocks your app if it wasn't installed from Google Play. It needs your app's license key, and so do donations. The key in the sample isn't valid, so replace it:

1. Create your app in the [Google Play Console](https://play.google.com/console).
2. Go to **Monetize with Play → Monetization setup** and copy the **Licensing** key.
3. Paste it in `getLicKey`, keeping the quotes:

   ```kotlin
   override fun getLicKey(): String? = "your-license-key"
   ```

## Turn the license checker on or off

By default, the license checker only runs in release builds, so you can test debug builds without it. The last line of `getLicenseChecker` decides when it runs:

| You want the checker... | Last line |
| --- | --- |
| Only in release builds (default) | `return if (BuildConfig.DEBUG) null else super.getLicenseChecker()` |
| Never | `return null` |
| Always, also in debug builds | `return super.getLicenseChecker()` |

Keep `destroyChecker()` as the first line of `getLicenseChecker`.

> **Note**
> If you see "Unresolved reference: BuildConfig" in this file, your package name isn't set up correctly. See [Set Package Name](Set-Package-Name#common-problems).
