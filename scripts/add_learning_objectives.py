#!/usr/bin/env python3
"""
Add learning objectives sections to lessons that are missing them
"""
import os
import glob
import re
from pathlib import Path

BASE_DIR = "/Users/a3015110/Desktop/IB45PLS/subjects"

OBJECTIVES_TEMPLATE = '''<div class="objectives" style="background: #f0f4ff; border-left: 4px solid #2563eb; padding: 1rem 1.2rem; margin: 1.5rem 0; border-radius: 0 8px 8px 0;">
    <h3 style="margin-top: 0; color: #1e40af;">Learning Objectives</h3>
    <p>By the end of this lesson, you will be able to:</p>
    <ul>
        {objectives_list}
    </ul>
</div>
'''

def extract_lesson_title(content):
    """Extract the lesson title from h1 tag"""
    match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    if match:
        title = re.sub(r'<[^>]+>', '', match.group(1))  # Strip HTML tags
        return title.strip()
    return "this lesson"

def extract_main_headings(content):
    """Extract h2 and h3 headings to infer objectives"""
    headings = []
    # Find h2 headings
    for match in re.finditer(r'<h2[^>]*>(.*?)</h2>', content, re.DOTALL):
        heading = re.sub(r'<[^>]+>', '', match.group(1)).strip()
        if heading and not heading.startswith('Learning Objectives'):
            headings.append(heading)
    return headings[:5]  # Limit to first 5 headings

def generate_objectives(title, headings):
    """Generate learning objectives based on title and headings"""
    objectives = []

    # Add a general objective based on title
    if title and title != "this lesson":
        # Clean up title
        clean_title = re.sub(r'^Lesson \d+[:\-—\s]+', '', title, flags=re.IGNORECASE)
        clean_title = re.sub(r'\s+—\s+.*$', '', clean_title)  # Remove subtitle after dash
        objectives.append(f"<li><strong>Understand</strong> the key concepts in {clean_title}</li>")

    # Add objectives based on main headings
    for heading in headings[:3]:  # Use up to 3 headings
        heading_clean = re.sub(r'^\d+\.?\s*', '', heading)  # Remove numbering
        if len(heading_clean) > 10 and not any(skip in heading_clean.lower() for skip in ['prior knowledge', 'check', 'introduction']):
            objectives.append(f"<li><strong>Explain</strong> {heading_clean.lower()}</li>")

    # Add a practice objective
    objectives.append(f"<li><strong>Apply</strong> your knowledge through practice problems and examples</li>")

    return '\n        '.join(objectives) if objectives else '<li><strong>Master</strong> the key concepts covered in this lesson</li>'

