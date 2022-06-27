# made by j0/!j0.

if __name__ == '__main__':
    import push_to_nox as ptn
    import os
    import json
    # the number in the filename
    cwd = os.path.dirname(os.path.realpath(__file__))


    with open("settings.json", "r") as sf:
        json_data = json.loads(sf.read())
    
    download_beta = input("do you want to download the alt version? (y/n)")

    if download_beta[0] == "y":
        download_beta = True
    elif download_beta[0] == "n":
        download_beta = False
    else:
        print("invaild input. please type \"y\" or \"n\".")
        input("press enter to exit")
        exit()


    import gdown

    if download_beta:
        url = f"https://drive.google.com/uc?id={json_data['alt_obb_download_id']}"
    else:
        url = f"https://drive.google.com/uc?id={json_data['main_download_id']}"
        
    output = f"main.{json_data['obb_file_name_version']}.com.ea.game.pvz2_{json_data['custom_obb_letters']}.obb"
    gdown.download(url, output, quiet=False)
    
    print("moving file to emulator...")
#    print( os.path.join(cwd, output))
    ptn.push( os.path.join(cwd, output), f"/storage/self/primary/Android/obb/com.ea.game.pvz2_{json_data['custom_obb_letters']}/", json_data["nox_install_location"], json_data["emulator_name"])
