def verificar_email(email):
    # Verifica si "@" está presente y si hay al menos un carácter antes y después de "@"
    if "@" in email and email.count("@") == 1 and email.index("@") > 0 and email.index("@") < len(email) - 1:
        # Verifica si termina con ".com" o ".com.xx" donde xx puede ser cualquier extensión
        if email.endswith(".com") or email.endswith(".com.br"):
            print("Ok")
        else:
            print("La dirección de email es incorrecta")
    else:
        print("La dirección de email es incorrecta")

# Ejemplo de uso
verificar_email("usuario@example.com")  # Ok
verificar_email("usuario@example.com.br")  # Ok
verificar_email("usuario@example")  # Incorrecta
verificar_email("usuarioexample.com")  # Incorrecta
