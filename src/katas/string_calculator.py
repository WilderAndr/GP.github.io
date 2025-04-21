def add(numbers):
    """
    Kata 1: String Calculator
    TDD implementación del famoso ejercicio de String Calculator
    """
    if not numbers:
        return 0
    
    # Implementación inicial básica
    return sum(map(int, numbers.split(',')))
