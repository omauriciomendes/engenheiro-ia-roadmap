from typing import Any


def check_drift(reference_stats: dict[str, Any], live_stats: dict[str, Any]) -> dict[str, Any]:
    alerts = {}
    for k, ref in reference_stats.items():
        live = live_stats.get(k, ref)
        delta = abs(live - ref) / max(ref, 1e-6)
        if delta > 0.2:
            alerts[k] = {"ref": ref, "live": live, "delta": delta}
    return alerts


if __name__ == "__main__":
    ref = {"bpm_avg": 120.0, "energia_avg": 0.6}
    live = {"bpm_avg": 132.0, "energia_avg": 0.5}
    print(check_drift(ref, live))
