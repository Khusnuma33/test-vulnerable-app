import subprocess

def run_system_command(user_input):
    # This matches the "insecure_subprocess" shell=True rule inside src/scanners.py!
    print("Executing system command...")
    return subprocess.Popen(user_input, shell=True)

# This matches the "hardcoded_secret" rule perfectly!
AWS_SECRET_KEY = "sk_live_51NxAwesomeSecretTokenForTesting"
