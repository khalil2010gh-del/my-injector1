
[app]
title = Pro Injector HS
package.name = proinjector
package.domain = org.cheat
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# المتطلبات الأساسية
requirements = python3,kivy==2.2.1,pyjnius,android

# الأذونات المطلوبة للحقن
android.permissions = INTERNET, SYSTEM_ALERT_WINDOW, ACCESS_SUPERUSER

# إعدادات النظام (مهمة جداً لمنع خطأ 100)
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True
android.skip_setup_py = True

# مظهر التطبيق
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
