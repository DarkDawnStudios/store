import subprocess
from datetime import datetime
def get_git_timestamp(abs_path):
    git_log = subprocess.Popen(
        "git log --pretty=format:%ct --quiet -1 HEAD",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True,
        cwd=abs_path,
        universal_newlines=True,
    )
    
    time_format = "%Y%m%d%H%M%S"
    git_timestamp = git_log.communicate()[0]
    try:
        timestamp = datetime.utcfromtimestamp(int(git_timestamp))
    except ValueError:
        return datetime.now().strftime(time_format)
    return timestamp.strftime(time_format)