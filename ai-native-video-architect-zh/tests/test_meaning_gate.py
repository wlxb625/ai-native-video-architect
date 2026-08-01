from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("runner", ROOT / "scripts" / "contract_runner.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

def thematic(**overrides):
    d = {
        "profile":"THEMATIC_MEANING_REQUIRED", "genre_basis":"STANDARD_NARRATIVE",
        "human_question":"普通执行者明知程序被篡改时是否仍能以服从免责",
        "competing_value_a":"维持公共秩序与家庭安全", "competing_value_b":"拒绝参与不可逆伤害",
        "protagonist_initial_belief":"小人物只需完成自己的职责", "belief_pressure_or_change":"他发现每个合规小步骤正在共同制造死亡",
        "climax_thematic_answer":"他拒绝敲下最后一锣并承担同罪后果", "ending_residue_or_question":"制度恢复后个人责任仍无法被规章完全代替",
        "contemporary_relevance":"回应现实中按流程办事与责任分散的问题", "why_worth_telling":"让观众重新判断服从与责任的边界",
        "generic_theme_risk":"避免退化为好人反抗坏官的单向正义故事"
    }
    d.update(overrides); return d

def formal(**overrides):
    d={"profile":"FORMAL_ABSURDIST_EXCEPTION","genre_basis":"ABSURDIST","formal_intent":"用不断交换用途的日常物件制造身份失稳",
       "audience_experience":"让观众先发笑再逐渐失去判断物件用途的安全感","pattern_logic":"每次交换都遵循尺寸递减和声音增大的规则",
       "formal_culmination":"最后人物自身被当成物件登记并完成模式反转","anti_randomness_proof":"所有无因果事件都由同一交换规则和声响递进控制",
       "why_exception_applies":"作品核心是荒诞形式体验，改成因果叙事会破坏观看机制"}
    d.update(overrides); return d

def run():
    cases=[]
    cases.append(("valid_thematic", runner._check_meaning_unit(thematic(), "x", "COMMERCIAL"), True))
    cases.append(("generic_theme_rejected", runner._check_meaning_unit(thematic(human_question="成长"), "x", "COMMERCIAL"), False))
    cases.append(("valid_absurdist", runner._check_meaning_unit(formal(), "x", "EXPERIMENTAL"), True))
    cases.append(("exception_abuse_rejected", runner._check_meaning_unit(formal(), "x", "COMMERCIAL"), False))
    cases.append(("random_exception_rejected", runner._check_meaning_unit(formal(pattern_logic="随机"), "x", "EXPERIMENTAL"), False))
    failed=[]
    for name, errors, should_pass in cases:
        ok = not errors
        if ok != should_pass: failed.append((name, errors, should_pass))
        print(name, "PASS" if ok else "REJECT", errors)
    if failed: raise SystemExit(f"failed: {failed}")
if __name__ == '__main__': run()
