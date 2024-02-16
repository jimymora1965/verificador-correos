def verificar_correo(correo):
    if "@" in correo and correo.count("@") == 1 and correo.index("@") >0 and correo.index("@") < len(correo) -1:
        
        if correo.endswith(".com") or correo.endswith(".com.br"):
            print("ok")
        else:
            print("Error en el correo")
        
    else:
        print("Error en el email")
verificar_correo("usuario@example.com.co")


