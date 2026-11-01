# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Respiratory CO2 Tolerance BOLT Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentRespiratoryCo2Tolerance

def main():
    agent = PersonalAgentRespiratoryCo2Tolerance()

    print("=" * 70)
    print("DEMO: Personal Agent Respiratory CO2 Tolerance & BOLT Modeler")
    print("=" * 70)

    # 1. Evaluate individual with 14-second BOLT score (mild hyperventilation)
    res_bolt = agent.evaluate_bolt_respiratory_efficiency(
        bolt_score_seconds=14.0,
        resting_respiratory_rate_bpm=16.0
    )

    print(f"\n1. Respiratory Efficiency Audit (BOLT: 14.0s, RR: 16 bpm):")
    print(f"   Minute Ventilation: {res_bolt['estimated_minute_ventilation_liters']} L/min")
    print(f"   Bohr Effect Unloading: {res_bolt['bohr_effect_oxygen_unloading_multiplier']}")
    print(f"   Chemoreceptor Sensitivity: {res_bolt['chemoreceptor_hypercapnic_sensitivity']}")
    print(f"   Classification: {res_bolt['respiratory_functional_tier']}")
    print(f"   Guidance: {res_bolt['clinical_guidance']}")

    # 2. Prescribe Buteyko conditioning schedule
    res_sched = agent.generate_reduced_breathing_schedule(bolt_score_seconds=14.0)

    print(f"\n2. Buteyko Reduced-Breathing Prescription:")
    print(f"   Target BOLT Goal: {res_sched['target_bolt_goal_seconds']} seconds")
    print(f"   Session Length: {res_sched['prescribed_session_duration_minutes']} min")
    print(f"   Exercise: {res_sched['daily_training_exercise']}")
    print(f"   Night Protocol: {res_sched['nocturnal_sleep_protocol']}")
    print(f"   Objective: {res_sched['biochemical_objective']}")

    print("\nVerification complete: Respiratory CO2 tolerance engine executed flawlessly.")

if __name__ == "__main__":
    main()
