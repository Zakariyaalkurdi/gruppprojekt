import matplotlib.pyplot as plt
from beräkningar2 import run_simulation_two_rooms

# Gemensamma värden för Program 2
hours = 48
T_ute = -5
T1_start = 17
T2_start = 15
T_desired = 21

# =========================
# EXPERIMENT 1 – Referensfall (två rum)
# =========================
temps1_1, temps2_1, energy1 = run_simulation_two_rooms(
    T1_start, T2_start, T_ute, T_desired,
    k_vagg=0.9, k_forlust1=0.02, k_forlust2=0.02, P=2.0, hours=hours
)

# =========================
# EXPERIMENT 2 – Lägre värmeöverföring mellan rum
# =========================
temps1_2, temps2_2, energy2 = run_simulation_two_rooms(
    T1_start, T2_start, T_ute, T_desired,
    k_vagg=0.3, k_forlust1=0.02, k_forlust2=0.02, P=2.0, hours=hours
)

# =========================
# EXPERIMENT 3 – Sämre isolering i båda rummen
# =========================
temps1_3, temps2_3, energy3 = run_simulation_two_rooms(
    T1_start, T2_start, T_ute, T_desired,
    k_vagg=0.9, k_forlust1=0.05, k_forlust2=0.05, P=2.0, hours=hours
)

# =========================
# EXPERIMENT 4 – Öka isolering i rum 2 (från exp 3)
# =========================
temps1_4, temps2_4, energy4 = run_simulation_two_rooms(
    T1_start, T2_start, T_ute, T_desired,
    k_vagg=0.9, k_forlust1=0.05, k_forlust2=0.02, P=2.0, hours=hours
)

# =========================
# Utskrift
# =========================
print("Program 2 - Energiförbrukning (timmar element rum 1 på):")
print(f"Exp 1 Referensfall: {energy1}")
print(f"Exp 2 Lägre k_vägg: {energy2}")
print(f"Exp 3 Sämre isolering båda: {energy3}")
print(f"Exp 4 Bättre isolering rum 2: {energy4}")

# =========================
# Grafer: Två kurvor i samma fönster per experiment
# =========================
experiments = [
    ((temps1_1, temps2_1), "Exp 1 – Referensfall"),
    ((temps1_2, temps2_2), "Exp 2 – Lägre värmeöverföring"),
    ((temps1_3, temps2_3), "Exp 3 – Sämre isolering båda"),
    ((temps1_4, temps2_4), "Exp 4 – Bättre isolering rum 2")
]

tid = list(range(len(temps1_1)))

for (temps1, temps2), title in experiments:
    plt.figure(figsize=(10, 6))
    plt.plot(tid, temps1, label="Rum 1 (med element)", linewidth=2)
    plt.plot(tid, temps2, label="Rum 2 (utan element)", linewidth=2)
    plt.xlabel("Tid (timmar)")
    plt.ylabel("Temperatur (°C)")
    plt.title(f"Program 2: {title}")
    plt.legend()
    plt.grid(True)
    plt.show()
