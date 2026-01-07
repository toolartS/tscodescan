# tscodescan

`tscodescan` adalah CLI tool untuk memindai repository dan menghasilkan **artefak konteks yang AI-friendly**.
Tool ini dirancang untuk workflow berbasis terminal (Linux / Termux) dan fokus pada **struktur, makna, dan konteks repository**, bukan sekadar dump file.

---

## Konsep Utama

`tscodescan` membedakan antara **scan isi**, **analisis struktur**, dan **diagnosis repository**.

- **Scan** → isi file (artefak utama)
- **Summary** → identitas & makna repository
- **Tree** → struktur direktori
- **Raw** → dump tanpa filter
- **Doctor** → diagnosis & maintenance

---

## Instalasi

```bash
pip install tscodescan
```

Atau mode development:

```bash
pip install -e .
```

---

## Penggunaan Dasar

```bash
tscodescan
```

Default scan menghasilkan **document scan** (artefak utama) berisi:
- struktur file
- isi source code (text-based)
- ignore otomatis untuk folder noise

Output disimpan ke:

```
~/storage/downloads/Scan/<repo>/
```

---

## Modes & Flags

### Document Scan (Default)
```bash
tscodescan
```

### Tree (CLI Only)
```bash
tscodescan --tree
```

### Tree File
```bash
tscodescan --tf
```

### Raw Scan
```bash
tscodescan --raw
```

### Summary (Analisis Struktur)
```bash
tscodescan --summary
```

Summary menganalisis:
- tipe repository
- komposisi bahasa
- sinyal dokumentasi (heading Markdown)
- sinyal kematangan repo

### Doctor (Diagnosis Repository)
```bash
tscodescan --doctor
```

### ID Marker
```bash
tscodescan --raw -i 3
```

---

## Filosofi Desain

- CLI-first
- Terminal-friendly (Termux compatible)
- Artefak sebagai source of context
- Git sebagai source of truth

---

## Lisensi

MIT
