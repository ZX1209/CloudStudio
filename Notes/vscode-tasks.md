Not all tasks or scripts can be auto-detected in your workspace. Sometimes it is necessary to define your own custom tasks. Assume you have a script to run your tests in order to set up some environment correctly. The script is stored in a script folder inside your workspace and named test.sh for Linux and macOS and test.cmd for Windows. Run Configure Tasks from the global Terminal menu and select the Create tasks.json file from template entry. This opens the following picker:

Configure Task Runner

Note: If you don't see the list of task runner templates, you may already have a tasks.json file in your folder and its contents will be open in the editor. Close the file and either delete or rename it for this example.

We are working on more auto-detection support, so this list will get smaller and smaller in the future. Since we want to write our own custom task, select Others from the list. This opens the tasks.json file with a task skeleton. Replace the contents with the following:

{
  // See https://go.microsoft.com/fwlink/?LinkId=733558
  // for the documentation about the tasks.json format
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run tests",
      "type": "shell",
      "command": "./scripts/test.sh",
      "windows": {
        "command": ".\\scripts\\test.cmd"
      },
      "group": "test",
      "presentation": {
        "reveal": "always",
        "panel": "new"
      }
    }
  ]
}
The task's properties have the following semantic:

label: The task's label used in the user interface.
type: The task's type. For a custom task, this can either be shell or process. If shell is specified, the command is interpreted as a shell command (for example: bash, cmd, or PowerShell). If process is specified, the command is interpreted as a process to execute.
command: The actual command to execute.
windows: Any Windows specific properties. Will be used instead of the default properties when the command is executed on the Windows operating system.
group: Defines to which group the task belongs. In the example, it belongs to the test group. Tasks that belong to the test group can be executed by running Run Test Task from the Command Palette.
presentation: Defines how the task output is handled in the user interface. In this example, the Integrated Terminal showing the output is always revealed and a new terminal is created on every task run.
options: Override the defaults for cwd (current working directory), env (environment variables), or shell (default shell). Options can be set per task but also globally or per platform. Environment variables configured here can only be referenced from within your task script or process and will not be resolved if they are part of your args, command, or other task attributes.
runOptions: Defines when and how a task is run.