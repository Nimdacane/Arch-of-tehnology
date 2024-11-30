def ret_file():
    try:
        path = input("\033[3;32mEnter the path: \033[0m")
        return open(path, "rb")
    except:
        print('\033[5;33mIncorrect path!\033[0m')
        input()
        return ret_file()


file = ret_file().read()

sections = [".idata", ".text", ".data", ".bss", ".rdata", ".didat", ".pdata", ".pdata", ".xdata", ".CRT", ".tls",
            ".rsrc", ".reloc"]

in_file_sections = {}

for section in sections:  # fill the array
    try:  # if this section's in the file
        addrOFrealSize = file.decode("cp866").index(section) + 0x8 + 0x8  # Address of r_size
        realSizeBytes = file[addrOFrealSize:addrOFrealSize + 0x4]  # r_size bytes
        realSize = realSizeBytes[0] * 4096 + realSizeBytes[1] * 256 + realSizeBytes[2] * 16 + realSizeBytes[3]  # r_size
        addrOFvirtualSize = file.decode("cp866").index(section) + 0x8 + 0x0  # Address of v_size
        virtualSizeBytes = file[addrOFvirtualSize:addrOFvirtualSize + 0x4]  # v_size bytes
        virtualSize = virtualSizeBytes[0] * 4096 + virtualSizeBytes[1] * 256 + virtualSizeBytes[2] * 16 + \
                      virtualSizeBytes[3]  # v_size bytes
        addrOFrealAddr = file.decode("cp866").index(section) + 0x8 + 0xC  # Address of r_addr
        realAddrBytes = file[addrOFrealAddr:addrOFrealAddr + 0x4]  # r_addr bytes
        realAddr = realAddrBytes[0] * 4096 + realAddrBytes[1] * 256 + realAddrBytes[2] * 16 + realAddrBytes[3]  # r_addr
        addrOFvirtualAddr = file.decode("cp866").index(section) + 0x8 + 0x4  # Address of v_addr
        virtualAddrBytes = file[addrOFvirtualAddr:addrOFvirtualAddr + 0x4]  # v_addr bytes
        virtualAddr = virtualAddrBytes[0] * 4096 + virtualAddrBytes[1] * 256 + virtualAddrBytes[2] * 16 + virtualAddrBytes[3]  # v_addr

        in_file_sections[section] = {'r_addr': hex(realAddr), 'v_addr': hex(virtualAddr), 'r_size': hex(realSize),
                                     'v_size': hex(virtualSize)}
    except ValueError:  # if this section's not in the file
        pass

for section_name in sections:  # fill the array
    if section_name in in_file_sections:  # if this section's in the file
        data = in_file_sections[section_name]
        print(
            f"\033[1;32m{section_name}\033[0m:\t" +
            f"\033[3;31mreal address \033[1m{data['r_addr']}\033[0m,\t" +
            f"\033[3;33mvirtual address \033[1m{data['v_addr']}\033[0m,\t" +
            f"\033[3;34mreal size \033[1m{data['r_size']}\033[0m,\t" +
            f"\033[3;36mvirtual size \033[1m{data['v_size']}\033[0m"
        )
    else:  # if this section's not in the file
        print(
            f"\033[1;32m{section_name}\033[0m:\t"
            f"\033[5;36mmissing\033[0m"
        )
