# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
import os
import sys
import datetime
import win32com.client

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'schedule' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

# file_path = os.path.join(base_path, "rocketbot_kill.bat")

"""
    Obtengo el modulo que fue invocado
"""

module = GetParams("module")

if module == "schedule":
    script = GetParams("script_bat")
    time = GetParams("time")
    id = GetParams("id")
    arg = GetParams("arg")
    privilege_level = GetParams("privilege")
    desc = GetParams("desc")
    name = GetParams("task_name")
    file_path = GetParams("path")

    try:
        time = int(time)
        privilege_level = int(privilege_level)

        with open(file_path, 'w') as f:
            f.write(script)

        scheduler = win32com.client.Dispatch('Schedule.Service')
        scheduler.Connect()
        root_folder = scheduler.GetFolder('\\')
        task_def = scheduler.NewTask(0)

        # Create trigger
        start_time = datetime.datetime.now() + datetime.timedelta(minutes=time)
        TASK_TRIGGER_TIME = 1
        trigger = task_def.Triggers.Create(TASK_TRIGGER_TIME)
        trigger.StartBoundary = start_time.isoformat()


        # Create action
        TASK_ACTION_EXEC = 0
        action = task_def.Actions.Create(TASK_ACTION_EXEC)
        action.ID = id
        action.Path = file_path
        action.Arguments = arg

        # Set parameters
        if not privilege_level:
            privilege_level = 0

        TASK_LOGON_SERVICE_ACCOUNT = 5
        task_def.RegistrationInfo.Description = desc
        task_def.Settings.Enabled = True
        task_def.Settings.StopIfGoingOnBatteries = False
        task_def.Principal.LogonType = TASK_LOGON_SERVICE_ACCOUNT
        task_def.Principal.RunLevel = privilege_level

        # Register task
        # If task already exists, it will be updated
        TASK_CREATE_OR_UPDATE = 6
        TASK_LOGON_NONE = 0
        root_folder.RegisterTaskDefinition(
            name,
            task_def,
            TASK_CREATE_OR_UPDATE,
            '',  # No user
            '',  # No password
            TASK_LOGON_NONE)
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        PrintException()
        raise e
