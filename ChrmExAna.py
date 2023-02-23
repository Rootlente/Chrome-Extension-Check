import argparse
import os
import re
import json
import glob

def check_permissions(manifest, dangerous_perms, dangerous_found):
    perm_list = manifest.get("permissions", []) + manifest.get("optional_permissions", [])

    if not perm_list:
        return

    for perm in perm_list:
        if perm in dangerous_perms:
            dangerous_found.add(perm)


def check_buffer_code(file_path):
    with open(file_path) as f:
        content = f.read()

    if "buffer = \"\";" in content and "document.addEventListener(\"keyup\"," in content:
        print(f"    Keylogger code found in file: {file_path}")


def analyze_extension(extension_path, dangerous_perms):
    manifest_path = os.path.join(extension_path, "manifest.json")

    if not os.path.exists(manifest_path):
        return

    with open(manifest_path) as f:
        manifest = json.load(f)

    dangerous_found = set()
    check_permissions(manifest, dangerous_perms, dangerous_found)

    if not dangerous_found:
        return

    print(f"Analyzing extension: {extension_path}")
    print(f"    Dangerous permissions found: {', '.join(sorted(dangerous_found))}")

    js_files = glob.glob(os.path.join(extension_path, "*.js"))
    for js_file in js_files:
        check_buffer_code(js_file)


def main():
    parser = argparse.ArgumentParser(description='Analyze Google Chrome extensions for dangerous permissions and keylogger code')
    parser.add_argument('-p', '--path', type=str, help='Path to the directory containing the extensions\n'
                                                       'For Windows, the path is C:\\Users\\<username>\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\n'
                                                       'For macOS, the path is /Users/<username>/Library/Application Support/Google/Chrome/Default/Extensions/\n'
                                                       'For Linux, the path is ~/.config/google-chrome/Default/Extensions/')

    args = parser.parse_args()

    if not args.path:
        parser.print_help()
        return

    dangerous_perms = [
        "activeTab",
        "alarms",
        "background",
        "bookmarks",
        "browsingData",
        "clipboardRead",
        "clipboardWrite",
        "contentSettings",
        "contextMenus",
        "cookies",
        "debugger",
        "declarativeContent",
        "declarativeNetRequest",
        "declarativeNetRequestWithHostAccess",
        "declarativeNetRequestFeedback",
        "desktopCapture",
        "downloads",
        "fontSettings",
        "gcm",
        "geolocation",
        "history",
        "identity",
        "idle",
        "management",
        "nativeMessaging",
        "notifications",
        "pageCapture",
        "power",
        "printerProvider",
        "privacy",
        "proxy",
        "scripting",
        "search",
        "sessions",
        "storage",
        "system.cpu",
        "system.display",
        "system.memory",
        "system.storage",
        "tabCapture",
        "tabGroups",
        "tabs",
        "topSites",
        "tts",
        "ttsEngine",
        "unlimitedStorage",
        "webNavigation",
        "webRequest"
    ]

    for dirpath, dirnames, filenames in os.walk(args.path):
        for dirname in dirnames:
            extension_path = os.path.join(dirpath, dirname)
            analyze_extension(extension_path, dangerous_perms)


if __name__ == '__main__':
    main()





