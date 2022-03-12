import os

os.system("xcopy /s /Y dist\horsy.exe bin\horsy.exe*")
os.system("xcopy /s /Y dist\horsygui.exe bin\horsygui.exe*")
os.system("xcopy /s /Y dist\horsy_installer.exe bin\installer-horsy-win.exe*")
os.system("xcopy /s /Y dist\horsy_installer_silent.exe bin\installer-horsy-win-silent.exe*")
os.system("xcopy /s /Y dist\horsy_updater.exe bin\horsy_updater.exe*")

with open("web_vars/version", "r") as f_r:
    version = f_r.readline()

with open("web_vars/version", "w") as f_w:
    f_w.write(str(int(version) + 1))
