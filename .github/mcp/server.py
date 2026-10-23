from mcp.server.fastmcp import FastMCP


mcp = FastMCP("cityops-prime")


MISSIONS = {
    "INC-001": {
        "status": "investigating",
        "team": "Water Operations",
        "location": "Sector 15",
    },
    "INC-002": {
        "status": "open",
        "team": "Traffic Operations",
        "location": "Sector 21",
    },
}


@mcp.tool()
def get_mission_status(incident_id: str) -> dict:
    """Return operational status for a CityOps incident."""

    incident = MISSIONS.get(incident_id)

    if not incident:
        return {
            "found": False,
            "incident_id": incident_id,
        }

    return {
        "found": True,
        "incident_id": incident_id,
        **incident,
    }


if __name__ == "__main__":
    mcp.run()