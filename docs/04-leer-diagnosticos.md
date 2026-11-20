# 4. Leer los diagnósticos y decidir qué comprar

Idea central: **mide antes de comprar**. En un equipo viejo, normalmente rinden más una buena cantidad de RAM y un SSD sano que cambiar el procesador.

Arranca con **Fedora Live** (modo *Try*, no *Install*) o **SystemRescue** y abre una terminal.

## 1. Resumen del equipo

```bash
lscpu | head -20                     # modelo de CPU, núcleos, hilos
sudo dmidecode -t system             # marca y modelo
sudo dmidecode -t baseboard          # placa base
lsblk -o NAME,SIZE,MODEL,TRAN,TYPE   # discos
```

## 2. RAM: ¿cuánto cabe y qué se puede añadir?

```bash
sudo dmidecode -t memory             # cada ranura: tamaño, tipo (DDR3/DDR4), velocidad, vacía o llena
sudo dmidecode -t 16                 # capacidad MÁXIMA que soporta la placa
```

Fíjate en:

- **Tipo** (DDR3, DDR4…): lo que compres debe ser del mismo tipo.
- **Ranuras libres**: si todas están llenas, tocará reemplazar módulos.
- **Capacidad máxima** (`Maximum Capacity`): no compres más de lo que la placa reconoce.
- **Velocidad**: mezclar módulos distintos funciona, pero todos trabajan a la velocidad del más lento.

Luego corre **Memtest86+** al menos **4 pasadas**. **Errors: 0** significa RAM sana. Cualquier error = módulo malo.

## 3. Discos: ¿están sanos?

```bash
sudo smartctl -a /dev/sda            # SATA (HDD o SSD)
sudo smartctl -a /dev/nvme0          # NVMe
```

Identifica el disco por **modelo y tamaño**, no solo por la letra: los nombres pueden cambiar entre arranques.

**HDD / SSD SATA**: son malas señales los valores **mayores a 0** en:

- `Reallocated_Sector_Ct`
- `Current_Pending_Sector`
- `Offline_Uncorrectable`

`UDMA_CRC_Error_Count` alto suele indicar un cable malo, no un disco malo. Mira también `Power_On_Hours` (horas de uso) y, en SSD, el desgaste (`Wear_Leveling_Count` / `Media_Wearout_Indicator`).

**NVMe**:

- `Critical Warning`: debe ser `0x00`.
- `Available Spare` vs `Available Spare Threshold`: el primero debe estar bien por encima del segundo.
- `Percentage Used`: desgaste (100 % = vida estimada agotada, no muerte inmediata).
- `Media and Data Integrity Errors`: debe ser 0.
- `Unsafe Shutdowns`: apagones o cortes bruscos; si es alto, conviene mantener respaldos.

Regla práctica: con errores reales (sectores pendientes/reasignados creciendo, errores de media), **no pongas datos importantes** en ese disco. Si está sano, no lo reemplaces solo por viejo.

## 4. CPU y temperaturas

```bash
sensors                              # temperaturas (paquete lm_sensors)
```

- En reposo, una CPU de escritorio normal ronda 30–50 °C.
- Si se acerca a 90–100 °C bajo carga, revisa el disipador, el polvo y la pasta térmica antes de pensar en cambiar la CPU.
- Para ver el límite de la placa: busca el modelo de CPU en la página del fabricante (Intel ARK o AMD) para confirmar el **socket** y la **RAM máxima y tipo soportados**.

Prueba bajo carga (puede requerir instalar la herramienta, necesita internet): `stress-ng` y `s-tui`.

## 5. Batería (laptops)

```bash
upower -i $(upower -e | grep BAT)    # compara "energy-full" con "energy-full-design"
```

Si `energy-full` es mucho menor que `energy-full-design`, la batería está degradada. En Hiren's PE, HWiNFO también muestra el desgaste.

## 6. Herramientas de Windows (Hiren's PE)

Seguras para mirar: **CPU-Z**, **GPU-Z**, **HWiNFO**, **Speccy**, **CrystalDiskInfo**.

Con cuidado (pueden escribir): recuperación de datos (guarda en **otro** disco), Victoria (solo modo lectura), Check Disk.

No abrir sin necesidad: contraseñas de Windows, particionado, imágenes, reparación de arranque.

Hiren's corre desde la memoria RAM: **guarda los reportes** (por ejemplo HWiNFO → *Save Report*) en la USB o en otro disco antes de apagar.

## 7. Ficha por equipo

Copia esto para cada computadora:

```
Equipo:                     Fecha:
Marca/modelo:
CPU (modelo / socket):
RAM instalada (tipo, módulos):
RAM máxima / ranuras libres:
Memtest86+ (pasadas / errores):
Disco 1 (modelo, tamaño, horas, estado SMART):
Disco 2:
Temperatura CPU reposo / carga:
Batería (si aplica):
Veredicto: usar tal cual / ampliar RAM / cambiar disco / descartar
Compras necesarias:
```
