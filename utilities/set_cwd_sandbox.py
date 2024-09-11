import os

def set_cwd_to_sandbox():
    # Specifieke pad naar de sandbox map
    sandbox_path = r'C:\GIT\Work\MIT_AIP\src\sandbox'

    # Controleer of de 'sandbox'-map bestaat
    if os.path.exists(sandbox_path):
        # Verander de huidige werkdirectory naar de 'sandbox'-map
        os.chdir(sandbox_path)
        print(f"CWD veranderd naar: {os.getcwd()}")
    else:
        print(f"De map '{sandbox_path}' bestaat niet.")

# Roep de functie aan om de CWD naar 'sandbox' te veranderen
set_cwd_to_sandbox()
