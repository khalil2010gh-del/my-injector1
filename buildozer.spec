
[app]
title = My Injector
package.name = myinjector
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

requirements = python3,kivy,pyjnius,android

android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, ACCESS_SUPERUSER

# الإعدادات التي تحل مشكلة 100
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
