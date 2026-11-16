# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dk.theme import new_deck, blank
from dk import sec1, sec2, sec3, sec4
from dk.talk import NOTES

BUILDERS = [
    sec1.s_cover,
    sec1.s_agenda,
    sec1.s_div1,
    sec1.s_what_is_ai,
    sec1.s_timeline,
    sec1.s_ml,
    sec1.s_three_types,
    sec1.s_supervised,
    sec1.s_unsupervised,
    sec1.s_rl,
    sec1.s_deep,
    sec2.s_div2,
    sec2.s_llm,
    sec2.s_training,
    sec2.s_scale,
    sec2.s_limits,
    sec2.s_div3,
    sec2.s_tokens,
    sec2.s_embedding,
    sec2.s_transformer,
    sec2.s_attention,
    sec2.s_gpt,
    sec2.s_context,
    sec2.s_div4,
    sec2.s_why_prompt,
    sec2.s_anatomy,
    sec2.s_principles,
    sec2.s_techniques1,
    sec2.s_techniques2,
    sec2.s_before_after,
    sec2.s_practice,
    sec2.s_checklist,
    sec3.s_div5,
    sec3.s_toolmap,
    sec3.s_text_tools,
    sec3.s_visual_tools,
    sec3.s_audio_tools,
    sec3.s_code_tools,
    sec3.s_matrix,
    sec3.s_div6,
    sec3.s_agent,
    sec3.s_chat_vs_agent,
    sec3.s_agent_parts,
    sec3.s_mcp,
    sec3.s_agent_use,
    sec3.s_div7,
    sec3.s_claude,
    sec3.s_claude_code,
    sec3.s_claude_vs,
    sec4.s_div8,
    sec4.s_install,
    sec4.s_free,
    sec4.s_ollama,
    sec4.s_interaction,
    sec4.s_div9,
    sec4.s_build_web,
    sec4.s_build_code,
    sec4.s_motion,
    sec4.s_automate,
    sec4.s_nl_tools,
    sec4.s_div10,
    sec4.s_trends,
    sec4.s_work,
    sec4.s_skills,
    sec4.s_ethics,
    sec4.s_summary,
    sec4.s_resources,
    sec4.s_qa,
]


def main(out="AI-Seminar.pptx"):
    prs = new_deck()
    total = len(BUILDERS)
    for i, fn in enumerate(BUILDERS):
        s = blank(prs)
        fn(s, i + 1, total)
        note = NOTES.get(i + 1)
        if note:
            s.notes_slide.notes_text_frame.text = note
    cp = prs.core_properties
    cp.title = "هوش مصنوعی: از صفر تا ایجنت"
    cp.subject = "سمینار هوش مصنوعی"
    cp.author = "AI Seminar"
    cp.language = "fa-IR"
    prs.save(out)
    print("saved", out, len(BUILDERS), "slides")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "AI-Seminar.pptx")
