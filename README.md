# lazy-translator
This is for all the lazy people(like me) who cant do translation so they give them to the interns to suffer . Now with this i can fire the interns haha, hope u find a pace better than now(u can't)

# JSON Translation Script

This script translates the values in a JSON file from one language to another using the `googletrans` library. It supports multi-threading to speed up the translation process and provides detailed progress updates during the translation.

## Prerequisites

- Python 3.6 or later
- `googletrans` library (version 4.0.0-rc1)

## Installation

1. **Clone the repository or download the script.**

2. **Install the required libraries.** Open a terminal or command prompt and run the following command:

   ```bash
   pip install googletrans==4.0.0-rc1
   ```

## Usage

1. **Prepare your JSON file.** Ensure you have a JSON file with the content you want to translate. For example, `en.json`:

   ```json
   {
     "general": {
       "crm": "CRM",
       "analytics": "Analytics",
       "e_commerce": "eCommerce",
       "apps_pages": "Apps & Pages",
       "apps": "Apps",
       "create": "Create",
       "method": "Method",
       "chat": "Chat",
       "calendar": "Calendar",
       "invoice": "Invoice",
       "list": "List",
       "preview": "Preview",
       "edit": "Edit",
       "add": "Add",
       "add_new": "Add New",
       "view": "View",
       "overview": "Overview",
       "security": "Security",
       "billing_plans": "Billing & Plans",
       "shortcuts": "Shortcuts",
       "notifications": "Notifications",
       "read_all_notifications": "Read All Notifications",
       "something_went_wrong": "Something went wrong please try again later",
       "connection": "Connection",
       "pages": "Pages",
       "user_profile": "User Profile",
       "profile": "Profile",
       "teams": "Teams",
       "projects": "Projects",
       "connections": "Connections",
       "account_settings": "Account Settings",
       "account": "Account",
       "logout": "Logout",
       "faq": "FAQ",
       "help_center": "Help Center",
       "pricing": "Pricing",
       "miscellaneous": "Miscellaneous",
       "coming_soon": "Coming Soon",
       "under_maintenance": "Under Maintenance",
       "page_not_found_404": "Page Not Found - 404",
       "not_authorized_401": "Not Authorized - 401",
       "server_error_500": "Server Error - 500",
       "auth_pages": "Auth Pages",
       "401homeButton": "Home",
       "comingSoonNotifyButton": "Notify",
       "enterEmail": "Enter your email",
       "comingSoontitle2": "We are creating something awesome. Please subscribe to get notified when it is ready!",
       "comingSoontitle1": "We are launching soon"
     }
   }
   ```

2. **Run the script.** Use the following command to run the script, specifying the input file, output file, and target language:

   ```bash
   python translate_json.py <input_file> <output_file> <target_language>
   ```

   For example, to translate from English to German:

   ```bash
   python translate_json.py en.json translated_de.json de
   ```

## Parameters

- `<input_file>`: Path to the input JSON file containing the text to be translated.
- `<output_file>`: Path to the output JSON file where the translated text will be saved.
- `<target_language>`: Target language code (e.g., `es` for Spanish, `fr` for French, `de` for German).

## Features

- **Multi-threaded Translation**: The script uses multi-threading to speed up the translation process.
- **Progress Updates**: Provides detailed progress updates, showing the current item being translated.
- **Error Handling**: Includes error handling to manage translation issues and ensure the process continues smoothly.
- **Preserves Formatting**: Maintains the formatting, including spaces and empty lines, of the original JSON file.

## Example

1. **Prepare your JSON file (`en.json`).**

2. **Run the translation:**

   ```bash
   python translate_json.py en.json translated_de.json de
   ```

3. **Check the output file (`translated_de.json`) for the translated content.**

## Troubleshooting

- **Error: Invalid language code**: Ensure you are using a valid language code from the `googletrans` library.
- **No translation returned**: If no translation is returned for a particular string, the script will fallback to the original text and log a warning.

## License

This project is licensed under the MIT License.
