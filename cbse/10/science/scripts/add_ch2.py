import json
import re
import os

def get_content_ch2():
    c = []
    c.append({"type": "heading", "level": 1, "content": "Acids, Bases and Salts"})
    c.append({"type": "text", "content": "You have learnt in your previous classes that the sour and bitter tastes of food are due to acids and bases, respectively, present in them. If someone in the family is suffering from a problem of acidity after overeating, baking soda solution is a suggested remedy."})
    c.append({"type": "heading", "level": 2, "content": "2.1 Understanding the Chemical Properties of Acids and Bases"})
    c.append({"type": "heading", "level": 3, "content": "2.1.1 Acids and Bases in the Laboratory"})
    c.append({"type": "activity", "title": "Activity 2.1: Testing with Indicators", "content": "Collect solutions like HCl, H2SO4, HNO3, CH3COOH, NaOH, Ca(OH)2, KOH, Mg(OH)2, and NH4OH. Test them with various indicators (red litmus, blue litmus, phenolphthalein, and methyl orange)."})
    c.append({"type": "text", "content": "Acids turn blue litmus red. Bases turn red litmus blue. Synthetic indicators like phenolphthalein (colorless in acid, pink in base) and methyl orange (red in acid, yellow in base) are also used."})
    c.append({"type": "heading", "level": 3, "content": "2.1.2 How do Acids and Bases React with Metals?"})
    c.append({"type": "text", "content": "When an acid reacts with a metal, hydrogen gas is evolved and a salt is formed.\n\nAcid + Metal → Salt + Hydrogen gas\n\n$$\\ce{Zn + H2SO4 -> ZnSO4 + H2}$$ "})
    c.append({"type": "text", "content": "Bases also react with some metals to form salts and hydrogen gas.\n\n$$\\ce{2NaOH + Zn -> Na2ZnO2 + H2}$$ (Sodium zincate)"})
    c.append({"type": "heading", "level": 3, "content": "2.1.3 Reaction of Metal Carbonates and Metal Hydrogencarbonates with Acids"})
    c.append({"type": "text", "content": "All metal carbonates and hydrogencarbonates react with acids to give a corresponding salt, carbon dioxide and water.\n\nMetal carbonate/Metal hydrogencarbonate + Acid → Salt + Carbon dioxide + Water\n\n$$\\ce{Na2CO3(s) + 2HCl(aq) -> 2NaCl(aq) + H2O(l) + CO2(g)}$$\n$$\\ce{NaHCO3(s) + HCl(aq) -> NaCl(aq) + H2O(l) + CO2(g)}$$"})
    c.append({"type": "heading", "level": 3, "content": "2.1.4 How do Acids and Bases React with each other?"})
    c.append({"type": "text", "content": "The reaction between an acid and a base to give a salt and water is known as a neutralisation reaction.\n\nBase + Acid → Salt + Water\n\n$$\\ce{NaOH(aq) + HCl(aq) -> NaCl(aq) + H2O(l)}$$"})
    c.append({"type": "heading", "level": 2, "content": "2.2 What do all Acids and all Bases have in Common?"})
    c.append({"type": "text", "content": "All acids generate hydrogen gas on reacting with metals, so hydrogen seems to be common to all acids. Acids produce $\\ce{H+(aq)}$ ions in solution, which are responsible for their acidic properties. Similarly, bases produce $\\ce{OH-(aq)}$ ions in water."})
    c.append({"type": "heading", "level": 2, "content": "2.3 How Strong are Acid or Base Solutions?"})
    c.append({"type": "text", "content": "A scale for measuring hydrogen ion concentration in a solution, called pH scale, has been developed. The p in pH stands for 'potenz' in German, meaning power. On the pH scale we can measure pH generally from 0 (very acidic) to 14 (very alkaline)."})
    c.append({"type": "list", "items": ["Neutral solution: pH = 7", "Acidic solution: pH < 7", "Basic solution: pH > 7"]})
    c.append({"type": "heading", "level": 2, "content": "2.4 More about Salts"})
    c.append({"type": "text", "content": "Salts of a strong acid and a strong base are neutral with pH value of 7. Salts of a strong acid and weak base are acidic with pH value less than 7. Salts of a strong base and weak acid are basic with pH value more than 7."
})
    c.append({"type": "heading", "level": 3, "content": "Common Salt and its Chemicals"})
    c.append({"type": "text", "content": "Common salt (\\ce{NaCl}$) is an important raw material for various materials of daily use, such as sodium hydroxide, baking soda, washing soda, bleaching powder and many more."})
    c.append({"type": "list", "items": ["Bleaching Powder: $\\ce{CaOCl2}$", "Baking Soda: $\\ce{NaHCO3}$", "Washing Soda: $\\ce{Na2CO3.10H2O}$", "Plaster of Paris: $\\ce{CaSO4.1/2H2O}$"]})
    return c

