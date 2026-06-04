INC_P1 = 2
INC_P2 = 4
INC_P3 = 5


def clock(global_time, increment):
    return global_time * increment


print("=== BEZ LAMPORTOVOG ALGORITMA ===")

t_send_m1 = 2
p1_send_m1 = clock(t_send_m1, INC_P1)
print("P1 šalje m1:", p1_send_m1)

t_recv_m1 = t_send_m1 + 2
p2_recv_m1 = clock(t_recv_m1, INC_P2)
print("P2 prima m1:", p2_recv_m1)

t_send_m2 = t_recv_m1 + 3
p2_send_m2 = clock(t_send_m2, INC_P2)
print("P2 šalje m2:", p2_send_m2)

t_recv_m2 = t_send_m2 + 2
p3_recv_m2 = clock(t_recv_m2, INC_P3)
print("P3 prima m2:", p3_recv_m2)

t_send_m3 = t_recv_m2 + 2
p3_send_m3 = clock(t_send_m3, INC_P3)
print("P3 šalje odgovor:", p3_send_m3)

t_recv_m3 = t_send_m3 + 2
p2_recv_m3 = clock(t_recv_m3, INC_P2)
print("P2 prima odgovor:", p2_recv_m3)

t_send_m4 = t_recv_m3 + 3
p2_send_m4 = clock(t_send_m4, INC_P2)
print("P2 šalje m4:", p2_send_m4)

t_recv_m4 = t_send_m4 + 2
p1_recv_m4 = clock(t_recv_m4, INC_P1)
print("P1 prima m4:", p1_recv_m4)

print("Rezultat bez Lamporta:", p1_recv_m4)


print("\n=== SA LAMPORTOVIM ALGORITMOM ===")

C1 = clock(2, INC_P1)
m1 = C1
print("P1 šalje m1:", m1)

C2 = clock(4, INC_P2)
C2 = max(C2, m1) + INC_P2
print("P2 prima m1:", C2)

C2 = C2 + 3 * INC_P2
m2 = C2
print("P2 šalje m2:", m2)

C3 = clock(9, INC_P3)
C3 = max(C3, m2) + INC_P3
print("P3 prima m2:", C3)

C3 = C3 + 2 * INC_P3
m3 = C3
print("P3 šalje odgovor:", m3)

C2_normal = clock(13, INC_P2)
C2 = max(C2_normal, m3) + INC_P2
print("P2 prima odgovor:", C2)

C2 = C2 + 3 * INC_P2
m4 = C2
print("P2 šalje m4:", m4)

C1_normal = clock(18, INC_P1)
C1 = max(C1_normal, m4) + INC_P1
print("P1 prima m4:", C1)

print("Rezultat sa Lamportom:", C1)