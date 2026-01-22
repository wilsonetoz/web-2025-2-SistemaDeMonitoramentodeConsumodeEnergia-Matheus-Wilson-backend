def calcular_status_meta(total_consumo, meta_valor):
    percentual = (total_consumo / meta_valor) * 100

    if percentual < 80:
        return "OK"
    elif percentual <= 100:
        return "ALERTA"
    else:
        return "EXCEDIDA"