def get_quiz_ch2():
    q = []
    q.append({"id": "ch2-q1", "question": "What is the pH of a neutral solution?", "options": ["0", "7", "14", "1"], "correctAnswer": 1, "explanation": "A neutral solution has a pH of exactly 7."})
    q.append({"id": "ch2-q2", "question": "Which ion is responsible for acidic properties?", "options": ["OH-", "H+", "Cl-", "Na+"], "correctAnswer": 1, "explanation": "H+ (or H3O+) ions are responsible for acidic nature."})
    q.append({"id": "ch2-q3", "question": "What is formed when an acid reacts with a metal carbonate?", "options": ["Salt and Hydrogen", "Salt, Water and CO2", "Base and Water", "Only Salt"], "correctAnswer": 1, "explanation": "Acid + Metal Carbonate -> Salt + Water + Carbon Dioxide."})
    q.append({"id": "ch2-q4", "question": "What is the chemical name of Bleaching Powder?", "options": ["Calcium sulphate", "Calcium oxychloride", "Sodium carbonate", "Sodium bicarbonate"], "correctAnswer": 1, "explanation": "Bleaching powder is Calcium oxychloride (CaOCl2)."})
    q.append({"id": "ch2-q5", "question": "Which of the following is an antacid?", "options": ["Vinegar", "Lemon juice", "Milk of magnesia", "Hydrochloric acid"], "correctAnswer": 2, "explanation": "Milk of magnesia [Mg(OH)2] is a mild base used as an antacid."})
    return q

def get_flashcards_ch2():
    f = []
    f.append({"id": "ch2-f1", "front": "Acid", "back": "Substance that turns blue litmus red and has pH < 7."})
    f.append({"id": "ch2-f2", "front": "Base", "back": "Substance that turns red litmus blue and has pH > 7."})
    f.append({"id": "ch2-f3", "front": "Neutralisation", "back": "Reaction between acid and base to form salt and water."})
    f.append({"id": "ch2-f4", "front": "pH Scale", "back": "Scale from 0-14 measuring H+ ion concentration."})
    f.append({"id": "ch2-f5", "front": "Baking Soda", "back": "Sodium hydrogencarbonate (NaHCO3)."})
    f.append({"id": "ch2-f6", "front": "Washing Soda", "back": "Sodium carbonate decahydrate (Na2CO3.10H2O)."})
    f.append({"id": "ch2-f7", "front": "Plaster of Paris", "back": "Calcium sulphate hemihydrate (CaSO4.1/2H2O)."})
    return f

def get_summary_ch2():
    return [
        "Acid-base indicators are dyes which indicate the presence of acids and bases.",
        "Acidic nature is due to H+(aq) ions; basic nature is due to OH-(aq) ions.",
        "Acid + Metal -> Salt + Hydrogen gas.",
        "Base + Metal -> Salt + Hydrogen gas.",
        "Acid + Metal Carbonate/Hydrogencarbonate -> Salt + CO2 + Water.",
        "Acid + Base -> Salt + Water (Neutralisation).",
        "pH scale (0-14) measures the strength of acids and bases.",
        "Neutral pH = 7, Acidic pH < 7, Basic pH > 7.",
        "Salts have various uses in daily life and industry."
    ]

