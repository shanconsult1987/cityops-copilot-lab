from dataclasses import dataclass, asdict


@dataclass
class Incident:
    id: int
    description: str
    severity: str
    status: str = "open"


INCIDENTS = []


def classify_incident(description: str) -> str:
    text = description.lower()

    if any(word in text for word in ["fire", "explosion", "gas leak"]):
        return "critical"

    if any(word in text for word in ["water leak", "power outage", "road blocked"]):
        return "high"

    if any(word in text for word in ["street light", "pothole"]):
        return "medium"

    return "low"


def create_incident(description: str) -> Incident:
    incident = Incident(
        id=len(INCIDENTS) + 1,
        description=description,
        severity=classify_incident(description),
    )

    INCIDENTS.append(incident)
    return incident


def list_incidents():
    return [asdict(incident) for incident in INCIDENTS]


if __name__ == "__main__":
    incident = create_incident(
        "Large water leak near Sector 15"
    )

    print("CityOps Incident Created")
    print(incident)

    print("\nAll incidents:")
    print(list_incidents())