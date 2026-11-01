# -*- coding: utf-8 -*-
"""
Personal Agent Respiratory CO2 Tolerance BOLT Client
Zero-dependency Body Oxygen Level Test (BOLT) calculator, Bohr effect tissue oxygenation
modeler, hypercapnic chemoreceptor sensitivity tracker, and Buteyko breathing scheduler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentRespiratoryCo2Tolerance:
    """
    Quantifies arterial carbon dioxide tolerance, central/peripheral chemoreceptor sensitivity,
    Bohr effect hemoglobin oxygen unloading dynamics, and Buteyko reduced-breathing protocols.
    """

    def evaluate_bolt_respiratory_efficiency(
        self,
        bolt_score_seconds: float,
        resting_respiratory_rate_bpm: float = 14.0
    ) -> Dict[str, Any]:
        """
        Evaluates the Body Oxygen Level Test (BOLT score): the duration in seconds from the end
        of a normal exhalation until the first definitive physiological impulse to breathe.
        Higher BOLT indicates higher arterial pCO2 tolerance and enhanced Bohr effect O2 delivery.
        """
        bolt = max(2.0, min(120.0, float(bolt_score_seconds)))
        rr = max(4.0, min(35.0, float(resting_respiratory_rate_bpm)))

        # Bohr Effect tissue oxygen release efficiency multiplier
        # High CO2 shifts oxyhemoglobin dissociation curve to the right, freeing oxygen for mitochondria
        bohr_efficiency_multiplier = round(min(1.85, 0.65 + (bolt / 40.0) * 0.70), 2)

        # Minute ventilation estimate in Liters/min (Normal: 5-7 L/min; Over-breathers: 10-15 L/min)
        # Low BOLT strongly correlates with hyperventilation tidal volume inflation
        est_tidal_volume_ml = round(400.0 + max(0.0, (25.0 - bolt) * 15.0), 0)
        minute_ventilation_liters = round((rr * est_tidal_volume_ml) / 1000.0, 1)

        # Chemoreceptor sensitivity and functional status classification
        if bolt >= 40.0:
            status = "Elite Respiratory Fitness & High Parasympathetic Tone"
            chemo_sens = "Low (Highly blunted hypercapnic alarm; exceptional endurance base)"
            guidance = "Maintain current nasal-only athletic training and functional breathing."
        elif bolt >= 30.0:
            status = "Optimal Functional Breathing Baseline"
            chemo_sens = "Normal (Balanced arterial pCO2 ~40 mmHg; robust Bohr effect delivery)"
            guidance = "Ideal day-to-day CO2 tolerance. Excellent recovery and deep sleep architecture."
        elif bolt >= 20.0:
            status = "Moderate Respiratory Efficiency (Sub-Optimal Aerobic Reserve)"
            chemo_sens = "Mildly Hypersensitive (Occasional sighing, exercise breathlessness)"
            guidance = "Introduce 15 minutes of daily Buteyko reduced-volume nasal breathing exercises."
        elif bolt >= 10.0:
            status = "Chronic Over-Breathing / Subclinical Hyperventilation"
            chemo_sens = "Hyperactive (Chemoreceptors trigger panic/gasp at low pCO2 thresholds)"
            guidance = "Enforce 100% strict daytime nasal breathing and nocturnal mouth taping."
        else:
            status = "Severe Respiratory Alkalosis / Extreme CO2 Sensitivity"
            chemo_sens = "Critical Hypersensitivity (High resting sympathetic arousal, frequent yawning)"
            guidance = "Urgent breath re-education: Short gentle nasal breathing intervals, zero mouth breathing."

        return {
            "measured_bolt_score_seconds": bolt,
            "resting_respiratory_rate_bpm": rr,
            "estimated_minute_ventilation_liters": minute_ventilation_liters,
            "bohr_effect_oxygen_unloading_multiplier": f"{bohr_efficiency_multiplier}x tissue delivery",
            "chemoreceptor_hypercapnic_sensitivity": chemo_sens,
            "respiratory_functional_tier": status,
            "clinical_guidance": guidance
        }

    def generate_reduced_breathing_schedule(
        self,
        bolt_score_seconds: float
    ) -> Dict[str, Any]:
        """
        Prescribes structured daily Buteyko reduced-volume breathing exercises and nasal
        conditioning intervals to progressively upregulate carbon dioxide tolerance.
        """
        bolt = max(2.0, min(80.0, float(bolt_score_seconds)))

        if bolt < 15.0:
            pause_sec = 3.0
            reps = 6
            session_mins = 10.0
            exercise_desc = "Gentle Nasal Inhale (2s) -> Passive Nasal Exhale (3s) -> Relaxed Hold (3s). Repeat for 10 min."
        elif bolt < 30.0:
            pause_sec = 5.0
            reps = 8
            session_mins = 15.0
            exercise_desc = "Nasal Inhale (2s) -> Passive Exhale (3s) -> Hold (5s) -> Air Hunger Breathing (30s). Repeat for 15 min."
        else:
            pause_sec = 10.0
            reps = 10
            session_mins = 20.0
            exercise_desc = "Paced Nasal Walking with 10-step breath holds every minute to simulate high-altitude hypoxia."

        return {
            "current_bolt_score_seconds": bolt,
            "target_bolt_goal_seconds": 40.0,
            "prescribed_session_duration_minutes": session_mins,
            "breath_hold_cadence_seconds": pause_sec,
            "daily_training_exercise": exercise_desc,
            "nocturnal_sleep_protocol": "Apply micropore surgical tape over lips during sleep to enforce nocturnal nasal nitric oxide synthesis.",
            "biochemical_objective": "Gradually reset medullary respiratory chemoreceptors to tolerate higher arterial PaCO2."
        }
