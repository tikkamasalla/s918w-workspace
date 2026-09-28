@echo off
set HTTPS_PROXY=
set HTTP_PROXY=
set https_proxy=
set http_proxy=
set JAVA_HOME=E:\android-sdk\jdk21
set ANDROID_HOME=E:\android-sdk
set ANDROID_SDK_ROOT=E:\android-sdk
E:
cd E:\powersave-spoof
call gradlew.bat :app:assembleDebug --console=plain
echo BUILD-RC=%ERRORLEVEL%
