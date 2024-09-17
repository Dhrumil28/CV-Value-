
def calculate_cv_liquids(Q, G, delta_P):
    
    Cv = Q * (G / delta_P) ** 0.5
    return Cv

def calculate_cv_gases(Q, T, Z, P1, G, delta_P):
    
    Cv = Q * ((T * Z) / (P1 * G)) ** 0.5 / (delta_P ** 0.5)
    return Cv

def calculate_cv_steam(W, P1, P2, delta_P):
    
    Cv = W / ((delta_P * (P1 + P2)) ** 0.5)
    return Cv

# Example usage:

Medium = input("Enter the flow medium :- ")

if Medium == 'Liquid':
    # For Liquids
    Q_liquids = float(input("Enter the flow rate (gpm): "))
    G_liquids = float(input("Enter the specific gravity of the fluid: "))
    delta_P_liquids = float(input("Enter the pressure drop across the valve (psi): "))

    Cv_liquids = calculate_cv_liquids(Q_liquids, G_liquids, delta_P_liquids)
    print(f"Cv for liquids: {Cv_liquids:.2f}")

elif Medium == 'Gas':
    # For Gases
    Q_gases = float(input("\nEnter the flow rate (SCFM): "))
    T_gases = float(input("Enter the absolute temperature (Rankine): "))
    Z_gases = float(input("Enter the compressibility factor (dimensionless): "))
    P1_gases = float(input("Enter the upstream pressure (psia): "))
    G_gases = float(input("Enter the specific gravity of the gas (relative to air): "))
    delta_P_gases = float(input("Enter the pressure drop across the valve (psi): "))
    Cv_gases = calculate_cv_gases(Q_gases, T_gases, Z_gases, P1_gases, G_gases, delta_P_gases)
    print(f"Cv for gases: {Cv_gases:.2f}")

elif Medium == 'Steam':
    # For Steam
    W_steam = float(input("\nEnter the mass flow rate of steam (lb/hr): "))
    P1_steam = float(input("Enter the upstream absolute pressure (psia): "))
    P2_steam = float(input("Enter the downstream absolute pressure (psia): "))
    delta_P_steam = float(input("Enter the pressure drop across the valve (psi): "))
    Cv_steam = calculate_cv_steam(W_steam, P1_steam, P2_steam, delta_P_steam)
    print(f"Cv for steam: {Cv_steam:.2f}")
else:
    print("Enter Proper Input")