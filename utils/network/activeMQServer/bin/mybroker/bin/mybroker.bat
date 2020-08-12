@echo off
set ACTIVEMQ_HOME="C:/Users/Visiteur/Desktop/apache-activemq-5.16.0-bin/apache-activemq-5.16.0"
set ACTIVEMQ_BASE="C:/Users/Visiteur/Desktop/apache-activemq-5.16.0-bin/apache-activemq-5.16.0/bin/mybroker"

set PARAM=%1
:getParam
shift
if "%1"=="" goto end
set PARAM=%PARAM% %1
goto getParam
:end

%ACTIVEMQ_HOME%/bin/activemq %PARAM%