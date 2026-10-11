Blueprint can show its sections in a bottom navigation bar (default) or in a side menu (drawer).

You choose in `MainActivity.kt`, inside your package folder. Change the class `MainActivity` extends, and its `import`:

| Style | Import | Class |
| --- | --- | --- |
| Bottom bar (default) | `import dev.jahir.blueprint.ui.activities.BottomNavigationBlueprintActivity` | `BottomNavigationBlueprintActivity()` |
| Side menu | `import dev.jahir.blueprint.ui.activities.DrawerBlueprintActivity` | `DrawerBlueprintActivity()` |

For example, for the side menu:

```kotlin
import dev.jahir.blueprint.ui.activities.DrawerBlueprintActivity

class MainActivity : DrawerBlueprintActivity() {
    // ...keep everything else as it is
}
```

The bottom bar's labels can be customized in [Customize Styles](Customize-Styles#bottom-navigation-labels). The side menu's header can show your app name and version: see `with_drawer_texts` in [Change Blueprint Settings](Change-Blueprint-Settings).
