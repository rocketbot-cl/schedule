



# Schedule
  
With this module you can create a task and schedule its execution  

![banner](imgs/ModuloShedule.jpg)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Description of the commands

### Schedule a task
  
Create a .bat task and schedule its execution
|Parameters|Description|example|
| --- | --- | --- |
|Task Name||Rocketbot kill app|
|Script for the .bat||taskkill /f /im rocketbot.exe|
|Arguments|Arguments for creating the task|/c 'exit'|
|Minutes|Time to schedule task execution, must be an integer|10|
|Action ID|ID to identify the task|Rocketbot killer|
|Description|Task description|Rocketbot killer batch file|
|Privilege Level|Index of the Privilege Level to execute the task.|0|
|Assign to variable|Variable where the result of the command will be saved|var|
