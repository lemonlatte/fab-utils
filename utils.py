from fabric.api import local, run, env, put, sudo, cd, lcd, settings, prefix
import os

# env.hosts = ["127.0.0.1"]
# env.user = "test"
# env.password = "qwerty"
env.use_ssh_config = True


def tar(tar_file, src_file, excludes=[], user=env.user, remote=False):
    exclude_files = " ".join(['--exclude="%s"' % e for e in excludes])
    if remote:
        sudo('tar zcvf %s %s %s' % (tar_file, exclude_files, src_file), user=user)
    else:
        local('tar zcvf %s %s %s' % (tar_file, exclude_files, src_file))


def create_virtualenv(venv_name=".venv", user=env.user, vevn_args=[], **kwargs):

    with settings(sudo_user=user):
        sudo('virtualenv %s %s' % (venv_name, " ".join(vevn_args)))

        with prefix('source %s/bin/activate' % venv_name):
            with settings(warn_only=True):
                if 'pip_file' in kwargs:
                    sudo('pip install -r %s' % kwargs["pip_file"])
