When your app opens, it shows a launch screen (splash screen) for a moment: your image, centered, on top of your `surface` color (see [Set App Colors](Set-App-Colors)).

To use your own image:

1. Save your artwork as a PNG, **288 × 288 px**, named `app_splash_screen_picture.png`.
2. Put it in `app/src/main/res/drawable-nodpi`. If the folder doesn't exist, create it: right-click `app/src/main/res`, select **New → Directory**, and name it `drawable-nodpi`.

That's it. Your image replaces {{Lib}}'s default one.
