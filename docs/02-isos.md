# 2. Descargar y verificar las ISO

Descarga siempre de la página **oficial** y verifica la ISO con su checksum. Una ISO corrupta da fallos raros que se confunden con problemas del hardware.

| Programa | Página oficial |
|---|---|
| Memtest86+ | <https://www.memtest.org> → *Linux ISO (64 bits)* (viene en `.zip`; usa el `.iso` de dentro) |
| Fedora Workstation Live | <https://fedoraproject.org/workstation/download> |
| Ubuntu Server LTS | <https://releases.ubuntu.com/> |
| SystemRescue | <https://www.system-rescue.org/Download/> |
| Clonezilla | <https://clonezilla.org/downloads.php> |
| Rescuezilla | <https://github.com/rescuezilla/rescuezilla/releases> |
| ShredOS | <https://github.com/PartialVolume/shredos.x86-64/releases> (usa la versión `x86-64`, no la `i686`) |
| Hiren's BootCD PE | <https://www.hirensbootcd.org/download/> |

❌ No descargues el `.torrent` (Ventoy no lo puede usar) ni copies el `.zip` de memtest.

## Verificar

Cada sitio publica un archivo de sumas (`SHA256SUMS`, `CHECKSUM`, `.sha256`, `.sha1`…). Ejemplo:

```bash
cd ~/Downloads
sha256sum -c SHA256SUMS --ignore-missing     # debe decir: archivo.iso: OK
```

Si el archivo trae solo la suma (sin `-c` compatible):

```bash
sha256sum archivo.iso      # compara el resultado con el de la página
```

Nota: Fedora publica un `CHECKSUM` firmado; `sha256sum -c` puede avisar "N lines are improperly formatted" por el texto de la firma. Es normal si el archivo dice `OK`.
