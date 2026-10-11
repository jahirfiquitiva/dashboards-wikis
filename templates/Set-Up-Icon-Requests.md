Icon requests let users ask you for icons of apps your pack doesn't cover yet. Blueprint collects the app info and icons and sends them to you.

All request settings live in `app/src/main/res/values/blueprint_setup.xml`.

## Step 1: Choose how you receive requests

You can receive requests in two ways:

- **By email** (default). Blueprint opens the user's email app with a zip file attached, addressed to your `email`.
- **Through [Pacific Manager](https://pacificmanager.app)**, a request manager. Requests are uploaded there, and you see them all in one place instead of in your inbox.

Either way, set your `email` first (see [Change Icon Settings](Change-Icon-Settings)). Requests don't work without it.

To use Pacific Manager, create an account there, get your API key, and paste it:

```xml
<string name="request_manager_backend_api_key" translatable="false">your-api-key</string>
<string name="request_manager_base_url" translatable="false">https://pacificmanager.app/</string>
```

Keep `request_manager_base_url` as it is. If the API key is empty, Blueprint sends requests by email.

## Step 2: Set limits (optional)

You can limit how many apps users can request, and how often:

```xml
<integer name="max_apps_to_request">-1</integer>
<integer name="time_limit_in_minutes">0</integer>
```

| Setting | Value | Result |
| --- | --- | --- |
| `max_apps_to_request` | `-1` (default) | No limit |
| | `0` | Requests are turned off |
| | Any other number | Users can request up to that many apps at a time |
| `time_limit_in_minutes` | `0` or less (default) | No waiting between requests |
| | Any other number | Users have to wait that many minutes between requests |

Some useful time limits:

| Minutes | Means |
| --- | --- |
| `60` | One request per hour |
| `1440` | One request per day |
| `10080` | One request per week |
| `40320` | One request every four weeks |

## Step 3: Set the request title

`request_title` is the subject of request emails, so you can find them easily in your inbox:

```xml
<string name="request_title">My Icon Pack Request</string>
```