def add_learning_objectives(filepath):
    """Add learning objectives section to a lesson file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if objectives already exist
    if 'learning objectives' in content.lower() or 'objectives' in content.lower() and '<ul>' in content[:2000]:
        return False, "already has objectives"

    # Extract lesson info
    title = extract_lesson_title(content)
    headings = extract_main_headings(content)

    # Generate objectives
    objectives_list = generate_objectives(title, headings)
    objectives_html = OBJECTIVES_TEMPLATE.format(objectives_list=objectives_list)

    # Find insertion point (after h1, before first h2 or content)
    h1_match = re.search(r'</h1>', content)
    if not h1_match:
        return False, "no h1 tag found"

    insertion_point = h1_match.end()

    # Skip past any subtitle or syllabus reference paragraph
    next_p_match = re.search(r'<p[^>]*>.*?</p>', content[insertion_point:insertion_point+500], re.DOTALL)
    if next_p_match:
        insertion_point += next_p_match.end()

    # Insert objectives
    new_content = content[:insertion_point] + '\n' + objectives_html + '\n' + content[insertion_point:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

    return True, "objectives added"

# Process lessons that are missing objectives
subjects_to_fix = [
    ('physics', 'L*.html', [
        'L2_forces_review.html', 'L3_momentum_impulse.html', 'L4_momentum_applications.html',
        'L6_rigid_body_1.html', 'L7_rigid_body_2.html', 'L8_rigid_body_3.html',
        'L9_relativity_1.html', 'L10_measurement_uncertainty.html', 'L11_relativity_2.html',
        'L12_relativity_3.html', 'L13_relativity_4.html', 'L14_thermal_1.html',
        'L15_thermal_2.html', 'L16_greenhouse_1.html', 'L17_greenhouse_2.html',
        'L18_gas_laws_1.html', 'L20_gas_laws_3.html', 'L21_thermo_1.html',
        'L22_thermo_2.html', 'L23_thermo_3.html', 'L24_circuits_1.html',
        'L26_circuits_3.html', 'L27_circuits_4.html', 'L28_circuits_5.html',
        'L29_shm_1.html', 'L30_shm_2.html', 'L31_shm_3.html', 'L32_shm_4.html',
        'L35_wave_model_3.html', 'L37_wave_phenomena_2.html', 'L38_wave_phenomena_3.html',
        'L39_wave_phenomena_4.html', 'L40_standing_waves_1.html', 'L41_standing_waves_2.html',
        'L42_standing_waves_3.html', 'L43_doppler_1.html', 'L44_doppler_2.html',
        'L45_gravitational_fields_1.html', 'L46_gravitational_fields_2.html',
        'L47_gravitational_fields_3.html', 'L48_em_fields_1.html', 'L49_em_fields_2.html',
        'L50_em_fields_3.html', 'L51_em_fields_4.html', 'L52_motion_em_1.html',
        'L53_motion_em_2.html', 'L54_induction_1.html', 'L55_induction_2.html',
        'L56_induction_3.html', 'L57_atom_1.html', 'L58_atom_2.html',
        'L59_atom_3.html', 'L60_quantum_1.html', 'L61_quantum_2.html',
        'L62_quantum_3.html', 'L63_quantum_4.html', 'L64_radioactive_decay_1.html',
        'L65_radioactive_decay_2.html', 'L66_fission.html', 'L67_fusion_stars.html'
    ]),
    ('math', 'lesson*.html', [
        'lesson2.html', 'lesson3.html', 'lesson4.html', 'lesson5.html', 'lesson6.html',
        'lesson7.html', 'lesson8.html', 'lesson9.html', 'lesson10.html', 'lesson11.html',
        'lesson12.html', 'lesson13.html', 'lesson14.html', 'lesson15.html', 'lesson16.html',
        'lesson17.html', 'lesson18.html', 'lesson19.html', 'lesson20.html', 'lesson21.html',
        'lesson22.html', 'lesson23.html', 'lesson24.html', 'lesson25.html', 'lesson26.html',
        'lesson27.html', 'lesson28.html', 'lesson29.html', 'lesson30.html', 'lesson31.html',
        'lesson32.html', 'lesson33.html', 'lesson34.html', 'lesson35.html', 'lesson36.html',
        'lesson37.html', 'lesson38.html', 'lesson39.html', 'lesson40.html', 'lesson41.html',
        'lesson47.html', 'lesson48.html', 'lesson49.html', 'lesson50.html'
    ]),
    ('economics', 'lesson_*.html', [
        'lesson_10_YED_XED.html', 'lesson_11_PES.html', 'lesson_12_price_controls_ceilings.html',
        'lesson_25_aggregate_demand.html', 'lesson_26_short_run_aggregate_supply.html',
        'lesson_27_long_run_aggregate_supply.html', 'lesson_28_keynesian_as_equilibrium.html',
        'lesson_29_as_shifts_comparing_models.html', 'lesson_30_unemployment_types_measurement.html',
        'lesson_42_tariffs_quotas.html', 'lesson_43_protectionism.html',
        'lesson_44_economic_integration.html', 'lesson_45_floating_exchange_rates.html',
        'lesson_46_consequences_exchange_rate.html', 'lesson_47_exchange_market_intervention.html',
        'lesson_48_balance_of_payments.html', 'lesson_49_understanding_economic_development.html',
        'lesson_50_measuring_development.html', 'lesson_51_poverty_cycles_economic_barriers.html',
        'lesson_52_political_social_barriers.html', 'lesson_53_trade_strategies_development.html',
        'lesson_54_market_based_strategies.html', 'lesson_55_interventionist_strategies_aid.html',
        'lesson_56_fdi_mncs_institutional_change.html', 'lesson_57_sdgs_progress.html',
        'lesson_58_theory_firm_hl.html', 'lesson_59_game_theory_hl.html',
        'lesson_60_asymmetric_info_hl.html', 'lesson_61_price_discrimination_hl.html',
        'lesson_62_contestable_markets_hl.html', 'lesson_63_behavioral_economics_hl.html',
        'lesson_64_monopsony_hl.html', 'lesson_65_efficiency_equity_hl.html',
        'lesson_66_international_finance_hl.html', 'lesson_67_national_income_calc_hl.html'
    ])
]

total_added = 0
total_skipped = 0

for subject, pattern, target_files in subjects_to_fix:
    print("=" * 60)
    print(f"Processing {subject.upper()}")
    print("=" * 60)

    added = 0
    skipped = 0

    for filename in target_files:
        filepath = os.path.join(BASE_DIR, subject, filename)

        if not os.path.exists(filepath):
            print(f"✗ {filename} - file not found")
            skipped += 1
            continue

        success, message = add_learning_objectives(filepath)

        if success:
            print(f"✓ {filename} - {message}")
            added += 1
        else:
            print(f"○ {filename} - {message}")
            skipped += 1

    print(f"\n{subject.upper()}: {added} updated, {skipped} skipped\n")
    total_added += added
    total_skipped += skipped

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"✅ Total lessons updated: {total_added}")
print(f"○ Total lessons skipped: {total_skipped}")
print(f"\nAll learning objectives added successfully!")
