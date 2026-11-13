[app]

title = WhatsApp Ban Checker
package.name = whatsappchecker
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a
android.permissions = INTERNET

android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
