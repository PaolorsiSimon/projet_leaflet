@echo off
call "%~dp0\o4w_env.bat"
path %OSGEO4W_ROOT%\apps\qgis-ltr\bin;%PATH%
set QGIS_PREFIX_PATH=%OSGEO4W_ROOT:\=/%/apps/qgis-ltr
set QT_PLUGIN_PATH=%OSGEO4W_ROOT%\apps\qgis-ltr\qtplugins;%OSGEO4W_ROOT%\apps\qt5\plugins
cd %USERPROFILE%
start "Qt Designer with QGIS custom widgets" /B "%OSGEO4W_ROOT%\apps\qt5\bin\designer.exe" %*