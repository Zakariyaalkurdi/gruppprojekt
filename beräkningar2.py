def termostat(T1, T_desired):
    """Termostat för rum 1: returnerar 1 om elementet ska vara på"""
    if T1 < T_desired:
        return 1
    else:
        return 0

def next_temperatures(T1, T2, T_ute, k_vagg, k_forlust1, k_forlust2, P, u):
    """
    Beräknar nästa timmes temperaturer för båda rummen
    
    Rum 1 (med element):
    T1_ny = T1 + k_vagg*(T2 - T1) + k_forlust1*(T_ute - T1) + u*P
    
    Rum 2 (utan element):
    T2_ny = T2 + k_vagg*(T1 - T2) + k_forlust2*(T_ute - T2)
    """
    # Rum 1
    T1_ny = (T1 + 
             k_vagg * (T2 - T1) + 
             k_forlust1 * (T_ute - T1) + 
             u * P)
    
    # Rum 2  
    T2_ny = (T2 + 
             k_vagg * (T1 - T2) + 
             k_forlust2 * (T_ute - T2))
    
    return T1_ny, T2_ny

def run_simulation_two_rooms(T1_start, T2_start, T_ute, T_desired, 
                            k_vagg, k_forlust1, k_forlust2, P, hours):
    """
    Simulerar två rum och returnerar:
    - lista med T1 temperaturer
    - lista med T2 temperaturer  
    - energiförbrukning (timmar element på i rum 1)
    """
    T1, T2 = T1_start, T2_start
    temps1, temps2 = [T1_start], [T2_start]
    energy = 0
    
    for _ in range(hours):
        u = termostat(T1, T_desired)
        if u == 1:
            energy += 1
            
        T1_ny, T2_ny = next_temperatures(T1, T2, T_ute, k_vagg, 
                                       k_forlust1, k_forlust2, P, u)
        
        temps1.append(T1_ny)
        temps2.append(T2_ny)
        T1, T2 = T1_ny, T2_ny
    
    return temps1, temps2, energy

       