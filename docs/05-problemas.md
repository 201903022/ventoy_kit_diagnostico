# 5. Problemas frecuentes

## El instalador de Ubuntu dice "problem examining the storage devices"

Pasa cuando el disco destino tiene particiones o firmas viejas (por ejemplo, un Linux anterior).

1. En la pantalla de error: **Switch to a shell**.
2. Mira los discos:

```bash
lsblk -o NAME,SIZE,MODEL,FSTYPE,LABEL
```

3. **Solo si ese disco no tiene nada que quieras guardar** (⚠️ no se puede deshacer), borra sus firmas. Confirma que sea el disco correcto y **no la USB**:

```bash
wipefs -a /dev/sdX[1-6]
wipefs -a /dev/sdX
lsblk /dev/sdX        # no debe tener particiones
reboot
```

4. Arranca otra vez desde la USB y repite la instalación.

## La USB no aparece en el menú de arranque

- Desactiva **Secure Boot** en la BIOS (o inscribe la clave de Ventoy si prefieres dejarlo activo).
- Prueba otro puerto USB, preferiblemente uno trasero en escritorios.
- En equipos muy viejos puede hacer falta activar *Legacy Support*.

## Una ISO no arranca

- Verifica su checksum (ver [guía 2](02-isos.md)).
- Prueba **Boot in normal mode**, o **Grub2 mode** si el normal falla.
- Actualiza Ventoy (`-u`): las versiones nuevas soportan ISO más recientes.

## `ventoy.json` no hace efecto

- Debe estar exactamente en `ventoy/ventoy.json` dentro de la unidad Ventoy.
- Valídalo con `python3 -m json.tool`.
- Las rutas de `image` deben coincidir con los nombres reales de las ISO, con `/` inicial y mayúsculas exactas.

## Los nombres de discos cambian

Los nombres (`nvme0n1`, `nvme1n1`, `sda`) pueden intercambiarse entre arranques. Antes de cualquier operación destructiva, identifica el disco por **modelo y tamaño**.
