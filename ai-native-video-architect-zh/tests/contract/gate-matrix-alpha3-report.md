# Contract Skill 门禁测试矩阵

- 总测试：45
- 符合预期：45
- 暴露漏洞：0

| 测试 | 预期 | 实际 | 结论 |
|---|---|---|---|
| package_validator | PASS | PASS | 通过 |
| contract_validator | PASS | PASS | 通过 |
| integrity_tamper | BLOCK | BLOCK | 通过 |
| early_finalize | BLOCK | BLOCK | 通过 |
| evaluate_without_submission | BLOCK | BLOCK | 通过 |
| wrong_stage_submission | BLOCK | BLOCK | 通过 |
| S01_candidate_count | BLOCK | BLOCK | 通过 |
| S01_duplicate_concept_id | BLOCK | BLOCK | 通过 |
| S01_selected_missing | BLOCK | BLOCK | 通过 |
| S01_shortlist_too_short | BLOCK | BLOCK | 通过 |
| S01_insufficient_settings | BLOCK | BLOCK | 通过 |
| S01_insufficient_climax_types | BLOCK | BLOCK | 通过 |
| S01_relationship_ratio | BLOCK | BLOCK | 通过 |
| S01_climax_values_identical | BLOCK | BLOCK | 通过 |
| S01_shortlist_ids_exist | BLOCK | BLOCK | 通过 |
| S01_semantic_duplicate_spoof | BLOCK | BLOCK | 通过 |
| G01_missing_evaluator | BLOCK/FAIL | FAIL | 通过 |
| G01_low_total | BLOCK/FAIL | FAIL | 通过 |
| G01_low_originality | BLOCK/FAIL | FAIL | 通过 |
| G01_missing_evidence | BLOCK/FAIL | BLOCK | 通过 |
| G01_hard_failure | BLOCK/FAIL | FAIL | 通过 |
| G01_same_context | BLOCK | BLOCK | 通过 |
| G01_hash_mismatch | BLOCK | BLOCK | 通过 |
| G01_unknown_ref | BLOCK | BLOCK | 通过 |
| G01_valid_pass | PASS | PASS | 通过 |
| G02_missing_visual | BLOCK/FAIL | FAIL | 通过 |
| G02_low_drama | BLOCK/FAIL | FAIL | 通过 |
| G02_mechanism_fail | BLOCK/FAIL | FAIL | 通过 |
| G02_climax_low_subscore | BLOCK/FAIL | FAIL | 通过 |
| G02_climax_counterfactual | BLOCK/FAIL | BLOCK | 通过 |
| G02_semantically_flat_treatment | BLOCK | BLOCK | 通过 |
| G02_valid_pass | PASS | PASS | 通过 |
| G03_dialogue_NA_with_dialogue | BLOCK | BLOCK | 通过 |
| G03_mechanism_NA_with_mechanism | BLOCK | BLOCK | 通过 |
| G03_twist_without_twist_legality_check | BLOCK | BLOCK | 通过 |
| G03_semantically_flat_script | BLOCK | BLOCK | 通过 |
| G03_valid_pass | PASS | PASS | 通过 |
| policy_allowed_preference_patch | APPLY | APPLY | 通过 |
| policy_protected_patch | REJECT | REJECT | 通过 |
| policy_can_weaken_execution_thresholds | REJECT | REJECT | 通过 |
| policy_threshold_bypass_actual | BLOCK | BLOCK | 通过 |
| revision_limit_after_3_failures | CONTRACT_FAILED | CONTRACT_FAILED | 通过 |
| G12_minimal_empty_package_passes | BLOCK | BLOCK | 通过 |
| full_flow_completion_receipt | PASS | PASS | 通过 |
| target_stage_S04_respected | READY_TO_FINALIZE | S04:READY_TO_FINALIZE | 通过 |