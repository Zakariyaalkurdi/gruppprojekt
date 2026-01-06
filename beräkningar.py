def thermostat(T, T_desired):
    """
    Enkel termostat:
    Returnerar 1 om elementet ska vara på, annars 0
    """
    if T < T_desired:
        return 1
    else:
        return 0


def next_temperature(T, T_ute, k_forlust, P, u):
    """
    Beräknar temperaturen nästa timme
    """
    return T + k_forlust * (T_ute - T) + u * P


def run_simulation(
    T_start,
    T_ute,
    T_desired,
    k_forlust,
    P,
    hours):

    """
    Kör simuleringen och returnerar:
    - lista med temperaturer
    - energiförbrukning (antal timmar elementet är på)
    """
    T = T_start
    temperatures = []
    energy = 0

    for _ in range(hours):
        temperatures.append(T)

        u = thermostat(T, T_desired)
        if u == 1:
            energy += 1

        T = next_temperature(T, T_ute, k_forlust, P, u)

    return temperatures, energy
