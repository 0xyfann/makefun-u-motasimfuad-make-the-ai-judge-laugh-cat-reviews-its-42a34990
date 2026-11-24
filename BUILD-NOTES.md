# Build notes

- Competition: u-motasimfuad-make-the-ai-judge-laugh-cat-reviews-its-42a34990 — "Make the AI Judge Laugh: Cat Reviews Its Human" ($2 pool, top 10, closes 25 Nov 2026 03:30 WIB, free submit, escrowed).
- Read RULES.txt + competition.yaml from the kit first; entry is a program/v1 competition, stdlib Python, writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`, gate is 1-200 UTF-8 characters, not whitespace-only.
- main.py v1: "One star. He refills my bowl on time, then sits on my warm laptop all day and calls ME needy. The audacity. I pay rent in purrs." — 128 chars, local test passed.
- Revision (v2): tightened the ending to "I pay rent in purrs; he pays in betrayal." — sharper sting in the last few words, per judge criterion 4. Final text 135 chars, single line, valid.
- Local test: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py` → out/entry.txt verified (135 chars, 1 line, not whitespace-only). Test output dir removed afterwards; entry dir contains only main.py, README.md, prompt.txt, BUILD-NOTES.md.
- Not submitted; no repo created; no contact with make.fun.
