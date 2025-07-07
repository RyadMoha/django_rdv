from datetime import datetime, timedelta, time

def generer_creneaux(start=time(9, 0), end=time(18, 0), interval_minutes=30):
    """
    Génère une liste de créneaux horaires entre start et end (heures),
    espacés de interval_minutes minutes.
    """
    creneaux = []
    # On part d'une date fictive, seule l'heure compte ici
    base_date = datetime.today().date()
    current = datetime.combine(base_date, start)
    end_dt = datetime.combine(base_date, end)

    while current < end_dt:
        creneaux.append(current.time())
        current += timedelta(minutes=interval_minutes)
    return creneaux
