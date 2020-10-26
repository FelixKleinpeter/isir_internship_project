@echo off
set ACTIVEMQ_HOME="C:/Users/Visiteur/Desktop/project/utils/network/activeMQServer"
set ACTIVEMQ_BASE="C:/Users/Visiteur/Desktop/project/utils/network/activeMQServer/bin/mybroker"

set PARAM=%1
:getParam
shift
if "%1"=="" goto end
set PARAM=%PARAM% %1
goto getParam
:end

%ACTIVEMQ_HOME%/bin/activemq %PARAM%