# gdb -x solver.py souk

import gdb

cmp_addr = 0x00005555555555b2
gdb.execute(f"b*{cmp_addr}")

passwd = list("."*70)
i_range = list(range(70))
for n in range(71):
    padding = list("."*70)
    gdb.execute(f"run < <(echo -ne {''.join(padding)})")
    for _ in range(n):
        gdb.execute("c")
        
    bad_rdx = gdb.parse_and_eval("$rdx")

    for i in i_range:
        tmp_padding = padding.copy()
        tmp_padding[i] = "B"
        payload = "".join(tmp_padding)
        gdb.execute(f"run < <(echo -ne {payload})")
        for _ in range(n):
            gdb.execute("c")

        rdx = gdb.parse_and_eval("$rdx")
        rax = gdb.parse_and_eval("$rax")
        if rdx != bad_rdx:
            index = i
            i_range.remove(i)
            break

    passwd[i] = chr(ord('B')+(rax-rdx))

    open("flag.txt", "w").write(''.join(passwd))

gdb.execute("q")

# FCSC{665cfa3e0277a889258cc9f6e24c88fc9db654178558de101b8a19af8fb00575}
