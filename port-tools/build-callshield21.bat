@echo off
set HTTPS_PROXY=
set HTTP_PROXY=
set https_proxy=
set http_proxy=
set JAVA_HOME=E:\android-sdk\jdk21
set ANDROID_HOME=E:\android-toolchain\sdk
set ANDROID_SDK_ROOT=E:\android-toolchain\sdk
C:
cd C:\Users\Aows\Downloads\callshield-port\CallShield-release
call gradlew.bat :app:testDebugUnitTest ktlintCheck detekt lintRelease --console=plain
echo BUILD-RC=%ERRORLEVEL%
