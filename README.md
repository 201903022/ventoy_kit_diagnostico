# ventoy-kit-diagnostico

Una USB multiuso con **Ventoy** para **diagnosticar computadoras viejas**, decidir **qué piezas comprar** (RAM, discos, CPU), **respaldar discos** y **instalar un servidor Ubuntu**. Todo se prepara desde Linux.

> ⚠️ Instalar Ventoy **borra todo** lo que tenga la USB. Revisa siempre con `lsblk` cuál es la USB antes de ejecutar comandos.

## ¿Qué incluye el kit?

| Carpeta en la USB | ISO | Para qué sirve |
|---|---|---|
| `Diagnostico/` | Memtest86+ | Probar la RAM (errores = 0 tras varias pasadas) |
| `Linux/` | Fedora Workstation Live | Probar el equipo sin instalar: `lscpu`, `lsblk`, `smartctl`, `sensors`, `dmidecode` |
| `Linux/` | Ubuntu Server LTS | Instalar el servidor |
| `Rescate/` | SystemRescue | Rescate, SMART de discos, GParted, `dmidecode` |
| `Rescate/` | Clonezilla | Respaldo/clonado de discos (texto, muy eficiente) |
| `Rescate/` | Rescuezilla | Lo mismo que Clonezilla pero con ventanas |
| `Rescate/` | ShredOS | **Borrado seguro** de discos (peligroso) |
| `Windows/` | Hiren's BootCD PE | Windows de rescate con CPU-Z, GPU-Z, HWiNFO, CrystalDiskInfo |

Con esto se puede revisar **RAM, disco, CPU, temperaturas y placa base** de cualquier equipo, sin tocar su sistema.

## Guías

1. [Instalar Ventoy en la USB](docs/01-instalar-ventoy.md)
2. [Descargar y verificar las ISO](docs/02-isos.md)
3. [Organizar la USB y configurar `ventoy.json`](docs/03-organizar-usb.md)
4. [Leer los diagnósticos y decidir qué comprar](docs/04-leer-diagnosticos.md)
5. [Problemas frecuentes](docs/05-problemas.md)
6. [Herramientas portables opcionales (Windows)](docs/06-herramientas-portables.md)

## Inicio rápido

```bash
lsblk -o NAME,SIZE,MODEL,TRAN          # identifica la USB (ej. sda)
sudo umount /dev/sda1 /dev/sda2        # "not mounted" está bien
sudo sh Ventoy2Disk.sh -i /dev/sda     # ⚠️ borra la USB
```

Luego copia las ISO a la unidad **Ventoy**, copia `ventoy/ventoy.json` a `ventoy/ventoy.json` dentro de la USB, y arranca el equipo desde ella.

## Licencia

Documentación bajo MIT. Las ISO son de sus respectivos autores y **no** se incluyen en este repositorio: se descargan de las páginas oficiales.