def get_exercises_ch2():
    return [
        "1. A solution turns red litmus blue, its pH is likely to be (a) 1 (b) 4 (c) 5 (d) 10",
        "2. A solution reacts with crushed egg-shells to give a gas that turns lime-water milky. The solution contains (a) NaCl (b) HCl (c) LiCl (d) KCl",
        "3. 10 mL of NaOH is neutralised by 8 mL of HCl. How much HCl is needed for 20 mL of NaOH? (a) 4 mL (b) 8 mL (c) 12 mL (d) 16 mL",
        "4. Which medicine is used for treating indigestion? (a) Antibiotic (b) Analgesic (c) Antacid (d) Antiseptic",
        "5. Write balanced equations for: (a) Dilute H2SO4 + Zn, (b) Dilute HCl + Mg, (c) Dilute H2SO4 + Al, (d) Dilute HCl + Fe."
    ]

def get_formulae_ch2():
    return [
        "$$\\ce{Acid + Metal -> Salt + H2}$$ ",
        "$$\\ce{Base + Metal -> Salt + H2}$$ ",
        "$$\\ce{Acid + Base -> Salt + H2O}$$ ",
        "$$\\ce{Acid + Metal Carbonate -> Salt + H2O + CO2}$$ ",
        "$$\\ce{CaOCl2}$$ (Bleaching Powder)",
        "$$\\ce{NaHCO3}$$ (Baking Soda)",
        "$$\\ce{Na2CO3.10H2O}$$ (Washing Soda)",
        "$$\\ce{CaSO4 . 1/2 H2O}$$ (Plaster of Paris)"
    ]

# Original Lesson 1 data
import sys
import os

# We will read the existing lessons.ts to preserve Chapter 1
# Actually, it's easier to just construct the whole list in the python script.

def get_lesson_1():
    # This is a simplified version of Lesson 1 to keep the script manageable, 
    # but we should ideally read the existing data.
    # For now, I will manually include Lesson 1 data here to ensure both exist.
    # (In a production system, we'd append to the JSON or use a database)
    
    # I'll re-fetch Lesson 1 data from my previous successful turn
    # but to save tokens, I will just focus on adding Lesson 2 and 
    # assuming I need to maintain the full list.
    pass

# I'll read src/data/lessons.ts to get Lesson 1
import re

with open('src/data/lessons.ts', 'r') as f:
    ts_content = f.read()
    # Extract the JSON array part
    match = re.search(r'export const lessons: Lesson\[\] = (.*\].*);', ts_content, re.DOTALL)
    if match:
        existing_lessons = json.loads(match.group(1))
    else:
        existing_lessons = []

new_lesson = {
    "id": "chem-02",
    "subject": "Chemistry",
    "title": "Acids, Bases and Salts",
    "chapterNumber": 2,
    "content": get_content_ch2(),
    "quiz": get_quiz_ch2(),
    "flashcards": get_flashcards_ch2(),
    "summary": get_summary_ch2(),
    "exercises": get_exercises_ch2(),
    "formulae": get_formulae_ch2()
}

# Update or Append
found = False
for i, l in enumerate(existing_lessons):
    if l['id'] == new_lesson['id']:
        existing_lessons[i] = new_lesson
        found = True
        break
if not found:
    existing_lessons.append(new_lesson)

ts_header = """
export type ContentBlock = 
  | { type: 'text'; content: string }
  | { type: 'image'; src: string; alt: string; caption?: string }
  | { type: 'heading'; level: 1 | 2 | 3; content: string }
  | { type: 'list'; items: string[] }
  | { type: 'activity'; title: string; content: string; warning?: string };

export type QuizQuestion = {
  id: string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
};

export type Flashcard = {
  id: string;
  front: string;
  back: string;
};

export type Lesson = {
  id: string;
  subject: 'Chemistry' | 'Physics' | 'Biology';
  title: string;
  chapterNumber: number;
  content: ContentBlock[];
  quiz: QuizQuestion[];
  flashcards: Flashcard[];
  summary: string[];
  exercises: string[];
  formulae: string[];
};

"""

with open('src/data/lessons.ts', 'w') as f:
    f.write(ts_header)
    f.write(f"export const lessons: Lesson[] = {json.dumps(existing_lessons, indent=2)};\n")