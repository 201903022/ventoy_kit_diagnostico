# 3. Organizar la USB y configurar `ventoy.json`

## Carpetas

Dentro de la unidad **Ventoy**:

```
Diagnostico/memtest.iso
Linux/fedora-live.iso
Linux/ubuntu-server.iso
Rescate/systemrescue.iso
Rescate/clonezilla.iso
Rescate/rescuezilla.iso
Rescate/shredos.iso
Windows/hirens.iso
Herramientas/            (programas portables de Windows, notas, reportes)
ventoy/ventoy.json
```

Puedes renombrar las ISO con nombres simples. Ventoy no necesita el nombre original, y así `ventoy.json` no se rompe al cambiar de versión.

## `ventoy.json`

Copia [`ventoy/ventoy.json`](../ventoy/ventoy.json) a `ventoy/ventoy.json` dentro de la USB. Hace tres cosas:

- **`control`**: abre el menú en modo árbol (con carpetas) en vez de lista plana.
- **`menu_alias`**: muestra nombres claros ("ShredOS - BORRAR DISCOS (peligro)") en lugar del nombre del archivo.
- **`menu_tip`**: muestra un aviso en rojo al resaltar cada ISO.

Valida que el JSON esté bien escrito antes de usarlo:

```bash
python3 -m json.tool ventoy/ventoy.json > /dev/null && echo "JSON válido"
```

Una coma de más y Ventoy ignora el archivo entero.

## Menú en árbol sin `ventoy.json`

En el menú de Ventoy, presiona **F3** para alternar entre vista de árbol (carpetas) y lista.

## Hiren's BootCD PE

Si no arranca bien, en el menú de Ventoy presiona **Ctrl+W** antes de entrar para usar el modo *wimboot*.
