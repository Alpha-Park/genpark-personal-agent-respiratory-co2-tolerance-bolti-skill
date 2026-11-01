# -*- coding: utf-8 -*-
"""FastMCP Server for Personal Agent Respiratory CO2 Tolerance BOLT Skill."""

from mcp.server.fastmcp import FastMCP
from client import PersonalAgentRespiratoryCo2Tolerance

mcp = FastMCP("PersonalAgentRespiratoryCo2Tolerance")
client = PersonalAgentRespiratoryCo2Tolerance()

@mcp.tool()
def evaluate_bolt_respiratory_efficiency(
    bolt_score_seconds: float,
    resting_respiratory_rate_bpm: float = 14.0
) -> str:
    """Evaluates BOLT score, Bohr effect tissue oxygenation, and chemoreceptor sensitivity."""
    import json
    return json.dumps(client.evaluate_bolt_respiratory_efficiency(bolt_score_seconds, resting_respiratory_rate_bpm), indent=2)

@mcp.tool()
def generate_reduced_breathing_schedule(
    bolt_score_seconds: float
) -> str:
    """Prescribes Buteyko reduced-breathing conditioning exercises to elevate CO2 tolerance."""
    import json
    return json.dumps(client.generate_reduced_breathing_schedule(bolt_score_seconds), indent=2)

if __name__ == "__main__":
    mcp.run()
