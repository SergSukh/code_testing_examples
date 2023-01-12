from hospital import (calculate_statistics, check_patient, discharge,
                      err_except, get_status, status_down, status_up, stop)

CMD = {
    "узнать статус пациента": get_status,
    "get status": get_status,
    "повысить статус пациента": status_up,
    "status up": status_up,
    "понизить статус пациента": status_down,
    "status down": status_down,
    "выписать пациента": discharge,
    "discharge": discharge,
    "рассчитать статистику": calculate_statistics,
    "calculate statistics": calculate_statistics,
    'Желаете этого клиента выписать? (да/нет): ': check_patient,
    "стоп": stop,
    "stop": stop,
    "error": err_except,
}