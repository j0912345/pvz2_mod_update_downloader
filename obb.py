# made by j0/!j0.

if __name__ == '__main__':
    import push_to_nox as ptn
    import os
    import json
    cwd = os.path.dirname(os.path.realpath(__file__))


    with open("settings.json", "r") as sf:
        json_data = json.loads(sf.read())
    
    download_beta = input("do you want to download the beta? (y/n)")

    if download_beta[0] == "y":
        download_beta = True
    elif download_beta[0] == "n":
        download_beta = False
    else:
        print("invaild input. please type \"y\" or \"n\".")
        input("press enter to exit")
        exit()

    # from: https://github.com/wkentaro/gdown
    import gdown


    if download_beta:
        url = "https://drive.google.com/uc?id=1RPXwKU-UR7Nkm-8XUUyhgkSStodB-dz5"
    else:
        # url for constain builds
        url = "https://drive.google.com/uc?id=10yQvqpbLoXBX9kpHzbK4fGAEWg_uE1ww"
    output = "com.ea.game.pvz2_wha.obb"
    gdown.download(url, output, quiet=False)
    
    print("moving file to emulator...")
#    print( os.path.join(cwd, output))
    ptn.push( os.path.join(cwd, output), "/storage/self/primary/Android/obb/com.ea.game.pvz2_wha/", json_data["nox_install_location"], json_data["emulator_name"])
