[app]
# (str) Title of your application
title = Emaus App

# (str) Package name
package.name = emausapp

# (str) Package domain (needed for android packaging)
package.domain = org.emaus

# (str) Source code where the main.py live
source.dir = .

# (str) Application versioning
version = 0.1

# (str) Python version to use
python.version = 3.10

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json,html,css,js

# (list) Application requirements
# IMPORTANT: Include flask and its dependencies
requirements = python3,flask,werkzeug,jinja2,itsdangerous,click,setuptools,kivy

# (str) Custom source folders for requirements
# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (str) Android build-tools version to use
android.build_tools_version = 33.0.0

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Short name of the application
name = EmausApp

# (str) Icon of the application
#icon.filename = %(source.dir)s/static/logo.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1