class Proizvoditel:
    def __init__(self, kod, nazvanie):
        self.kod = kod
        self.nazvanie = nazvanie

    def __str__(self):
        return f"{self.kod}: {self.nazvanie}"

class Remont:
    def __init__(self, kod, kod_klienta, kod_tehniki, kod_kategorii, nazvanie_tehniki, data_obr, data_isp):
        self.kod = kod
        self.kod_klienta = kod_klienta
        self.kod_tehniki = kod_tehniki
        self.kod_kategorii = kod_kategorii
        self.nazvanie_tehniki = nazvanie_tehniki
        self.data_obr = data_obr
        self.data_isp = data_isp

    def __str__(self):
        status = "Выполнен" if self.data_isp else "Не выполнен"
        return f"{self.kod}: {self.nazvanie_tehniki} ({status})"
