Most of {{Lib}}'s setup happens in XML files, like `strings.xml` or `dashboard_setup.xml`. If you've never edited one, this page explains everything you need. It takes a few minutes, and it saves you from the most common build errors. 🧩

## What an XML file looks like

Here's a small example:

```xml
<resources>
    <!-- Your app's name -->
    <string name="app_name">My App</string>
    <bool name="animations_enabled_by_default">true</bool>
</resources>
```

Each setting is one **element**, with three parts:

```xml
<string name="app_name">My App</string>
```

| Part | In the example | Can you change it? |
| --- | --- | --- |
| The opening tag, with the setting's type and name | `<string name="app_name">` | **No.** {{Lib}} finds the setting by this name |
| The value | `My App` | **Yes.** This is the only part you change |
| The closing tag | `</string>` | **No.** It must match the opening tag |

So, to change your app's name, only replace `My App` and leave everything around it exactly as it is:

```xml
<string name="app_name">Wallpapers by Jane</string>
```

Everything goes inside `<resources>` and `</resources>`, the first and last lines of the file. Don't delete them.

## Types of values

The type at the start of the tag tells you what kind of value it expects:

| Type | What to write | Example |
| --- | --- | --- |
| `string` | Any text | `<string name="email">jane@example.com</string>` |
| `bool` | Only `true` or `false` | `<bool name="show_overview">true</bool>` |
| `integer` | A whole number | `<integer name="default_theme">2</integer>` |
| `color` | A hex color code | `<color name="accent">#3881fa</color>` |

### Empty values

Some settings are empty by default. That means "not set":

```xml
<string name="toolbar_logo"></string>
```

To set it, write the value between the two tags, with no spaces around it:

```xml
<string name="toolbar_logo">my_logo</string>
```

### Lists

A `string-array` is a list. Each value goes in its own `<item>`:

```xml
<string-array name="donation_items">
    <item>small_donation</item>
    <item>large_donation</item>
</string-array>
```

To add a value, copy a whole `<item>...</item>` line and change what's inside. To remove one, delete its whole line.

### Elements without a closing tag

Some elements keep their value inside the tag, and end with `/>` instead of a closing tag. You change the text inside the quotes:

```xml
<version title="v1.0.0" />
<item text="First release" />
```

## Comments

Anything between `<!--` and `-->` is a comment. The app ignores it. Comments explain what each setting does, so they're worth reading.

```xml
<!-- Do you want animations to be enabled for all your users? -->
<bool name="animations_enabled_by_default">true</bool>
```

Comments can also turn off a piece of code. Some pages ask you to "remove the comment marks" to turn something on. That means deleting the `<!--` before the code and the `-->` after it, and nothing else:

```xml
<!--
<uses-permission android:name="com.android.vending.BILLING" />
-->
```

becomes:

```xml
<uses-permission android:name="com.android.vending.BILLING" />
```

Always delete both marks. If you delete only one, the rest of the file breaks.

## Special characters

A few characters have a special meaning in XML, so they need to be written differently inside a value:

| Character | Write it as | Example |
| --- | --- | --- |
| `&` | `&amp;` | `Black &amp; White` shows as "Black & White" |
| `<` | `&lt;` | `5 &lt; 10` |
| `'` (apostrophe) | `\'` | `Jane\'s Wallpapers` |
| `"` (double quote) | `\"` | `The \"best\" icons` |

The `&` matters most in links. For example, a Google Drive link has an `&` in it, so in an XML file you write it like this:

```xml
<string name="json_url">https://drive.google.com/uc?export=download&amp;id=FILE_ID</string>
```

This only applies to XML files. In the wallpapers JSON file, write `&` as it is.

## Let Android Studio help you

- **Red underlines** mean something is wrong on that line. Hover over it to see what.
- **Code → Reformat Code** fixes the indentation of the whole file, which makes a missing or extra tag easier to spot.
- When the build fails, the error message names the file and the line. Click it to jump there.

## Common problems

The exact error message depends on your version of Android Studio, but it always names the file and the line. Go to that line and look for one of these.

- **The error mentions a tag, like "mismatched tag" or "must be terminated"**

  A closing tag is missing, misspelled or doesn't match its opening tag. Check that every `<string ...>` has a `</string>` after it, and the same for every other type.

- **The error mentions an apostrophe**

  A text has an `'` in it. Write it as `\'`, like `Jane\'s Wallpapers`.

- **The error says "not well-formed", or mentions `&` or an entity**

  A value, usually a link, has an `&` in it. Write it as `&amp;`.

- **The error mentions "prolog" or "trailing section"**

  There's text before `<resources>` or after `</resources>`, usually a leftover from a paste. Delete it.

- **No error, but a setting has no effect**

  Check that you didn't change the `name`, that `bool` values are exactly `true` or `false`, and that the setting isn't inside a comment.
