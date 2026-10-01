from getpass import getpass

from werkzeug.security import generate_password_hash


password = getpass("Nueva contraseña administrativa: ")
confirmation = getpass("Confirma la contraseña: ")

if not password or password != confirmation:
    raise SystemExit("Las contraseñas no coinciden o están vacías.")

print(generate_password_hash(password))