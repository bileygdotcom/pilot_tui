command = 'mkdir ' + softpath
                p = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                out = str(p.stdout.read())
                err = str(p.stderr.read())
