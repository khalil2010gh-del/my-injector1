[app]
title = Super HS Injector
package.name = superinjector
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المتطلبات الأساسية (مبسطة جداً لتفادي الخطأ 1)
requirements = python3,kivy,pyjnius,android

# الأذونات
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, ACCESS_SUPERUSER

# الإعدادات التقنية
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
