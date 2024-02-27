import psutil
import time
import subprocess
import os
from colorama import Fore, Back, Style

def execute_bash_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

def bash(command_on_bash):
    os.system(command_on_bash)

def monitor():
    # Get the current running processes
    # running_processes = psutil.Process().children(recursive=True)
    
    # Get the number of CPU cores
    cpu_cores = psutil.cpu_count()
    # Get CPU freq
    cpu_freq = psutil.cpu_freq(percpu=True)
    # Get current temp
    # cpu_temp = psutil.sensors_temperatures()
    # Get the current CPU usage
    cpu_usage = psutil.cpu_percent()
    # Get the current memory usage
    memory_usage = psutil.virtual_memory().percent
    # Get the current disk usage
    disk_usage = psutil.disk_usage("/").percent
    # Print the collected data
    
    # print(f"Running Processes: {running_processes}")
    # print(f"CPU temp: {cpu_temp}")
    print(f"{Fore.GREEN}CPU freq: {cpu_freq}{Style.RESET_ALL}\n", end='\r')
    print(f"{Fore.GREEN}CPU cores: {cpu_cores}{Style.RESET_ALL}\n", end='\r')
    print(f"{Fore.GREEN}CPU usage: {cpu_usage}%{Style.RESET_ALL}\n", end='\r')
    print(f"{Fore.GREEN}Memory usage: {memory_usage}%{Style.RESET_ALL}\n", end='\r')
    print(f"{Fore.GREEN}Disk usage: {disk_usage}%{Style.RESET_ALL}\n", end='\r')

def main():
    try:
        while  True:
            bash('clear')
            bash('echo "MONITORING UR SYSTEM\n"')
            monitor()
            bash('neofetch')
            time.sleep(1)

    except (KeyboardInterrupt, SystemExit):
        print("\nexit")


if __name__ == "__main__":
    main()