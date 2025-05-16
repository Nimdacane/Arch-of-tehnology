# ELF
> [!WARNING]
> ВНИМАНИЕ! Если вы видите в описании ***Потом***, свяжитесь с создателем который забыл сделать описание

## ELF header
| Имя           |   Адрес x32/x64   | Размер x32/x64 | Значение     | Описание                                                     |
| ------------- | :---------------: | :------------: | ------------ | ------------------------------------------------------------ |
| EI_MAG        |     `0x0000`      |       4        | `0x7F454C46` | Сигнатура ELF                                                |
| EI_CLASS      |     `0x0004`      |       1        | `0x02`       | Разрядность системы (x64 - `02`, x32 - `01`)                 |
| EI_DATA       |     `0x0005`      |       1        | `0x01`       | Порядок байт (little-endian - `01`, big-endian - `02`)       |
| EI_VERSION    |     `0x0006`      |       1        | `0x01`       | Зарезервировано                                              |
| EI_OSABI      |     `0x0007`      |       1        | `0x00`       | Тип OS/ABI (`00` - System V)                                 |
| EI_ABIVERSION |     `0x0008`      |       1        | `0x00`       | Версия OS/ABI                                                |
| EI_PAD        |     `0x0009`      |       6        | `0x00`       | Зарезервировано                                              |
| e_type        |     `0x0010`      |       2        | `0x02`       | Тип программы ([**Список**](#типы-программы))                |
| e_machine     |     `0x0012`      |       2        | `0x3E`       | Архитектура программы ([**Список**](#архитектуры-программы)) |
| e_version     |     `0x0014`      |       4        | `0x01`       | Зарезервировано                                              |
| e_entry       |     `0x0018`      |      4/8       | `0x401000`   | Виртуальный адрес точки входа                                |
| e_phoff       | `0x001C`/`0x0020` |      4/8       | `0x40`       | Смещение к Program Header                                    |
| e_shoff       | `0x0020`/`0x0028` |      4/8       | `0x0100`     | Смещение к Section Header                                    |
| e_flags       | `0x0024`/`0x0030` |       4        | `0x00`       | Потом                                                        |
| e_ehsize      | `0x0028`/`0x0034` |       2        | `0x40`       | Размер заголовка файла (x64 - `40`, x32 - `34`)              |
| e_phentsize   | `0x002A`/`0x0036` |       2        | `0x38`       | Размер заголовка программы (x64 - `38`, x32 - `20`)          |
| e_phnum       | `0x002C`/`0x0038` |       2        | `0x02`       | Количество заголовков программы                              |
| e_shentsize   | `0x002E`/`0x003A` |       2        | `0x40`       | Размер заголовка секции (x64 - `40`, x32 - `28`)             |
| e_shnum       | `0x0030`/`0x003C` |       2        | `0x05`       | Количество заголовков секций                                 |
| e_shstrndx    | `0x0032`/`0x003E` |       2        | `0x00`       | Потом                                                        |

## Program header
| Имя      | Адрес (относительно смещения) | Значение                  | Описание                                                                    |
| -------- | :---------------------------: | ------------------------- | --------------------------------------------------------------------------- |
| p_type   |      `0x0000` - `0x0004`      | `00 00 00 01`             | Потом                                                                       |
| p_flags  |      `0x0004` - `0x0008`      | `00 00 00 04`             | Возможности сегмента (исполняемый код - `01`, запись - `02`, чтение - `04`) |
| p_offset |      `0x0048` - `0x0050`      | `00 00 00 00 00 00 00 00` | Смещение к сегменту                                                         |
| p_vaddr  |      `0x0050` - `0x0058`      | `00 00 00 00 00 40 00 00` | Виртуальный адрес сегмента                                                  |
| p_paddr  |      `0x0058` - `0x0060`      | `00 00 00 00 00 40 00 00` | Физический адрес сегмента                                                   |
| p_filesz |      `0x0060` - `0x0068`      | `00 00 00 00 00 00 00 B0` | Размер сегмента в файле  (потом)                                            |
| p_memsz  |      `0x0068` - `0x0070`      | `00 00 00 00 00 00 00 B0` | Размер сегмента в памяти (потом)                                            |
| p_align  |      `0x0000` - `0x0000`      | `00 00 00 00 00 00 10 00` | Потом                                                                       |
|          |                               |                           |

# Таблицы
## Типы программы
| Имя     | Значение | Описание                |
| ------- | -------- | ----------------------- |
| ET_REL  | `01`     | Объектный файл          |
| ET_EXEC | `02`     | Приложение              |
| ET_DYN  | `03`     | Динамическая библиотека |
| ET_CORE | `04`     | Файл ядра               |

## Архитектуры программы
| Имя               | Значение          | Описание                                              |
| ----------------- | ----------------- | ----------------------------------------------------- |
| EM_NONE           | `00 00`           | Нет данных об архитектуре                             |
| EM_M32            | `00 01`           | AT&T WE 32100                                         |
| EM_SPARC          | `00 02`           | SPARC                                                 |
| EM_386            | `00 03`           | Intel 80386                                           |
| EM_68K            | `00 04`           | Motorola 68000                                        |
| EM_88K            | `00 05`           | Motorola 88000                                        |
| *зарезервировано* | `00 06`           | Зарезервировано на будуйшее (раньще было EM_486)      |
| EM_860            | `00 07`           | Intel 80860                                           |
| EM_MIPS           | `00 08`           | MIPS I Architecture                                   |
| EM_S370           | `00 09`           | IBM System/370 Processor                              |
| EM_MIPS_RS3_LE    | `00 0A`           | MIPS RS3000 Little-endian                             |
| *зарезервировано* | `00 0B` - `00 0E` | Зарезервировано на будуйшее                           |
| EM_PARISC         | `00 0F`           | Hewlett-Packard PA-RISC                               |
| *зарезервировано* | `00 10`           | Зарезервировано на будуйшее                           |
| EM_VPP500         | `00 11`           | Fujitsu VPP500                                        |
| EM_SPARC32PLUS    | `00 12`           | Enhanced instruction set SPARC                        |
| EM_960            | `00 13`           | Intel 80960                                           |
| EM_PPC            | `00 14`           | PowerPC                                               |
| EM_PPC64          | `00 15`           | 64-bit PowerPC                                        |
| EM_S390           | `00 16`           | IBM System/390                                        |
| *зарезервировано* | `00 17` - `00 23` | Зарезервировано на будуйшее                           |
| EM_V800           | `00 24`           | NEC V800                                              |
| EM_FR20           | `00 25`           | Fujitsu FR20                                          |
| EM_RH32           | `00 26`           | TRW RH-32                                             |
| EM_RCE            | `00 27`           | Motorola RCE                                          |
| EM_ARM            | `00 28`           | Расшириные RISC устройства ARM                        |
| EM_ALPHA          | `00 29`           | Digital Alpha                                         |
| EM_SH             | `00 2A`           | Hitachi SH                                            |
| EM_SPARCV9        | `00 2B`           | SPARC Version 9                                       |
| EM_TRICORE        | `00 2C`           | Встроенный Siemens TriCore                            |
| EM_ARC            | `00 2D`           | Argonaut RISC Core, Argonaut Technologies Inc.        |
| EM_H8_300         | `00 2E`           | Hitachi H8/300                                        |
| EM_H8_300H        | `00 2F`           | Hitachi H8/300H                                       |
| EM_H8S            | `00 30`           | Hitachi H8S                                           |
| EM_H8_500         | `00 31`           | Hitachi H8/500                                        |
| EM_IA_64          | `00 32`           | Intel IA-64                                           |
| EM_MIPS_X         | `00 33`           | Stanford MIPS-X                                       |
| EM_COLDFIRE       | `00 34`           | Motorola ColdFire                                     |
| EM_68HC12         | `00 35`           | Motorola M68HC12                                      |
| EM_MMA            | `00 36`           | Мультимедийный ускоритель Fujitsu MMA                 |
| EM_PCP            | `00 37`           | Siemens PCP                                           |
| EM_NCPU           | `00 38`           | Встроенный Sony nCPU RISC                             |
| EM_NDR1           | `00 39`           | Микропроцессор Denso NDR1                             |
| EM_STARCORE       | `00 3A`           | Motorola Star*Core                                    |
| EM_ME16           | `00 3B`           | Toyota ME16                                           |
| EM_ST100          | `00 3C`           | STMicroelectronics ST100                              |
| EM_TINYJ          | `00 3D`           | Расширинное семейство встроенных Logic Corp. TinyJ    |
| EM_X86_64         | `00 3E`           | AMD x86-64                                            |
| EM_PDSP           | `00 3F`           | Sony DSP                                              |
| EM_PDP10          | `00 40`           | Digital Equipment Corp. PDP-10                        |
| EM_PDP11          | `00 41`           | Digital Equipment Corp. PDP-11                        |
| EM_FX66           | `00 42`           | Микроконтроллер Siemens FX66                          |
| EM_ST9PLUS        | `00 43`           | Микроконтроллер STMicroelectronics ST9+ 8/16 bit      |
| EM_ST7            | `00 44`           | Микроконтроллер STMicroelectronics ST7 8-bit          |
| EM_68HC16         | `00 45`           | Микроконтроллер Motorola MC68HC16                     |
| EM_68HC11         | `00 46`           | Микроконтроллер Motorola MC68HC11                     |
| EM_68HC08         | `00 47`           | Микроконтроллер Motorola MC68HC08                     |
| EM_68HC05         | `00 48`           | Микроконтроллер Motorola MC68HC05                     |
| EM_SVX            | `00 49`           | Silicon Graphics SVx                                  |
| EM_ST19           | `00 4A`           | Микроконтроллер STMicroelectronics ST19 8-bit         |
| EM_VAX            | `00 4B`           | Digital VAX                                           |
| EM_CRIS           | `00 4C`           | Встроенный процессор Axis Communications 32-bit       |
| EM_JAVELIN        | `00 4D`           | Встроенный процессор Infineon Technologies 32-bit     |
| EM_FIREPATH       | `00 4E`           | Element 14 64-bit DSP                                 |
| EM_ZSP            | `00 4F`           | LSI Logic 16-bit DSP                                  |
| EM_MMIX           | `00 50`           | Donald Knuth's educational 64-bit                     |
| EM_HUANY          | `00 51`           | Независимые объектные файлы Гарвардского университета |
| EM_PRISM          | `00 52`           | SiTera Prism                                          |
| EM_AVR            | `00 53`           | Микроконтроллер Atmel AVR 8-bit                       |
| EM_FR30           | `00 54`           | Fujitsu FR30                                          |
| EM_D10V           | `00 55`           | Mitsubishi D10V                                       |
| EM_D30V           | `00 56`           | Mitsubishi D30V                                       |
| EM_V850           | `00 57`           | NEC v850                                              |
| EM_M32R           | `00 58`           | Mitsubishi M32R                                       |
| EM_MN10300        | `00 59`           | Matsushita MN10300                                    |
| EM_MN10200        | `00 5A`           | Matsushita MN10200                                    |
| EM_PJ             | `00 5B`           | picoJava                                              |
| EM_OPENRISC       | `00 5C`           | Встроенный процессор OpenRISC 32-bit                  |
| EM_ARC_A5         | `00 5D`           | ARC ядра Tangent-A5                                   |
| EM_XTENSA         | `00 5E`           | Tensilica Xtensa                                      |
| EM_VIDEOCORE      | `00 5F`           | Alphamosaic VideoCore                                 |
| EM_TMM_GPP        | `00 60`           | Мультимедийный процессор общего назначения Thompson   |
| EM_NS32K          | `00 61`           | Национальные Semiconductor 32000 серии                |
| EM_TPC            | `00 62`           | Tenor Network TPC                                     |
| EM_SNP1K          | `00 63`           | Trebia SNP 1000                                       |
| EM_ST200          | `00 64`           | Микроконтроллер STMicroelectronics ST200              |

# Ресурсы
- https://refspecs.linuxfoundation.org/elf/gabi4+/ch4.eheader.html
- https://ru.wikipedia.org/wiki/Executable_and_Linkable_Format
