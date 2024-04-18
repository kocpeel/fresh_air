def validate_temperatura(temperatura):
    if temperatura < -50 or temperatura > 50:
        raise ValueError("Nieprawidłowa temperatura")

def validate_ciagnienie(ciagnienie):
    if ciagnienie < 700 or ciagnienie > 1100:
        raise ValueError("Nieprawidłowe ciśnienie")