Donations let your users support you with in-app purchases, from inside your app. This is optional.

## Step 1: Create your products

In the [Google Play Console](https://play.google.com/console), create one in-app product for each donation option, for example a small, a medium and a large donation. Write down each **Product ID**.

> [!TIP]
> **New to in-app products?**
> See [Create an in-app product](https://support.google.com/googleplay/android-developer/answer/1153481).

## Step 2: Turn on billing

Billing is on in the sample. Check these two things:

- In `MainActivity.kt`, `billingEnabled` is `true`:

  ```kotlin
  override val billingEnabled = true
  ```

- In `app/src/main/AndroidManifest.xml`, this line is there and isn't commented out:

  ```xml
  <uses-permission android:name="com.android.vending.BILLING" />
  ```

## Step 3: Add your license key

Donations need your app's license key, even if you don't use the license checker. See [Change Security Settings](Change-Security-Settings#license-key).

## Step 4: Add your products

Open `app/src/main/res/values/dashboard_setup.xml` and add each Product ID as an `item`:

```xml
<string-array name="donation_items">
    <item>small_donation</item>
    <item>medium_donation</item>
    <item>large_donation</item>
</string-array>
```

The IDs must match the ones in the Play Console exactly.

> [!NOTE]
> In-app purchases only work for builds installed from Google Play. Upload your app to a testing track (internal testing is the quickest) to try them.

## Not using donations?

1. Set `billingEnabled` to `false` in `MainActivity.kt`.
2. Delete the `BILLING` permission line from `AndroidManifest.xml`.
3. Leave `donation_items` empty.
