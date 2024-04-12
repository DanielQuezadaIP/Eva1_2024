aclNum = int(input("Ingrese ID de Vlan? "))
if aclNum >= 1 and aclNum <= 1005:
    print(" Es una Vlan de rango Normal.")
elif aclNum >=1006 and aclNum <= 4095:
    print(" Es una Vlan de rango Extendida")
else:
    print("Esta Vlan no es normal o Extendida.")
