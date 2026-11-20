# 1. Instalar Ventoy en la USB (desde Linux)

> ⚠️ Esto **borra todo** lo que tenga la USB.

## Identificar la USB

Ejecuta esto **sin** la USB y luego **con** la USB conectada. Lo que aparece nuevo es la USB.

```bash
lsblk -o NAME,SIZE,MODEL,TRAN
```

Ejemplo:

| Dispositivo | Tamaño | Modelo | Qué es |
|---|---|---|---|
| `sda` | 57.7G | DataTraveler 3.0 (`usb`) | **La USB** ✅ |
| `nvme0n1` | 465.8G | Disco de la compu | No tocar |

La letra (`sda`, `sdb`…) puede cambiar cada vez. **Revisa siempre antes de instalar.**

## Descargar e instalar

1. Descarga el archivo `-linux.tar.gz` desde <https://github.com/ventoy/Ventoy/releases>.
2. Instala:

```bash
cd ~/Downloads
tar -xzf ventoy-X.Y.Z-linux.tar.gz
cd ventoy-X.Y.Z                       # hay que entrar a la carpeta
sudo umount /dev/sda1 /dev/sda2       # si dice "not mounted", está bien
sudo sh Ventoy2Disk.sh -i /dev/sda    # cambia sda por lo que diga lsblk
```

- Pregunta **dos veces** si estás seguro: revisa que el tamaño coincida con tu USB y responde `y`.
- Debe terminar con `Install Ventoy to /dev/sda successfully finished.`
- Desconecta y vuelve a conectar la USB: aparece una unidad llamada **Ventoy**.

## Actualizar Ventoy sin borrar las ISO

```bash
sudo sh Ventoy2Disk.sh -u /dev/sda
```

## Expulsar la USB con seguridad

```bash
cd ~
sync
udisksctl unmount -b /dev/sda1
udisksctl power-off -b /dev/sda
```

## Arrancar desde la USB

1. En el equipo destino, entra al menú de arranque (en HP suele ser **F9**; en otras marcas F12, F8, Esc…).
2. Elige la USB en **UEFI Boot Sources**.
3. En el menú de Ventoy elige la ISO → **Boot in normal mode**.

Si no arranca, en la BIOS desactiva **Secure Boot** (y en equipos viejos revisa **Fast Boot** y **Legacy Support**).
