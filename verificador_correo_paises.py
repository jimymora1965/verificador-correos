def verificar_correo(correo):
    if "@" in correo and correo.count("@") == 1 and correo.index("@") >0 and correo.index("@") < len(correo) -1:
        extensiones_validas = [".com", ".br", ".co", ".uk", ".us", ".ca", ".au", ".mx"]  # Agrega aquí todas las extensiones válidas que desees reconocer
        for extension in extensiones_validas:
            if correo.endswith(extension):
                print("Correo válido")
                return  # Sale de la función después de encontrar una extensión válida
        print("Error en el correo")
    else:
        print("Error en el correo")

verificar_correo("usuario@example.br")
