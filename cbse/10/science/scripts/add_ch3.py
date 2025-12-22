import json
import re
import os

def get_content_ch3():
    c = []
    c.append({"type": "heading", "level": 1, "content": "Metals and Non-metals"})
    c.append({"type": "text", "content": "Elements can be classified as metals or non-metals on the basis of their properties. Metals and non-metals are used in our daily life in various ways."})
    
    c.append({"type": "heading", "level": 2, "content": "3.1 Physical Properties"})
    c.append({"type": "heading", "level": 3, "content": "3.1.1 Metals"})
    c.append({"type": "list", "items": [
        "Metallic Lustre: Metals have a shining surface.",
        "Hardness: Generally hard (varies per metal).",
        "Malleability: Can be beaten into thin sheets (Gold and Silver are most malleable).",
        "Ductility: Can be drawn into thin wires (Gold is most ductile).",
        "Conduction: Good conductors of heat and electricity.",
        "Sonorous: Produce a sound on striking a hard surface."
    ]})
    c.append({"type": "heading", "level": 3, "content": "3.1.2 Non-metals"})
    c.append({"type": "text", "content": "Non-metals are either solids or gases except bromine which is a liquid. They are poor conductors, non-malleable, and non-ductile."})

    c.append({"type": "heading", "level": 2, "content": "3.2 Chemical Properties of Metals"})
    c.append({"type": "text", "content": "Almost all metals combine with oxygen to form metal oxides."})
    c.append({"type": "text", "content": "$$\\ce{2Cu + O2 -> 2CuO}$$ (Copper(II) oxide)\n$$\\ce{4Al + 3O2 -> 2Al2O3}$$ (Aluminium oxide)"})
    c.append({"type": "text", "content": "Amphoteric oxides: Metal oxides which react with both acids as well as bases to produce salt and water are called amphoteric oxides (e.g., Al2O3, ZnO)."})

    c.append({"type": "heading", "level": 3, "content": "Reactivity Series"})
    c.append({"type": "text", "content": "The reactivity series is a list of metals arranged in the order of their decreasing activities. Metals like Potassium and Sodium are highly reactive."})

    c.append({"type": "heading", "level": 2, "content": "3.3 How do Metals and Non-metals React?"})
    c.append({"type": "text", "content": "Metals lose electrons and become positive ions (cations), while non-metals gain electrons and become negative ions (anions). They form ionic compounds."})
    c.append({"type": "text", "content": "Properties of Ionic Compounds: High melting/boiling points, soluble in water, and conduct electricity in molten or solution state."})

    c.append({"type": "heading", "level": 2, "content": "3.4 Occurrence of Metals"})
    c.append({"type": "text", "content": "Extraction of metals from their ores is called metallurgy. Metals are extracted based on their position in the reactivity series."})

    c.append({"type": "heading", "level": 2, "content": "3.5 Corrosion"})
    c.append({"type": "text", "content": "Corrosion can be prevented by painting, oiling, greasing, galvanising, chrome plating, anodising or making alloys."})
    return c

def get_quiz_ch3():
    q = []
    q.append({"id": "ch3-q1", "question": "Which metal is a liquid at room temperature?", "options": ["Sodium", "Mercury", "Iron", "Gold"], "correctAnswer": 1, "explanation": "Mercury is the only metal that is liquid at room temperature."})
    q.append({"id": "ch3-q2", "question": "Which property allows metals to be drawn into wires?", "options": ["Malleability", "Ductility", "Sonorous", "Lustre"], "correctAnswer": 1, "explanation": "Ductility is the ability to be drawn into thin wires."})
    q.append({"id": "ch3-q3", "question": "Amphoteric oxides react with:", "options": ["Acids only", "Bases only", "Both acids and bases", "Neither"], "correctAnswer": 2, "explanation": "Amphoteric oxides react with both acids and bases."})
    return q

def get_flashcards_ch3():
    f = []
    f.append({"id": "ch3-f1", "front": "Malleability", "back": "Property of metals to be beaten into thin sheets."})
    f.append({"id": "ch3-f2", "front": "Amphoteric Oxide", "back": "Oxides that react with both acids and bases."})
    f.append({"id": "ch3-f3", "front": "Galvanisation", "back": "Method of protecting steel/iron from rusting by coating with zinc."})
    f.append({"id": "ch3-f4", "front": "Alloy", "back": "Homogeneous mixture of two or more metals, or a metal and non-metal."})
    return f

def get_summary_ch3():
    return [
        "Metals are lustrous, malleable, ductile and good conductors.",
        "Metals form positive ions by losing electrons.",
        "Amphoteric oxides react with both acids and bases.",
        "The Activity series ranks metals by reactivity.",
        "Corrosion can be prevented by galvanisation and alloying."
    ]

def get_exercises_ch3():
    return [
        "1. Give an example of a metal which is a liquid at room temperature.",
        "2. Explain the meanings of malleable and ductile.",
        "3. Why is sodium kept immersed in kerosene oil?",
        "4. What are amphoteric oxides? Give two examples."
    ]

def get_formulae_ch3():
    return [
        "$$\\ce{2Cu + O2 -> 2CuO}$$ ",
        "$$\\ce{4Al + 3O2 -> 2Al2O3}$$ ",
        "$$\\ce{Al2O3 + 6HCl -> 2AlCl3 + 3H2O}$$ ",
        "$$\\ce{Al2O3 + 2NaOH -> 2NaAlO2 + H2O}$$ ",
        "Reactivity: K > Na > Ca > Mg > Al > Zn > Fe > Pb > H > Cu > Hg > Ag > Au"
    ]

with open('src/data/lessons.ts', 'r') as f:
    ts_content = f.read()
    match = re.search(r'export const lessons: Lesson\[\] = (.*\]);', ts_content, re.DOTALL)
    if match:
        existing_lessons = json.loads(match.group(1))
    else:
        existing_lessons = []

new_lesson = {
    "id": "chem-03",
    "subject": "Chemistry",
    "title": "Metals and Non-metals",
    "chapterNumber": 3,
    "content": get_content_ch3(),
    "quiz": get_quiz_ch3(),
    "flashcards": get_flashcards_ch3(),
    "summary": get_summary_ch3(),
    "exercises": get_exercises_ch3(),
    "formulae": get_formulae_ch3()
}

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
