import matplotlib.pyplot as plt
from beräkningar import run_simulation

# Gemensamma värden
T_start = 17
T_ute = -5
hours = 48

# =========================
# EXPERIMENT 1 – Referensfall
# =========================
temps1, energy1 = run_simulation(
    T_start=T_start,
    T_ute=T_ute,
    T_desired=21,
    k_forlust=0.05,
    P=1.4,
    hours=hours
)

# =========================
# EXPERIMENT 2 – Bättre isolering
# =========================
temps2, energy2 = run_simulation(
    T_start=T_start,
    T_ute=T_ute,
    T_desired=21,
    k_forlust=0.02,
    P=1.4,
    hours=hours
)

# =========================
# EXPERIMENT 3 – Sämre isolering
# =========================
temps3, energy3 = run_simulation(
    T_start=T_start,
    T_ute=T_ute,
    T_desired=21,
    k_forlust=0.10,
    P=1.4,
    hours=hours
)

# =========================
# EXPERIMENT 4 – Lägre önskad temperatur
# =========================
temps4, energy4 = run_simulation(
    T_start=T_start,
    T_ute=T_ute,
    T_desired=19,
    k_forlust=0.05,
    P=1.4,
    hours=hours
)

# =========================
# EXPERIMENT 5 – Effektivare element
# =========================
temps5, energy5 = run_simulation(
    T_start=T_start,
    T_ute=T_ute,
    T_desired=21,
    k_forlust=0.05,
    P=2.0,
    hours=hours
)

# =========================
# Utskrift av energiförbrukning
# =========================
print("Energiförbrukning (timmar):")
print("Experiment 1 – Referensfall:", energy1)
print("Experiment 2 – Bättre isolering:", energy2)
print("Experiment 3 – Sämre isolering:", energy3)
print("Experiment 4 – Lägre temperatur:", energy4)
print("Experiment 5 – Effektivare element:", energy5)

# =========================
# Plottar (en graf per experiment)
# =========================
experiments = [
    (temps1, "Experiment 1 – Referensfall"),
    (temps2, "Experiment 2 – Bättre isolering"),
    (temps3, "Experiment 3 – Sämre isolering"),
    (temps4, "Experiment 4 – Lägre temperatur"),
    (temps5, "Experiment 5 – Effektivare element"),
]

for temps, title in experiments:
    plt.figure()
    plt.plot(range(hours), temps)
    plt.xlabel("Tid (timmar)")
    plt.ylabel("Temperatur (°C)")
    plt.title(title)
    plt.grid()
    plt.show()
