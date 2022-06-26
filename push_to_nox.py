# made by j0/!j0.

def push(local_file, emu_file_dest, nox_install_location, emu_name="NoxPlayer"):
    #nox_install_location needs a "/" or '\" at the end (ie: "C:\users\x\nox\")
    #   nox_install_location: the location where nox is installed on this computer
    #   local_file: the file('s location) you want to push onto the emulator
    #   emu_file_dest: the destation folder on the emulator
    #   emu_name: the name of the emulator that you want to modifiy. check nox Multi-Drive for the exact name
    from subprocess import run as runcmd
    runcmd(f'{nox_install_location}noxconsole launch -name:{emu_name}', shell=True)
    runcmd(f'{nox_install_location}noxconsole adb -name:{emu_name} -command:"push {local_file} {emu_file_dest}"', shell=True)

