import subprocess

# Execute a shell command
command = "ls -l"
result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    print("Command executed successfully:")
    print(result.stdout)
else:
    print("Command failed:")
    print(result.stderr)

# Execute a shell script
script_path = "/path/to/your/script.sh"
result = subprocess.run(script_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

if result.returncode == 0:
    print("Script executed successfully:")
    print(result.stdout)
else:
    print("Script failed:")
    print(result.stderr)
