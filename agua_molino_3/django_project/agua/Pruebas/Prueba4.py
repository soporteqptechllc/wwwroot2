# 1:)
""" import os;
print("\nMetodo 1")
os.system('python c:/inetpub/django_project/agua/mensaje.py') """
# 2:)
"""print("\nMetodo 2")
from subprocess import call
call(["python", "c:/inetpub/django_project/agua/mensaje.py"])"""
# 3:)
print("\nMetodo 3")
import mensaje
print(mensaje.my_name())
# 4:)
""" print("\nMetodo 4")
import subprocess
result = subprocess.getoutput('python c:/inetpub/django_project/agua/mensaje.py')
print(result) """